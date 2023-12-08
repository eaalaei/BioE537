import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap

class MplWidget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.axes = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)

class TissueSimulationGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.ani = None  # Store the animation object

    def init_ui(self):
        # Create a label for the top image
        folchlab_image = QLabel(self)
        folchlab_pixmap = QPixmap('folchlab.webp')  # Provide the correct path to your image file
        folchlab_image.setPixmap(folchlab_pixmap)

        # Create labels and input fields
        self.x_label = QLabel('X Dimension:')
        self.x_input = QLineEdit(self)

        self.y_label = QLabel('Y Dimension:')
        self.y_input = QLineEdit(self)

        self.min_shear_label = QLabel('Min Shear Stress:')
        self.min_shear_input = QLineEdit(self)

        self.max_shear_label = QLabel('Max Shear Stress:')
        self.max_shear_input = QLineEdit(self)

        self.permeability_label = QLabel('Permeability:')
        self.permeability_input = QLineEdit(self)

        self.viscosity_label = QLabel('Viscosity:')
        self.viscosity_input = QLineEdit(self)

        # Create a button to trigger the simulation
        self.simulate_button = QPushButton('Simulate', self)
        self.simulate_button.clicked.connect(self.start_simulation)

        # Create a layout for the top image
        top_layout = QVBoxLayout()
        top_layout.addWidget(folchlab_image)

        # Create a layout for input fields
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.x_label)
        input_layout.addWidget(self.x_input)
        input_layout.addWidget(self.y_label)
        input_layout.addWidget(self.y_input)
        input_layout.addWidget(self.min_shear_label)
        input_layout.addWidget(self.min_shear_input)
        input_layout.addWidget(self.max_shear_label)
        input_layout.addWidget(self.max_shear_input)
        input_layout.addWidget(self.permeability_label)
        input_layout.addWidget(self.permeability_input)
        input_layout.addWidget(self.viscosity_label)
        input_layout.addWidget(self.viscosity_input)
        input_layout.addWidget(self.simulate_button)

        # Create a layout for the image
        image_layout = QVBoxLayout()
        tissue_image = QLabel(self)
        pixmap = QPixmap('tissue.png')  # Provide the correct path to your image file
        tissue_image.setPixmap(pixmap.scaledToWidth(400))  # Adjust the width as needed
        image_layout.addWidget(tissue_image)

        # Create a layout for the matplotlib plot
        plot_layout = QVBoxLayout()
        self.mpl_widget = MplWidget(self)
        plot_layout.addWidget(self.mpl_widget)

        # Create a horizontal layout to arrange input, image, and plot layouts
        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(image_layout)
        main_layout.addLayout(plot_layout)

        # Create a vertical layout to arrange top image and the horizontal layout
        final_layout = QVBoxLayout()
        final_layout.addLayout(top_layout)
        final_layout.addLayout(main_layout)

        # Set the layout for the main window
        self.setLayout(final_layout)

        # Set the window properties
        self.setWindowTitle('Tissue Simulation GUI')
        self.setGeometry(100, 100, 800, 500)

    def start_simulation(self):
        # Retrieve user inputs
        x_dimension = float(self.x_input.text())
        y_dimension = float(self.y_input.text())
        min_shear_stress = float(self.min_shear_input.text() if self.min_shear_input.text() else 0)
        max_shear_stress = float(self.max_shear_input.text())
        permeability = float(self.permeability_input.text())
        viscosity = float(self.viscosity_input.text())

        # Perform the simulation using the provided inputs
        plate_length_x = int(x_dimension)
        plate_length_y = int(y_dimension)
        max_iter_time = 200

        alpha = permeability / viscosity
        delta_x = 1
        delta_t = (delta_x ** 2) / (4 * alpha)
        gamma = (alpha * delta_t) / (delta_x ** 2)

        # Initialize solution: the grid of u(k, i, j)
        p = np.empty((max_iter_time, plate_length_x, plate_length_y))

        # Initial condition everywhere inside the grid
        p_initial = 0

        # Boundary conditions
        p_top = 101.0
        p_left = 0.0
        p_bottom = 0.0
        p_right = 0.0

        # Set the initial condition
        p.fill(p_initial)

        # Set the boundary conditions
        p[:, (plate_length_x - 1):, :] = p_top
        p[:, :, :1] = p_left
        p[:, :1, 1:] = p_bottom
        p[:, :, (plate_length_y - 1):] = p_right

        def calculate(p):
            for k in range(0, max_iter_time - 1, 1):
                for i in range(1, plate_length_x - 1, delta_x):
                    for j in range(1, plate_length_y - 1, delta_x):
                        p[k + 1, i, j] = gamma * (p[k][i + 1][j] + p[k][i - 1][j] + p[k][i][j + 1] + p[k][i][j - 1] - 4 * p[k][i][j]) + p[k][i][j]

            return p

        # Do the calculation here
        p = calculate(p)

        def update(frame):
            self.mpl_widget.axes.clear()
            im = self.mpl_widget.axes.pcolormesh(p[frame, :, :], cmap=plt.cm.jet, vmin=0, vmax=100)
            self.mpl_widget.axes.set_title(f"Pressure at t = {frame * delta_t/100:.3f} unit time")
            self.mpl_widget.axes.set_xlabel("x")
            self.mpl_widget.axes.set_ylabel("y")
            return im  # Return the image object

        # Create the animation
        self.ani = FuncAnimation(self.mpl_widget.figure, update, frames=max_iter_time, interval=100, repeat=False)

        # Show the animation within the PyQt5 GUI
        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = TissueSimulationGUI()
    gui.show()
    sys.exit(app.exec_())
