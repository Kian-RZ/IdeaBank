from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QLabel, QVBoxLayout
from see_ui import SeeDialog
from add_ui import AddDialog
from login_ui import LoginDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from database import run_database, get_idea_by_id, get_all_ideas, delete_idea

run_database()

class CustomItem(QWidget):
    def __init__(self, text, icon_path, id):
        super().__init__()

        icon_label = QLabel()
        pixmap = QPixmap(icon_path).scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(pixmap)
        self.id = id

        text_label = QLabel(text)
        font = QFont("YEKAN PLUS", 14, QFont.Bold)
        text_label.setFont(font)

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(icon_label)
        layout.addWidget(text_label)
        layout.addStretch()
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)

    def get_id(self):
        return self.id


class Ui_MainWindow(object):
    
    def delete_idea(self):
        try:
            current_row = self.list.currentRow()
            item = self.list.item(current_row)
            widget = self.list.itemWidget(item)

            id = widget.get_id()
            delete_idea(id)
        except:
            pass

        self.load_ideas_into_list()
        
    def open_dialog_see(self):
        try:
            current_row = self.list.currentRow()
            item = self.list.item(current_row)
            widget = self.list.itemWidget(item)

            id = widget.get_id()
            dialog = SeeDialog(id)
            dialog.exec_()
        except:
            pass


    def open_dialog_add(self):
        dialog = AddDialog()
        result = dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            self.load_ideas_into_list()

    def load_ideas_into_list(self):
        self.list.clear()
        ideas = get_all_ideas()

        for idea_id, title in ideas:
                item = QListWidgetItem()
                custom_widget = CustomItem(title,":images/icon.png",idea_id)
                item.setSizeHint(custom_widget.sizeHint())

                self.list.addItem(item)
                self.list.setItemWidget(item, custom_widget)

    def setupUi(self, MainWindow):
        MainWindow.setWindowOpacity(0)
        dialog = LoginDialog()
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            MainWindow.setWindowOpacity(1)
            self.stat = True
        else:
            self.stat = False

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 760)
        MainWindow.setFixedSize(1051, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 70, 321, 21))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 162, 0);")
        self.label_2.setObjectName("label_2")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(30, 30, 111, 61))
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
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(270, 30, 111, 61))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_2.setIcon(icon2)
        self.delete_2.setIconSize(QtCore.QSize(20, 20))
        self.delete_2.setObjectName("delete_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 720, 861, 20))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1000, 720, 21, 21))
        self.label_4.setStyleSheet("border-image: url(:/images/error.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(30, 110, 991, 591))
        self.list.setStyleSheet("border-radius:5px;\n"
"border: 1px solid rgb(195, 195, 195);")
        self.list.setObjectName("list")

        self.see = QtWidgets.QPushButton(self.centralwidget)
        self.see.setGeometry(QtCore.QRect(150, 30, 111, 61))
        font = QtGui.QFont()
        font.setFamily("YEKAN PLUS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.see.setFont(font)
        self.see.setStyleSheet("background-color: rgb(255, 162, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.see.setIcon(icon3)
        self.see.setIconSize(QtCore.QSize(20, 20))
        self.see.setObjectName("see")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connections 
        self.see.clicked.connect(self.open_dialog_see)
        self.add.clicked.connect(self.open_dialog_add)
        self.delete_2.clicked.connect(self.delete_idea)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "نرم افزار بانک ایده"))
        self.label.setText(_translate("MainWindow", "نرم افزار بانک ایده"))
        self.label_2.setText(_translate("MainWindow", "کیان رضایی"))
        self.add.setText(_translate("MainWindow", "افزودن"))
        self.delete_2.setText(_translate("MainWindow", "حذف"))
        self.label_3.setText(_translate("MainWindow", "ورود افراد غیر متفرقه ممنوع می باشد . لذا اگر بی اجازه وارد شده اید به سرعت خارج شوید . ورود بی اجازه به این نرم افزار و استفاده از متحوای داخل آن پیگرد قانونی دارد"))
        self.see.setText(_translate("MainWindow", "مشاهده"))
import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.load_ideas_into_list()
    if ui.stat == True:
        MainWindow.show()
        sys.exit(app.exec_())
