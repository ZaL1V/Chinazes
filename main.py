import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_MainWindow
from minecraft_launcher import launch_minecraft


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
