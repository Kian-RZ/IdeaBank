from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from database import get_idea_by_id
import resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(564, 605)
        Dialog.setFixedSize(564, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        self.title.setReadOnly(True)
        self.title.setObjectName("title")
        self.description = QtWidgets.QPlainTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(30, 150, 501, 421))
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
        self.description.setReadOnly(True)
        self.description.setPlainText("")
        self.description.setBackgroundVisible(False)
        self.description.setPlaceholderText("")
        self.description.setObjectName("description")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "بانک ایده - مشاهده"))
        self.label.setText(_translate("Dialog", "مشاهده ایده"))
        self.title.setPlaceholderText(_translate("Dialog", "عنوان ایده"))

class SeeDialog(QDialog):
    def __init__(self, id, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        idea = get_idea_by_id(id)
        self.ui.title.setText(idea["title"])
        self.ui.description.setPlainText(idea["description"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
