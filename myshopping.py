from re import A
import sys
import os

from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

cartItems = []
itemPrices = {'Cappucino': 20000,
              'Americano': 50000,
              'Machiato': 60000,
              'Caramel Latte': 70000,
              'Espresso': 70000,
              'MocchaChino': 50000}
cartTotal = 0


class Form(QObject):
    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)

        # load form uifile
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        cmBoxItem = self.window.findChild(QComboBox, 'cmBoxItem')
        btnAdd = self.window.findChild(QPushButton, 'btnAdd')

        cmBoxItem.addItem("Cappucino")
        cmBoxItem.addItem("Americano")
        cmBoxItem.addItem("Machiato")
        cmBoxItem.addItem("Caramel Latte")
        cmBoxItem.addItem("Espresso")
        cmBoxItem.addItem("MocchaChino")

        # mebuat klik add cart bekerja
        btnAdd.clicked.connect(self.updateCart)

        self.window.show()

    def addItem(self, item):
        # add item to di combo Box ke list dan view
        cmBoxItem = self.window.findChild(QComboBox, 'cmBoxItem')
        lstView = self.window.findChild(QListWidget, 'lstView')

        lstView.addItem(cmBoxItem.currentText())
        cartItems.append(item)

    def updateCart(self):
        global cartItems, itemPrice, cartTotal
        cmBoxItem = self.window.findChild(QComboBox, 'cmBoxItem')
        lblList = self.window.findChild(QLabel, 'lblList')
        lblTotal2 = self.window.findChild(QLabel, 'lblTotal2')

        # fungsi add item
        self.addItem(cmBoxItem.currentText())

        cartSummary = dict((item, cartItems.count(item))for item in cartItems)
        lblList.setText(str(cartSummary))

        for item in cartItems:
            itemPrice = itemPrices.get(item, 0)
            cartTotal += itemPrice
        lblTotal2.setText(str(cartTotal))
        cartTotal = 0

        # update status setelah di add


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # load ui\
    form = Form('cart.ui')
    sys.exit(app.exec_())
