import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QSplitter
from PyQt5.QtGui import QPixmap

class TissueSimulationGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

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

        self.density_label = QLabel('Density:')
        self.density_input = QLineEdit(self)

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
        input_layout.addWidget(self.density_label)
        input_layout.addWidget(self.density_input)
        input_layout.addWidget(self.viscosity_label)
        input_layout.addWidget(self.viscosity_input)
        input_layout.addWidget(self.simulate_button)

        # Create a layout for the image
        image_layout = QVBoxLayout()
        tissue_image = QLabel(self)
        pixmap = QPixmap('tissue.png')  # Provide the correct path to your image file
        tissue_image.setPixmap(pixmap.scaledToWidth(400))  # Adjust the width as needed (approximately 2 times the original size)
        image_layout.addWidget(tissue_image)

        # Create a horizontal layout to arrange input and image layouts
        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(image_layout)

        # Create a vertical layout to arrange top image and the horizontal layout
        final_layout = QVBoxLayout()
        final_layout.addLayout(top_layout)
        final_layout.addLayout(main_layout)

        # Set the layout for the main window
        self.setLayout(final_layout)

        # Set the window properties
        self.setWindowTitle('Tissue Simulation GUI')
        self.setGeometry(100, 100, 600, 500)

    def start_simulation(self):
        # Retrieve user inputs
        x_dimension = float(self.x_input.text())
        y_dimension = float(self.y_input.text())
        min_shear_stress = float(self.min_shear_input.text() if self.min_shear_input.text() else 0)
        max_shear_stress = float(self.max_shear_input.text())
        permeability = float(self.permeability_input.text())
        density = float(self.density_input.text())
        viscosity = float(self.viscosity_input.text())

        # TODO: Perform the simulation using the provided inputs
        # This is where you would integrate with DarcyTools and Pyomo packages

        # For now, let's print the inputs for demonstration purposes
        print(f"Simulating with inputs: X={x_dimension}, Y={y_dimension}, Min Shear Stress={min_shear_stress}, Max Shear Stress={max_shear_stress}, Permeability={permeability}, Density={density}, Viscosity={viscosity}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = TissueSimulationGUI()
    gui.show()
    sys.exit(app.exec_())
