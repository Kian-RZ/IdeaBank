from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from usermanager import register_new_user
import resources

class Ui_Dialog(object):
    
    def signup_proc(self):
        username = str(self.username.text())
        password = str(self.password.text())
        register_new_user(username,password)
        self.dialog.accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(429, 377)
        self.dialog = Dialog
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../qrc_res/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(70, 210, 301, 51))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("border-radius:5px;\n"
"border: 1px solid rgb(195, 195, 195);\n"
"padding-right:10px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.signup = QtWidgets.QPushButton(Dialog)
        self.signup.setGeometry(QtCore.QRect(70, 270, 301, 51))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setStyleSheet("background-color: rgb(255, 162, 0);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.signup.setObjectName("signup")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(70, 150, 301, 51))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet("border-radius:5px;\n"
"border: 1px solid rgb(195, 195, 195);\n"
"padding-right:10px;")
        self.username.setObjectName("username")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connections
        self.signup.clicked.connect(self.signup_proc)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "بانک ایده - ثبت نام"))
        self.label.setText(_translate("Dialog", "نرم افزار بانک ایده"))
        self.label_2.setText(_translate("Dialog", "ثبت نام"))
        self.password.setPlaceholderText(_translate("Dialog", "رمز عبور"))
        self.signup.setText(_translate("Dialog", "ثبت نام"))
        self.username.setPlaceholderText(_translate("Dialog", "نام کاربری"))

class SignupDialog(QDialog):
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
