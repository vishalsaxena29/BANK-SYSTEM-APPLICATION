
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_TRANSERWINDOW(object):

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

    def WithdrawalCancle(self):
        from services import Ui_BANK_SERVICES
        print('WithdrawalCancle')
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_BANK_SERVICES()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, TRANSERWINDOW):
        TRANSERWINDOW.setObjectName("TRANSERWINDOW")
        TRANSERWINDOW.resize(494, 450)
        TRANSERWINDOW.setStyleSheet("QDialog{background-color:qlineargradient(spread:pad, x1:0.438222, y1:0.0743182, x2:0.418961, y2:1, stop:0.413793 rgba(59, 136, 89, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.Title = QtWidgets.QLabel(TRANSERWINDOW)
        self.Title.setGeometry(QtCore.QRect(10, 10, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(33)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Enter_Amt_label = QtWidgets.QLabel(TRANSERWINDOW)
        self.Enter_Amt_label.setGeometry(QtCore.QRect(30, 110, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Enter_Amt_label.setFont(font)
        self.Enter_Amt_label.setObjectName("Enter_Amt_label")
        self.Act_holder_label_2 = QtWidgets.QLabel(TRANSERWINDOW)
        self.Act_holder_label_2.setGeometry(QtCore.QRect(30, 160, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Act_holder_label_2.setFont(font)
        self.Act_holder_label_2.setObjectName("Act_holder_label_2")
        self.Act_number_label_3 = QtWidgets.QLabel(TRANSERWINDOW)
        self.Act_number_label_3.setGeometry(QtCore.QRect(30, 210, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Act_number_label_3.setFont(font)
        self.Act_number_label_3.setObjectName("Act_number_label_3")
        self.Act_type_comboBox = QtWidgets.QComboBox(TRANSERWINDOW)
        self.Act_type_comboBox.setGeometry(QtCore.QRect(90, 250, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Act_type_comboBox.setFont(font)
        self.Act_type_comboBox.setObjectName("Act_type_comboBox")
        self.Act_type_comboBox.addItem("")
        self.Act_type_comboBox.addItem("")
        self.Act_type_comboBox.addItem("")
        self.Bank_Name_comboBox_2 = QtWidgets.QComboBox(TRANSERWINDOW)
        self.Bank_Name_comboBox_2.setGeometry(QtCore.QRect(90, 300, 341, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Bank_Name_comboBox_2.setFont(font)
        self.Bank_Name_comboBox_2.setObjectName("Bank_Name_comboBox_2")
        self.Bank_Name_comboBox_2.addItem("")
        self.Bank_Name_comboBox_2.addItem("")
        self.Bank_Name_comboBox_2.addItem("")
        self.Bank_Name_comboBox_2.addItem("")
        self.Bank_Name_comboBox_2.addItem("")
        self.Bank_Name_comboBox_2.addItem("")
        self.Bank_Name_comboBox_2.addItem("")
        self.Bank_Name_comboBox_2.addItem("")
        self.Entr_Amt_lineEdit = QtWidgets.QLineEdit(TRANSERWINDOW)
        self.Entr_Amt_lineEdit.setGeometry(QtCore.QRect(330, 110, 113, 21))
        self.Entr_Amt_lineEdit.setObjectName("Entr_Amt_lineEdit")
        self.Act_holder_lineEdit_2 = QtWidgets.QLineEdit(TRANSERWINDOW)
        self.Act_holder_lineEdit_2.setGeometry(QtCore.QRect(330, 160, 113, 21))
        self.Act_holder_lineEdit_2.setObjectName("Act_holder_lineEdit_2")
        self.Account_nbr_lineEdit_3 = QtWidgets.QLineEdit(TRANSERWINDOW)
        self.Account_nbr_lineEdit_3.setGeometry(QtCore.QRect(330, 210, 113, 21))
        self.Account_nbr_lineEdit_3.setObjectName("Account_nbr_lineEdit_3")
        self.Transfer_pushButton = QtWidgets.QPushButton(TRANSERWINDOW)
        self.Transfer_pushButton.setGeometry(QtCore.QRect(90, 360, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Transfer_pushButton.setFont(font)
        self.Transfer_pushButton.setObjectName("Transfer_pushButton")
        self.Cancel_pushButton_2 = QtWidgets.QPushButton(TRANSERWINDOW)
        self.Cancel_pushButton_2.setGeometry(QtCore.QRect(260, 360, 113, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_pushButton_2.setFont(font)
        self.Cancel_pushButton_2.setObjectName("Cancel_pushButton_2")
        self.Cancel_pushButton_2.clicked.connect(self.WithdrawalCancle)

        self.retranslateUi(TRANSERWINDOW)
        QtCore.QMetaObject.connectSlotsByName(TRANSERWINDOW)

    def retranslateUi(self, TRANSERWINDOW):
        _translate = QtCore.QCoreApplication.translate
        TRANSERWINDOW.setWindowTitle(_translate("TRANSERWINDOW", "TRANSFER WINDOW"))
        self.Title.setText(_translate("TRANSERWINDOW", "BANK TRANSFER WINDOW "))
        self.Enter_Amt_label.setText(_translate("TRANSERWINDOW", "ENTER AMOUNT TO TRANSFER"))
        self.Act_holder_label_2.setText(_translate("TRANSERWINDOW", "ACCOUNT HOLDER NAME"))
        self.Act_number_label_3.setText(_translate("TRANSERWINDOW", "ACCOUNT NUMBER"))
        self.Act_type_comboBox.setItemText(0, _translate("TRANSERWINDOW", "Account Type"))
        self.Act_type_comboBox.setItemText(1, _translate("TRANSERWINDOW", "Saving Account"))
        self.Act_type_comboBox.setItemText(2, _translate("TRANSERWINDOW", "CUrrent Account"))
        self.Bank_Name_comboBox_2.setItemText(0, _translate("TRANSERWINDOW", "BANK NAME"))
        self.Bank_Name_comboBox_2.setItemText(1, _translate("TRANSERWINDOW", "FirstBank"))
        self.Bank_Name_comboBox_2.setItemText(2, _translate("TRANSERWINDOW", "CITI BANK"))
        self.Bank_Name_comboBox_2.setItemText(3, _translate("TRANSERWINDOW", "YES BANK"))
        self.Bank_Name_comboBox_2.setItemText(4, _translate("TRANSERWINDOW", "SBI BANK"))
        self.Bank_Name_comboBox_2.setItemText(5, _translate("TRANSERWINDOW", "HDFC BANK"))
        self.Bank_Name_comboBox_2.setItemText(6, _translate("TRANSERWINDOW", "AXIS BANK"))
        self.Bank_Name_comboBox_2.setItemText(7, _translate("TRANSERWINDOW", "OTHERS"))
        self.Transfer_pushButton.setText(_translate("TRANSERWINDOW", "TRANSFER"))
        self.Cancel_pushButton_2.setText(_translate("TRANSERWINDOW", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TRANSERWINDOW = QtWidgets.QDialog()
    ui = Ui_TRANSERWINDOW()
    ui.setupUi(TRANSERWINDOW)
    TRANSERWINDOW.show()
    sys.exit(app.exec_())