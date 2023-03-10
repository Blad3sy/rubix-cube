from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class Application(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
    
class Window(QMainWindow):
    
    def __init__(self, title, width, height):
        super().__init__()

        self.xPos = 200
        self.yPos = 200
        self.width = width
        self.height = height
        self.title = title

        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setWindowTitle(self.title)

        self.show()

class Central_Widget(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        parent.setCentralWidget(self)

class Layout(QVBoxLayout):

    def __init__(self, parent):
        QVBoxLayout.__init__(self, parent)
        self.setAlignment(Qt.AlignTop)

class Main_Window():

    def __init__(self, title, width, height):
        self.width = width
        self.height = height
        self.title = title

        self.app = Application()
        self.win = Window(self.title, self.width, self.height)
        self.cen = Central_Widget(self.win)
        self.lay = Layout(self.cen)

class Sub_Window():

    def __init__(self, title, width, height):
        self.width = width
        self.height = height
        self.title = title

        self.win = Window(self.title, self.width, self.height)
        self.cen = Central_Widget(self.win)
        self.lay = Layout(self.cen)

class Label(QLabel):
    
    def __init__(self, parent, text, alignment):
        super().__init__()
        
        parent.addWidget(self)
        self.text = text
        self.alignment = alignment

        self.setText(self.text)
        self.setWordWrap(True)

        self.show()

        if self.alignment == "L":
            self.setAlignment(Qt.AlignLeft)
        elif self.alignment == "C":
            self.setAlignment(Qt.AlignCenter)
        else:
            self.setAlignment(Qt.AlignRight)
    
class Image(QLabel):

    def __init__(self, parent, image, width, height, keepAspectRatio, alignment):
        super().__init__()

        parent.addWidget(self)
        self.image = QPixmap(image)
        self.width = width
        self.height = height
        self.alignment = alignment
        self.keepAspectRatio = keepAspectRatio

        if keepAspectRatio:
            self.image = self.image.scaled(self.width, self.height, Qt.KeepAspectRatio)
        else:
            self.image = self.image.scaled(self.width, self.height)

        if self.alignment == "L":
            self.setAlignment(Qt.AlignLeft)
        elif self.alignment == "C":
            self.setAlignment(Qt.AlignCenter)
        else:
            self.setAlignment(Qt.AlignRight)

        self.setPixmap(self.image)

        self.show()

class Button(QPushButton):

    def __init__(self, parent, command, text):
        super().__init__()
        
        parent.addWidget(self)
        self.text = text

        self.clicked.connect(command)
        self.setText(self.text)

        self.show()

class Grid(QGridLayout):

    def __init__(self, parent):
        super().__init__()
        self.trueParent = super()
        self.parent = parent

        self.parent.addLayout(self)  