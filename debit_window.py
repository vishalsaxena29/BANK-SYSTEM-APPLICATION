# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debit_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Debit(object):
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
        self.MessagesProfile('Quit', 'Will you like to Cancel?')
        quit()

    def WithdrawalCancle(self):
        from services import Ui_BANK_SERVICES
        print('WithdrawalCancle')
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_BANK_SERVICES()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, Debit):
        Debit.setObjectName("Debit")
        Debit.resize(427, 337)
        Debit.setStyleSheet("QDialog{background-color:qlineargradient(spread:pad, x1:0.438222, y1:0.0743182, x2:0.418961, y2:1, stop:0.413793 rgba(59, 136, 89, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.debit_label = QtWidgets.QLabel(Debit)
        self.debit_label.setGeometry(QtCore.QRect(50, 130, 171, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.debit_label.setFont(font)
        self.debit_label.setObjectName("debit_label")
        self.debit_amt_label_2 = QtWidgets.QLabel(Debit)
        self.debit_amt_label_2.setGeometry(QtCore.QRect(50, 180, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.debit_amt_label_2.setFont(font)
        self.debit_amt_label_2.setObjectName("debit_amt_label_2")
        self.submit_pushButton = QtWidgets.QPushButton(Debit)
        self.submit_pushButton.setGeometry(QtCore.QRect(70, 240, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.submit_pushButton.setFont(font)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.submit_pushButton.clicked.connect(self.update_balance)

        self.Cancel_pushButton_2 = QtWidgets.QPushButton(Debit)
        self.Cancel_pushButton_2.setGeometry(QtCore.QRect(260, 240, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_pushButton_2.setFont(font)
        self.Cancel_pushButton_2.setObjectName("Cancel_pushButton_2")
        self.Cancel_pushButton_2.clicked.connect(self.WithdrawalCancle)
        self.debit_lineEdit_2 = QtWidgets.QLineEdit(Debit)
        self.debit_lineEdit_2.setGeometry(QtCore.QRect(260, 140, 113, 21))
        self.debit_lineEdit_2.setObjectName("debit_lineEdit_2")
        self.debit_amt_lineEdit_3 = QtWidgets.QLineEdit(Debit)
        self.debit_amt_lineEdit_3.setGeometry(QtCore.QRect(260, 180, 113, 21))
        self.debit_amt_lineEdit_3.setObjectName("debit_amt_lineEdit_3")
        self.Title = QtWidgets.QLabel(Debit)
        self.Title.setGeometry(QtCore.QRect(20, 10, 391, 91))
        font = QtGui.QFont()
        font.setPointSize(37)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.retranslateUi(Debit)
        QtCore.QMetaObject.connectSlotsByName(Debit)

    def update_balance(self):
        if self.debit_lineEdit_2.text():
            try:
                amnt = float(self.debit_lineEdit_2.get())
                dbb = sqlite3.connect('BANKVS.db')
                c = dbb.cursor()
                Debitor_Name = self.debit_lineEdit_2.text()
                Amount = self.debit_amt_lineEdit_3.text()
                c.execute("select AMOUNT from DEPOSIT where Depositor_name=?",([(Debitor_Name)]))
                bal = c.fetchone()
                if bal:
                    if amnt <= bal:

                        cmd = ("update DEPOSIT SET AMOUNT=AMOUNT-? where name=?",([(Amount), (Debitor_Name)]))
                        c.execute(cmd)
                        dbb.commit()
                        c.close()
                        dbb.close()
                        s = '!!DEBITED SUCESSFULLY!! \n ? rs debited from Your Account\nYour Updated Balance is now ?.'.format(
                            amnt, bal - amnt)
                        messagebox.showinfo("!!Sucess!!", s)


                    else:

                        s = '\nInsufficient account balance\nyou only have {}rs in your account'.format(bal)
                        messagebox.showinfo("!!DEBIT ERROR!!", s)


                else:
                    messagebox.showerror("!!UNKOWN ERROR!!", "DATABASE LOOKUP Error \nSomething WEnt Wrong")
            except ValueError as e:
                messagebox.showerror("!!Value Error!!", "!!ERROR!!Enter Vaid Amount to Debit\n")

            except Exception as error:
                messagebox.showerror("!!DataBase Connectivity Error!!", "!!ERROR!!{}".format(error))

        else:
            messagebox.showerror("!!Input Error!!", "Please Enter Amount to Debit")



    def retranslateUi(self, Debit):
        _translate = QtCore.QCoreApplication.translate
        Debit.setWindowTitle(_translate("Debit", "DEBIT WINDOW"))
        self.debit_label.setText(_translate("Debit", "DEBIT ACCOUNT NUMBER"))
        self.debit_amt_label_2.setText(_translate("Debit", "DEBIT AMOUNT"))
        self.submit_pushButton.setText(_translate("Debit", "SUBMITT"))
        self.Cancel_pushButton_2.setText(_translate("Debit", "CANCEL"))
        self.Title.setText(_translate("Debit", "BANK DEBIT WINDOW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Debit = QtWidgets.QDialog()
    ui = Ui_Debit()
    ui.setupUi(Debit)
    Debit.show()
    sys.exit(app.exec_())
