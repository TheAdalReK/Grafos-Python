from PySide2.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys

# Aplicacion de QT
app = QApplication()

window = MainWindow()
window.show()

# QT Loop
sys.exit(app.exec_())