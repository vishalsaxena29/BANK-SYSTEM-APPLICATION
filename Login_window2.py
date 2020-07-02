from tkinter import *
import tkinter.messagebox
from services import Ui_BANK_SERVICES
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LOGIN_Window(object):

    def reg(self):
        from Signup_Window3 import Ui_Signup_window
        self.general_message('Back', 'Would you like to Register First?')
        self.registrationPage = QtWidgets.QDialog()
        self.ui = Ui_Signup_window()
        self.ui.setupUi(self.registrationPage)
        self.registrationPage.show()

    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()

    def profile(self):
        self.Window = QtWidgets.QDialog()
        self.ui = Ui_BANK_SERVICES()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def loginLogin(self):
            import sqlite3
            dbb = sqlite3.connect('BANKVS.db')
            cur = dbb.cursor()
            username = self.user_lineEdit.text()
            password = self.pass_lineEdit_3.text()

            cur.execute("SELECT * FROM BANK4U WHERE USERNAME = ? AND PASSWORD = ?", ([(username), (password)]))
            result = cur.fetchall()

            if result:
                self.profile()
            else:
                self.general_message('User Error', 'User does not Exist')

    def setupUi(self, LOGIN_Window):
        LOGIN_Window.setObjectName("LOGIN_Window")
        LOGIN_Window.resize(539, 418)
        LOGIN_Window.setStyleSheet("QDialog{background-color:qlineargradient(spread:pad, x1:0.438222, y1:0.0743182, x2:0.418961, y2:1, stop:0.413793 rgba(59, 136, 89, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.user_label = QtWidgets.QLabel(LOGIN_Window)
        self.user_label.setGeometry(QtCore.QRect(110, 130, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.pass_label_2 = QtWidgets.QLabel(LOGIN_Window)
        self.pass_label_2.setGeometry(QtCore.QRect(110, 200, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pass_label_2.setFont(font)
        self.pass_label_2.setObjectName("pass_label_2")
        self.user_lineEdit = QtWidgets.QLineEdit(LOGIN_Window)
        self.user_lineEdit.setGeometry(QtCore.QRect(300, 140, 141, 31))
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.pass_lineEdit_3 = QtWidgets.QLineEdit(LOGIN_Window)
        self.pass_lineEdit_3.setGeometry(QtCore.QRect(300, 200, 141, 31))
        self.pass_lineEdit_3.setObjectName("pass_lineEdit_3")
        self.pass_lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(LOGIN_Window)
        self.label.setGeometry(QtCore.QRect(30, 40, 491, 81))
        font = QtGui.QFont()
        font.setPointSize(29)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.login_pushButton = QtWidgets.QPushButton(LOGIN_Window)
        self.login_pushButton.setGeometry(QtCore.QRect(120, 280, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setObjectName("login_pushButton")
        self.login_pushButton.clicked.connect(self.loginLogin)

        self.signup_pushButton_2 = QtWidgets.QPushButton(LOGIN_Window)
        self.signup_pushButton_2.setGeometry(QtCore.QRect(300, 280, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.signup_pushButton_2.setFont(font)
        self.signup_pushButton_2.setObjectName("signup_pushButton_2")
        self.signup_pushButton_2.clicked.connect(self.reg)
        self.retranslateUi(LOGIN_Window)
        QtCore.QMetaObject.connectSlotsByName(LOGIN_Window)

    def retranslateUi(self, LOGIN_Window):
        _translate = QtCore.QCoreApplication.translate
        LOGIN_Window.setWindowTitle(_translate("LOGIN_Window", "LOGIN WINDOW"))
        self.user_label.setText(_translate("LOGIN_Window", "USER NAME"))
        self.pass_label_2.setText(_translate("LOGIN_Window", "PASSWORD"))
        self.label.setText(_translate("LOGIN_Window", "BANK APPLICATION LOGIN FORM"))
        self.login_pushButton.setText(_translate("LOGIN_Window", "LOGIN"))
        self.signup_pushButton_2.setText(_translate("LOGIN_Window", "SIGN UP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGIN_Window = QtWidgets.QDialog()
    ui = Ui_LOGIN_Window()
    ui.setupUi(LOGIN_Window)
    LOGIN_Window.show()
    sys.exit(app.exec_())
