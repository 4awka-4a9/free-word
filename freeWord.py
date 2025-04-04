from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
from PyQt5.Qt import *

import sys

class DonateWindow(QtWidgets.QDialog):


    def __init__(self, parent=None):
        super(DonateWindow, self).__init__(parent)

        self.setWindowTitle("Донат")
        self.setGeometry(300, 250, 300, 300)

        self.BTCtext = QLabel(self)
        self.BTCtext.setGeometry(10, 25, 100, 20)
        self.BTCtext.setText("BTC:")

        self.ETHtext = QLabel(self)
        self.ETHtext.setGeometry(10, 75, 100, 20)
        self.ETHtext.setText("ETH:")

        self.USDTTtext = QLabel(self)
        self.USDTTtext.setGeometry(10, 125, 100, 20)
        self.USDTTtext.setText("USDT TRC 20:")

        self.USDTEtext = QLabel(self)
        self.USDTEtext.setGeometry(10, 175, 100, 20)
        self.USDTEtext.setText("USDT ERC 20:")

        self.BTCcopy = QLineEdit(self)
        self.BTCcopy.setGeometry(10, 50, 270, 20)
        self.BTCcopy.setText("bc1qml9r2f7qud0zsatjf3kh4c6v9yetd8zer52t97")
        self.BTCcopy.setReadOnly(True)

        self.ETHcopy = QLineEdit(self)
        self.ETHcopy.setGeometry(10, 100, 270, 20)
        self.ETHcopy.setText("0xc3006CD922641337053BfB34a919299754002Fa6")
        self.ETHcopy.setReadOnly(True)

        self.USDTTcopy = QLineEdit(self)
        self.USDTTcopy.setGeometry(10, 150, 270, 20)
        self.USDTTcopy.setText("TJ1Zc5Y2SsNLMaQKzdy9XFT5iLAZHx7zGZ")
        self.USDTTcopy.setReadOnly(True)

        self.USDTEcopy = QLineEdit(self)
        self.USDTEcopy.setGeometry(10, 200, 270, 20)
        self.USDTEcopy.setText("0xc3006CD922641337053BfB34a919299754002Fa6")
        self.USDTEcopy.setReadOnly(True)

        self.githubLink = QLabel(self)
        self.githubLink.setGeometry(125, 250, 40, 20)
        self.githubLink.setText("<a href=\"https://github.com/4awka-4a9/weather.git\">github</a>")
        self.githubLink.setOpenExternalLinks(True)


class Window(QMainWindow):


    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("ворд но бюджет 2 копейки")
        self.setGeometry(300, 250, 350, 200)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        self.create_menu_bar()

    def create_menu_bar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction("Открыть", self.action_clicked)
        fileMenu.addAction("Сохранить", self.action_clicked)

        donateMenu = QMenu("&Донат", self)
        self.menuBar.addMenu(donateMenu)

        donateMenu.addAction("Донат", self.action_clicked)

    def show_donate_bar(self):
        pass
        self.donate = DonateWindow()
        self.donate.exec_()

    @QtCore.pyqtSlot()

    def action_clicked(self):
            action = self.sender()

            if action.text() == "Открыть":
                fname = QFileDialog.getOpenFileName(self)[0]

                try:
                    f = open(fname, "r")
                    with f:
                        data = f.read()
                        self.textEdit.setText(data)
                    f.close()

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

            if action.text() == "Донат":
                self.show_donate_bar()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
