from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QWidget, 
    QScrollArea, 
    QMenu,
    QHBoxLayout,
    QVBoxLayout,
    QFileDialog
    )
from PySide6.QtWebEngineWidgets import QWebEngineView
import textparser
import htmlCrafting
import os

basedir = os.path.dirname(__file__)

class SideMenu(QWidget):
    def __init__(self, textwindow):
        super().__init__()
        self.textwindow = textwindow

        openButton = QPushButton("Open File")
        openButton.clicked.connect(self.openFileAndSetText)

        layout = QVBoxLayout()
        layout.addWidget(openButton)

        self.setLayout(layout)

    def openFileAndSetText(self):
        self.textwindow.openFileAndSetText()


class TextWindow(QWebEngineView):
        def __init__(self, morphemelist=""):
            super().__init__()

        def openFileAndSetText(self):
            filter = "Text Files (*.txt);; All Files (*)"
            filename, selected_filter = QFileDialog.getOpenFileName(self, filter=filter)

            with open(filename, "r", encoding="utf-8") as f:
                lines = f.read()

            morphemelist = textparser.roughTokenize(lines)
            htmlCrafting.craftHTML(morphemelist)
            self.setUrl(QUrl(QUrl.fromLocalFile(basedir + "/index.html")))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        hlayout = QHBoxLayout()

        textwindow = TextWindow()
        sidemenu = SideMenu(textwindow)

        hlayout.addWidget(textwindow, 80)
        hlayout.addWidget(sidemenu, 20)

        widget = QWidget()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)


app = QApplication([])

mainwindow = MainWindow()
mainwindow.show()

app.exec()
