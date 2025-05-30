from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from database import insert_idea

class Ui_Dialog(object):
    def add_idea(self):
        title = self.title.text()
        description = self.description.toPlainText()
        if title != None or title != '' or title != ' ':
            if description != None or description != '' or description != ' ':
                insert_idea(title,description)
                self.dialog.accept()
            else:
                insert_idea(title,None)
                self.dialog.accept()

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(564, 605)
        Dialog.setFixedSize(564, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.title = QtWidgets.QLineEdit(Dialog)
        self.title.setGeometry(QtCore.QRect(32, 80, 501, 61))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("border-radius:5px;\n"
"border: 1px solid rgb(195, 195, 195);\n"
"padding-right:10px;")
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(30, 510, 501, 61))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setStyleSheet("background-color: rgb(255, 162, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon1)
        self.add.setIconSize(QtCore.QSize(20, 20))
        self.add.setObjectName("add")
        self.description = QtWidgets.QPlainTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(30, 150, 501, 351))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.description.setFont(font)
        self.description.setStyleSheet("border-radius:5px;\n"
"border: 1px solid rgb(195, 195, 195);\n"
"padding-right:10px;")
        self.description.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.description.setPlainText("")
        self.description.setBackgroundVisible(False)
        self.description.setPlaceholderText("")
        self.description.setObjectName("description")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connections
        self.add.clicked.connect(self.add_idea)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "بانک ایده - افزودن"))
        self.title.setPlaceholderText(_translate("Dialog", "عنوان ایده"))
        self.label.setText(_translate("Dialog", "افزودن ایده"))
        self.add.setText(_translate("Dialog", "افزودن"))
import resources

class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
