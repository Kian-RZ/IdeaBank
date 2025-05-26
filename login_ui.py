from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import resources

class Ui_Dialog(object):

    def login_proc(self):
        password = self.lineEdit.text()
        if str(password) == "1390":
            self.dialog.accept()

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(429, 377)
        Dialog.setFixedSize(429, 377)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../qrc_res/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 30, 431, 71))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 431, 71))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(120, 120, 120);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 140, 431, 71))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 162, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 210, 301, 51))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:5px;\n"
"border: 1px solid rgb(195, 195, 195);\n"
"padding-right:10px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(70, 270, 301, 51))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color: rgb(255, 162, 0);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.login.setObjectName("login")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connections 
        self.login.clicked.connect(self.login_proc)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "بانک ایده - ورود"))
        self.label.setText(_translate("Dialog", "نرم افزار بانک ایده"))
        self.label_2.setText(_translate("Dialog", "ورود"))
        self.label_3.setText(_translate("Dialog", "کیان رضایی"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "رمز عبور"))
        self.login.setText(_translate("Dialog", "ورود"))

class LoginDialog(QDialog):
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
