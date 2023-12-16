import sys
import unittest
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from unittest.mock import patch
print('Original sys.path:', sys.path)
#sys.path.append('/path/to/directory')
from Code.Simulation import TissueSimulationGUI

class TestTissueSimulationGUI(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = TissueSimulationGUI()

    def tearDown(self):
        self.gui.close()
        del self.gui
        del self.app

    
    def test_initialization(self):
        # Check if the GUI is initialized properly
        self.assertIsInstance(self.gui, TissueSimulationGUI)
        self.assertEqual(self.gui.windowTitle(), 'Tissue Simulation GUI')

        # Check if required widgets are present
        self.assertIsInstance(self.gui.x_label, QLabel)
        self.assertIsInstance(self.gui.x_input, QLineEdit)
        self.assertIsInstance(self.gui.y_label, QLabel)
        self.assertIsInstance(self.gui.y_input, QLineEdit)
        self.assertIsInstance(self.gui.min_shear_label, QLabel)
        self.assertIsInstance(self.gui.min_shear_input, QLineEdit)
        self.assertIsInstance(self.gui.max_shear_label, QLabel)
        self.assertIsInstance(self.gui.max_shear_input, QLineEdit)
        self.assertIsInstance(self.gui.permeability_label, QLabel)
        self.assertIsInstance(self.gui.permeability_input, QLineEdit)
        self.assertIsInstance(self.gui.viscosity_label, QLabel)
        self.assertIsInstance(self.gui.viscosity_input, QLineEdit)
        self.assertIsInstance(self.gui.simulate_button, QPushButton)
        self.assertIsInstance(self.gui.mpl_widget, MplWidget)

    def test_start_simulation(self):
        # Simulate a button click and check if the animation object is created
        with patch('matplotlib.pyplot.show') as mock_show:
            self.gui.x_input.setText('10')
            self.gui.y_input.setText('10')
            self.gui.min_shear_input.setText('0')
            self.gui.max_shear_input.setText('100')
            self.gui.permeability_input.setText('1')
            self.gui.viscosity_input.setText('1')
            self.gui.simulate_button.click()
            self.assertIsNotNone(self.gui.ani)

    def test_simulation_with_invalid_input(self):
        # Simulate a button click with invalid input and check if it handles gracefully
        with patch('matplotlib.pyplot.show') as mock_show:
            self.gui.x_input.setText('invalid_input')
            self.gui.y_input.setText('10')
            self.gui.min_shear_input.setText('0')
            self.gui.max_shear_input.setText('100')
            self.gui.permeability_input.setText('1')
            self.gui.viscosity_input.setText('1')
            self.gui.simulate_button.click()
            self.assertIsNone(self.gui.ani)

if __name__ == '__main__':
    unittest.main()
