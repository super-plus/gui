from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.listwidget = QListWidget()
        self.get_servers()
        layout.addWidget(self.listwidget)

    def get_servers(self):
        self.listwidget.insertItem(0, "NASA")
        self.listwidget.insertItem(1, "FBI")
        self.listwidget.insertItem(2, "CPR")
        self.listwidget.insertItem(3, "YOURMOM.COM")
        self.listwidget.insertItem(4, "LEGOLAI.DK")


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
