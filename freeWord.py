from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys



class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("ворд но бюджет 2 копейки")
        self.setGeometry(300, 250, 350, 200)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction("Открыть", self.actionClicked)
        fileMenu.addAction("Сохранить", self.actionClicked)

    @QtCore.pyqtSlot()
    def actionClicked(self):
            action = self.sender()
            if action.text() == "Открыть":
                fname = QFileDialog.getOpenFileName(self)[0]
                try:
                    f = open(fname, "r")
                    with f:
                        data = f.read()
                        self.textEdit.setText(data)
                    f.close( )
                except FileNotFoundError:
                    print("no such file ")

            elif action.text() == "Сохранить":
                fname = QFileDialog.getSaveFileName(self)[0]
                try:
                    f = open(fname, "w")
                    text = self.textEdit.toPlainText()
                    f.write(text)
                    f.close()
                except FileNotFoundError:
                    print("no such file ")

def  application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
