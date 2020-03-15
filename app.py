import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import uic

class App(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('appUI.ui', self)
        self.progressBar.

        def prueba(self):
            print("hey")
    

app=QApplication(sys.argv)
mainFrame=App()
mainFrame.show()
sys.exit(app.exec_())