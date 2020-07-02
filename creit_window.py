import sqlite3
from tkinter import messagebox
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

dbb = sqlite3.connect('BANKVS.db')
c = dbb.cursor()


class Ui_CREDIT_WINDOW(object):

    def CreateNEWDB(self):
            c.execute(''' CREATE TABLE IF NOT EXISTS DEPOSIT(
                Depositor_name CHAR(20) NOT NULL,
                AMOUNT INTEGER NOT NULL);
                ''')

            self.insertdb()

    def insertdb(self):
        Depositor_name = self.Credit_accnt_lineEdit_2.text()
        AMOUNT = self.Credit_amt_lineEdit_3.text()
        c.execute("INSERT INTO DEPOSIT(Depositor_name, AMOUNT)VALUES (?,?)",
        (str(Depositor_name), str(AMOUNT)))
        print('insert done')
        dbb.commit()
        self.credit()


    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()


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


    def setupUi(self, CREDIT_WINDOW):
        CREDIT_WINDOW.setObjectName("CREDIT_WINDOW")
        CREDIT_WINDOW.resize(432, 339)
        CREDIT_WINDOW.setStyleSheet("QDialog{background-color:qlineargradient(spread:pad, x1:0.438222, y1:0.0743182, x2:0.418961, y2:1, stop:0.413793 rgba(59, 136, 89, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.Title = QtWidgets.QLabel(CREDIT_WINDOW)
        self.Title.setGeometry(QtCore.QRect(20, 10, 391, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Credit_accnt_label = QtWidgets.QLabel(CREDIT_WINDOW)
        self.Credit_accnt_label.setGeometry(QtCore.QRect(50, 120, 181, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Credit_accnt_label.setFont(font)
        self.Credit_accnt_label.setObjectName("Credit_accnt_label")
        self.Credit_amt_label_2 = QtWidgets.QLabel(CREDIT_WINDOW)
        self.Credit_amt_label_2.setGeometry(QtCore.QRect(50, 180, 171, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Credit_amt_label_2.setFont(font)
        self.Credit_amt_label_2.setObjectName("Credit_amt_label_2")
        self.Credit_accnt_lineEdit_2 = QtWidgets.QLineEdit(CREDIT_WINDOW)
        self.Credit_accnt_lineEdit_2.setGeometry(QtCore.QRect(280, 130, 113, 21))
        self.Credit_accnt_lineEdit_2.setObjectName("Credit_accnt_lineEdit_2")
        self.Credit_amt_lineEdit_3 = QtWidgets.QLineEdit(CREDIT_WINDOW)
        self.Credit_amt_lineEdit_3.setGeometry(QtCore.QRect(280, 190, 113, 21))
        self.Credit_amt_lineEdit_3.setObjectName("Credit_amt_lineEdit_3")
        self.Submit_pushButton = QtWidgets.QPushButton(CREDIT_WINDOW)
        self.Submit_pushButton.setGeometry(QtCore.QRect(80, 240, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Submit_pushButton.setFont(font)
        self.Submit_pushButton.setObjectName("Submit_pushButton")
        self.Submit_pushButton.clicked.connect(self.insertdb)
        self.Cancel_pushButton_2 = QtWidgets.QPushButton(CREDIT_WINDOW)
        self.Cancel_pushButton_2.setGeometry(QtCore.QRect(250, 240, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_pushButton_2.setFont(font)
        self.Cancel_pushButton_2.setObjectName("Cancel_pushButton_2")
        self.Cancel_pushButton_2.clicked.connect(self.WithdrawalCancle)

        #self.main_menu_pushButton_3.clicked.connect(self.Mainmenu)

        self.retranslateUi(CREDIT_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(CREDIT_WINDOW)



    def credit(self):
            try:
                import sqlite3
                dbb = sqlite3.connect('BANKVS.db')
                cur = dbb.cursor()
                Depositor_Name = self.Credit_accnt_lineEdit_2.text()
                Amount  = self.Credit_amt_lineEdit_3.text()
                cur.execute("select AMOUNT from DEPOSIT where Depositor_name= ?",([(Depositor_Name)]))
                bal = cur.fetchone()
                cmd = ("update DEPOSIT SET AMOUNT=AMOUNT+? where Depositor_name= ?",([(Amount), (Depositor_Name)]))
                c.execute(cmd)
                dbb.commit()
                print("CREDIT DONE!!")
                s = ("Sucessfully credited to the account.\nYour Updated Balance is now ?.",([(Depositor_Name)])+bal)
                messagebox.showinfo("CREDIT", s)
            except ValueError as e:
                messagebox.showerror("!!Input Error!!", "Please Enter a Valid Amount")
            else:
                messagebox.showerror("!!Input Error!!", "Please Enter Some Amount to Credit")


    def WithdrawalCancle(self):
        from services import Ui_BANK_SERVICES
        print('WithdrawalCancle')
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_BANK_SERVICES()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


    def retranslateUi(self, CREDIT_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        CREDIT_WINDOW.setWindowTitle(_translate("CREDIT_WINDOW", "CREDIT WINDOW"))
        self.Title.setText(_translate("CREDIT_WINDOW", "BANK CREDIT WINDOW"))
        self.Credit_accnt_label.setText(_translate("CREDIT_WINDOW", "CREDIT ACCOUNT NUMBER"))
        self.Credit_amt_label_2.setText(_translate("CREDIT_WINDOW", "CREDIT AMOUNT"))
        self.Submit_pushButton.setText(_translate("CREDIT_WINDOW", "SUBMIT"))
        self.Cancel_pushButton_2.setText(_translate("CREDIT_WINDOW", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CREDIT_WINDOW = QtWidgets.QDialog()
    ui = Ui_CREDIT_WINDOW()
    ui.setupUi(CREDIT_WINDOW)
    CREDIT_WINDOW.show()
    sys.exit(app.exec_())
