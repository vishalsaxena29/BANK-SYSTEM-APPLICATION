import sqlite3
from tkinter import *
from Login_window2 import Ui_LOGIN_Window
from tkinter import messagebox,scrolledtext
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
dbb = sqlite3.connect('BANKVS.db')
c = dbb.cursor()


class Ui_Signup_window(object):

    def MessagesProfile(self, title, message):
        mssg = QMessageBox()
        mssg.setWindowTitle(title)
        mssg.setIcon(QMessageBox.Warning)
        mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mssg.setText(message)
        mssg.buttonClicked.connect(self.buttonClickeed)
        mssg.exec_()

    def buttonClickeed(self, me):
        if me.text() == QMessageBox.Ok:
            print('quite')
            quit()

    def Logout(self):
        self.MessagesProfile('Quit', 'Will you like to quit?')
        quit()

    def setupUi(self, Signup_window):
        Signup_window.setObjectName("Signup_window")
        Signup_window.resize(520, 665)
        Signup_window.setStyleSheet("QDialog{background-color:qlineargradient(spread:pad, x1:0.438222, y1:0.0743182, x2:0.418961, y2:1, stop:0.413793 rgba(59, 136, 89, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.user_name_label = QtWidgets.QLabel(Signup_window)
        self.user_name_label.setGeometry(QtCore.QRect(90, 130, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.user_name_label.setFont(font)
        self.user_name_label.setObjectName("user_name_label")
        self.last_name_label = QtWidgets.QLabel(Signup_window)
        self.last_name_label.setGeometry(QtCore.QRect(90, 210, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.last_name_label.setFont(font)
        self.last_name_label.setObjectName("last_name_label")
        self.name_label = QtWidgets.QLabel(Signup_window)
        self.name_label.setGeometry(QtCore.QRect(90, 170, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.title_label = QtWidgets.QLabel(Signup_window)
        self.title_label.setGeometry(QtCore.QRect(20, 40, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title_label.setObjectName("title_label")
        self.username_col_lineedit = QtWidgets.QLineEdit(Signup_window)
        self.username_col_lineedit.setGeometry(QtCore.QRect(290, 130, 113, 21))
        self.username_col_lineedit.setObjectName("username_col_lineedit")
        self.Name_lineEdit_2 = QtWidgets.QLineEdit(Signup_window)
        self.Name_lineEdit_2.setGeometry(QtCore.QRect(290, 170, 113, 21))
        self.Name_lineEdit_2.setObjectName("Name_lineEdit_2")
        self.Last_Name_lineEdit_3 = QtWidgets.QLineEdit(Signup_window)
        self.Last_Name_lineEdit_3.setGeometry(QtCore.QRect(290, 210, 113, 21))
        self.Last_Name_lineEdit_3.setObjectName("Last_Name_lineEdit_3")
        self.email_label = QtWidgets.QLabel(Signup_window)
        self.email_label.setGeometry(QtCore.QRect(90, 370, 60, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.Mobile_label = QtWidgets.QLabel(Signup_window)
        self.Mobile_label.setGeometry(QtCore.QRect(90, 330, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Mobile_label.setFont(font)
        self.Mobile_label.setObjectName("Mobile_label")
        self.age_label = QtWidgets.QLabel(Signup_window)
        self.age_label.setGeometry(QtCore.QRect(90, 250, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.age_label.setFont(font)
        self.age_label.setObjectName("age_label")
        self.pass_label = QtWidgets.QLabel(Signup_window)
        self.pass_label.setGeometry(QtCore.QRect(90, 450, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.confirm_pass_label = QtWidgets.QLabel(Signup_window)
        self.confirm_pass_label.setGeometry(QtCore.QRect(90, 490, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.confirm_pass_label.setFont(font)
        self.confirm_pass_label.setObjectName("confirm_pass_label")
        self.Age_lineEdit_4 = QtWidgets.QLineEdit(Signup_window)
        self.Age_lineEdit_4.setGeometry(QtCore.QRect(290, 250, 113, 21))
        self.Age_lineEdit_4.setObjectName("Age_lineEdit_4")
        self.age_lineEdit_5 = QtWidgets.QLineEdit(Signup_window)
        self.age_lineEdit_5.setGeometry(QtCore.QRect(290, 290, 113, 21))
        self.age_lineEdit_5.setObjectName("age_lineEdit_5")
        self.mobile_lineEdit_6 = QtWidgets.QLineEdit(Signup_window)
        self.mobile_lineEdit_6.setGeometry(QtCore.QRect(290, 330, 113, 21))
        self.mobile_lineEdit_6.setObjectName("mobile_lineEdit_6")
        self.Email_lineEdit_7 = QtWidgets.QLineEdit(Signup_window)
        self.Email_lineEdit_7.setGeometry(QtCore.QRect(290, 370, 113, 21))
        self.Email_lineEdit_7.setObjectName("Email_lineEdit_7")
        self.Address_lineEdit_8 = QtWidgets.QLineEdit(Signup_window)
        self.Address_lineEdit_8.setGeometry(QtCore.QRect(290, 410, 113, 21))
        self.Address_lineEdit_8.setObjectName("Address_lineEdit_8")
        self.Gender_label = QtWidgets.QLabel(Signup_window)
        self.Gender_label.setGeometry(QtCore.QRect(90, 290, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Gender_label.setFont(font)
        self.Gender_label.setObjectName("Gender_label")
        self.Password_lineEdit_9 = QtWidgets.QLineEdit(Signup_window)
        self.Password_lineEdit_9.setGeometry(QtCore.QRect(290, 450, 113, 21))
        self.Password_lineEdit_9.setObjectName("Password_lineEdit_9")
        self.Password_lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.address_label = QtWidgets.QLabel(Signup_window)
        self.address_label.setGeometry(QtCore.QRect(90, 410, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")
        self.Confirm_pass_lineEdit_10 = QtWidgets.QLineEdit(Signup_window)
        self.Confirm_pass_lineEdit_10.setGeometry(QtCore.QRect(290, 490, 113, 21))
        self.Confirm_pass_lineEdit_10.setObjectName("Confirm_pass_lineEdit_10")
        self.Confirm_pass_lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signup_pushButton = QtWidgets.QPushButton(Signup_window)
        self.signup_pushButton.setGeometry(QtCore.QRect(140, 550, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.signup_pushButton.setFont(font)
        self.signup_pushButton.setObjectName("signup_pushButton")
        self.signup_pushButton.clicked.connect(self.CreateDB)

        self.EXIT_button = QtWidgets.QPushButton(Signup_window)
        self.EXIT_button.setGeometry(QtCore.QRect(210, 590, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.EXIT_button.setFont(font)
        self.EXIT_button.setObjectName("EXIT_button")
        self.EXIT_button.clicked.connect(self.Logout)
        self.pushButton = QtWidgets.QPushButton(Signup_window)
        self.pushButton.setGeometry(QtCore.QRect(280, 550, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Signup_window)
        QtCore.QMetaObject.connectSlotsByName(Signup_window)

    def CreateDB(self):
            c.execute(''' CREATE TABLE IF NOT EXISTS BANK4U(
                USERNAME CHAR(20) PRIMARY KEY NOT NULL,
                NAME STR NOT NULL,
                LASTNAME STR NOT NULL,
                AGE INTEGER NOT NULL,
                GENDER STR NOT NULL,
                MOBILE_NUMBER CHAR(11) NOT NULL,
                EMAIL STR NOT NULL,
                ADDRESS CHAR(50) NOT NULL,
                PASSWORD STR NOT NULL,
                CONFIRM STR NOT NULL);
                ''')
            self.insertdb()

    def insertdb(self):
        username = self.username_col_lineedit.text()
        firstname = self.Name_lineEdit_2.text()
        lastname = self.Last_Name_lineEdit_3.text()
        email = self.Email_lineEdit_7.text()
        if '@' not in email:
            self.general_message('Invalid Email', 'Please Check your Email again')
            return email
        else:
            password = self.Password_lineEdit_9.text()
            confirmPass = self.Confirm_pass_lineEdit_10.text()
            if password != confirmPass:
                self.general_message('password Error', 'Password Not Match')
                return password and confirmPass
            elif len(password) != len(confirmPass):
                self.general_message('password Error', 'password not Match')
                return password and confirmPass
            else:
                phone = self.mobile_lineEdit_6.text()
                if len(phone) != 11:
                    self.general_message('Invalid Number', 'please Check your Phone number')
                    return phone
                else:
                    sex = self.age_lineEdit_5.text()
                    age = self.Age_lineEdit_4.text()
                    address = self.Address_lineEdit_8.text()
                    c.execute(
                        "INSERT INTO BANK4U(USERNAME, NAME, LASTNAME, AGE, GENDER, MOBILE_NUMBER, EMAIL, ADDRESS, PASSWORD, CONFIRM)VALUES (?,?,?,?,?,?,?,?,?,?)",
                        (str(username), str(firstname), str(lastname), str(age), str(sex), str(phone),
                         str(email), str(address), str(password), str(confirmPass)))
                    print('insert done')
                    dbb.commit()
                    dbb.close()
                    self.login()

    def login(self):
        self.LoginWindow = QtWidgets.QDialog()
        self.ui = Ui_LOGIN_Window()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()

    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()

    def retranslateUi(self, Signup_window):
        _translate = QtCore.QCoreApplication.translate
        Signup_window.setWindowTitle(_translate("Signup_window", "Signup_window"))
        self.user_name_label.setText(_translate("Signup_window", "USER NAME"))
        self.last_name_label.setText(_translate("Signup_window", "LAST NAME"))
        self.name_label.setText(_translate("Signup_window", "NAME"))
        self.title_label.setText(_translate("Signup_window", "BANK APPLICATION SIGN UP FORM"))
        self.email_label.setText(_translate("Signup_window", "EMAIL ID"))
        self.Mobile_label.setText(_translate("Signup_window", "MOBILE NUMBER"))
        self.age_label.setText(_translate("Signup_window", "AGE"))
        self.pass_label.setText(_translate("Signup_window", "PASSWORD"))
        self.confirm_pass_label.setText(_translate("Signup_window", "CONFIRM PASSWORD"))
        self.Gender_label.setText(_translate("Signup_window", "GENDER"))
        self.address_label.setText(_translate("Signup_window", "PERMANENT ADDRESS "))
        self.signup_pushButton.setText(_translate("Signup_window", "Signup"))
        self.EXIT_button.setText(_translate("Signup_window", "Exit"))
        self.pushButton.setText(_translate("Signup_window", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signup_window = QtWidgets.QDialog()
    ui = Ui_Signup_window()
    ui.setupUi(Signup_window)
    Signup_window.show()
    sys.exit(app.exec_())
