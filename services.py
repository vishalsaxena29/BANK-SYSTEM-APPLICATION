from PyQt5.QtWidgets import QMessageBox
from creit_window import Ui_CREDIT_WINDOW
from Transfer_window import Ui_TRANSERWINDOW
from Update_window import Ui_Dialog
from debit_window import Ui_Debit
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BANK_SERVICES(object):
    
    def Credit(self):
        self.general_message('Back', 'Would you like to Deposit money?')
        self.creditPage = QtWidgets.QDialog()
        self.ui = Ui_CREDIT_WINDOW()
        self.ui.setupUi(self.creditPage)
        self.creditPage.show()
        
    def Debit(self):
        self.general_message('Back', 'Would you like to Withdraw?')
        self.debitPage = QtWidgets.QDialog()
        self.ui = Ui_Debit()
        self.ui.setupUi(self.debitPage)
        self.debitPage.show()
        
    def Transfer(self):
        self.general_message('Back', 'Would you like to Transfer?')
        self.TransferPage = QtWidgets.QDialog()
        self.ui = Ui_TRANSERWINDOW()
        self.ui.setupUi(self.TransferPage)
        self.TransferPage.show()
    
    def Update(self):
        self.general_message('Back', 'Would you like to Update your account?')
        self.UpdatePage = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.UpdatePage)
        self.UpdatePage.show()

    def general_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Question)
        msg.exec_()

    def Logout(self):
        self.MessagesProfile('Quit', 'Will you like to quit?')
        quit()

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


    def setupUi(self, BANK_SERVICES):
        BANK_SERVICES.setObjectName("BANK_SERVICES")
        BANK_SERVICES.resize(565, 394)
        BANK_SERVICES.setStyleSheet("QDialog{background-color:qlineargradient(spread:pad, x1:0.438222, y1:0.0743182, x2:0.418961, y2:1, stop:0.413793 rgba(59, 136, 89, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.Title = QtWidgets.QLabel(BANK_SERVICES)
        self.Title.setGeometry(QtCore.QRect(50, 20, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(37)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.DEBIT = QtWidgets.QPushButton(BANK_SERVICES)
        self.DEBIT.setGeometry(QtCore.QRect(30, 150, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DEBIT.setFont(font)
        self.DEBIT.setObjectName("DEBIT")
        self.DEBIT.clicked.connect(self.Debit)
        self.CREDIT = QtWidgets.QPushButton(BANK_SERVICES)
        self.CREDIT.setGeometry(QtCore.QRect(170, 150, 113, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CREDIT.setFont(font)
        self.CREDIT.setObjectName("CREDIT")
        self.CREDIT.clicked.connect(self.Credit)
        self.BALANCE = QtWidgets.QPushButton(BANK_SERVICES)
        self.BALANCE.setGeometry(QtCore.QRect(300, 150, 113, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BALANCE.setFont(font)
        self.BALANCE.setObjectName("BALANCE")
        self.PROFILE = QtWidgets.QPushButton(BANK_SERVICES)
        self.PROFILE.setGeometry(QtCore.QRect(430, 150, 113, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PROFILE.setFont(font)
        self.PROFILE.setObjectName("PROFILE")
        self.QUIT = QtWidgets.QPushButton(BANK_SERVICES)
        self.QUIT.setGeometry(QtCore.QRect(220, 300, 113, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.QUIT.setFont(font)
        self.QUIT.setObjectName("QUIT")
        self.QUIT.clicked.connect(self.Logout)
        self.MODIFY = QtWidgets.QPushButton(BANK_SERVICES)
        self.MODIFY.setGeometry(QtCore.QRect(220, 230, 113, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MODIFY.setFont(font)
        self.MODIFY.setObjectName("MODIFY")
        self.DELETE_ACCOUNT = QtWidgets.QPushButton(BANK_SERVICES)
        self.DELETE_ACCOUNT.setGeometry(QtCore.QRect(370, 230, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DELETE_ACCOUNT.setFont(font)
        self.DELETE_ACCOUNT.setObjectName("DELETE_ACCOUNT")
        self.TRANSFER = QtWidgets.QPushButton(BANK_SERVICES)
        self.TRANSFER.setGeometry(QtCore.QRect(80, 230, 113, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TRANSFER.setFont(font)
        self.TRANSFER.setObjectName("TRANSFER")
        self.TRANSFER.clicked.connect(self.Transfer)
        self.Title_2 = QtWidgets.QLabel(BANK_SERVICES)
        self.Title_2.setGeometry(QtCore.QRect(30, 90, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title_2.setFont(font)
        self.Title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_2.setObjectName("Title_2")

        self.retranslateUi(BANK_SERVICES)
        QtCore.QMetaObject.connectSlotsByName(BANK_SERVICES)

    def retranslateUi(self, BANK_SERVICES):
        _translate = QtCore.QCoreApplication.translate
        BANK_SERVICES.setWindowTitle(_translate("BANK_SERVICES", "Bank Services"))
        self.Title.setText(_translate("BANK_SERVICES", "BANK SERVICES "))
        self.DEBIT.setText(_translate("BANK_SERVICES", "DEBIT"))
        self.CREDIT.setText(_translate("BANK_SERVICES", "CREDIT"))
        self.BALANCE.setText(_translate("BANK_SERVICES", "BALANCE"))
        self.PROFILE.setText(_translate("BANK_SERVICES", "PROFILE"))
        self.QUIT.setText(_translate("BANK_SERVICES", "Logout"))
        self.MODIFY.setText(_translate("BANK_SERVICES", "MODIFY"))
        self.DELETE_ACCOUNT.setText(_translate("BANK_SERVICES", "DELETE ACCOUNT"))
        self.TRANSFER.setText(_translate("BANK_SERVICES", "TRANSFER"))
        self.Title_2.setText(_translate("BANK_SERVICES", "WELCOME TO YOUR DASHBOARD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BANK_SERVICES = QtWidgets.QDialog()
    ui = Ui_BANK_SERVICES()
    ui.setupUi(BANK_SERVICES)
    BANK_SERVICES.show()
    sys.exit(app.exec_())
