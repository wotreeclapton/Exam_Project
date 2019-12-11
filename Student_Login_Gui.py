# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_Login_Gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExamLogin(object):
    def setupUi(self, ExamLogin):
        ExamLogin.setObjectName("ExamLogin")
        ExamLogin.resize(588, 270)
        ExamLogin.setMinimumSize(QtCore.QSize(588, 270))
        ExamLogin.setMaximumSize(QtCore.QSize(588, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ep_program_logo_user_acc_zrP_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExamLogin.setWindowIcon(icon)
        ExamLogin.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(ExamLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.ClassLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClassLabel.setGeometry(QtCore.QRect(10, 10, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ClassLabel.setFont(font)
        self.ClassLabel.setObjectName("ClassLabel")

        self.StudentNameCmb = QtWidgets.QComboBox(self.centralwidget)
        self.StudentNameCmb.setGeometry(QtCore.QRect(10, 140, 391, 22))
        self.StudentNameCmb.setObjectName("StudentNameCmb")

        self.EnterNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.EnterNameLabel.setGeometry(QtCore.QRect(10, 114, 211, 16))
        self.EnterNameLabel.setObjectName("EnterNameLabel")

        self.InputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.InputPassword.setGeometry(QtCore.QRect(10, 200, 221, 20))
        self.InputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.InputPassword.setObjectName("InputPassword")

        self.InputPaswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.InputPaswordLabel.setGeometry(QtCore.QRect(10, 172, 131, 16))
        self.InputPaswordLabel.setObjectName("InputPaswordLabel")

        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(418, 216, 156, 23))
        self.buttonBox.setToolTip("")
        self.buttonBox.setStatusTip("")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.Logolabel = QtWidgets.QLabel(self.centralwidget)
        self.Logolabel.setEnabled(True)
        self.Logolabel.setGeometry(QtCore.QRect(320, 20, 75, 97))
        self.Logolabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Logolabel.setToolTipDuration(-5)
        self.Logolabel.setText("")
        self.Logolabel.setPixmap(QtGui.QPixmap("img/School logo75x97_grad.png"))
        self.Logolabel.setObjectName("Logolabel")

        self.PasswordShowButton = QtWidgets.QPushButton(self.centralwidget)
        self.PasswordShowButton.setGeometry(QtCore.QRect(210, 201, 20, 18))
        self.PasswordShowButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PasswordShowButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../06Icons_and_Logos/Password_Icon_20x20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PasswordShowButton.setIcon(icon1)
        self.PasswordShowButton.setIconSize(QtCore.QSize(20, 18))
        self.PasswordShowButton.setCheckable(False)
        self.PasswordShowButton.setAutoRepeat(True)
        self.PasswordShowButton.setAutoRepeatDelay(200)
        self.PasswordShowButton.setObjectName("PasswordShowButton")

        self.StudentPhoto = QtWidgets.QLabel(self.centralwidget)
        self.StudentPhoto.setGeometry(QtCore.QRect(414, 10, 160, 192))
        self.StudentPhoto.setFrameShape(QtWidgets.QFrame.Panel)
        self.StudentPhoto.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.StudentPhoto.setText("")
        self.StudentPhoto.setPixmap(QtGui.QPixmap("img/blank_girl.png"))
        self.StudentPhoto.setObjectName("StudentPhoto")

        self.ClassCmb = QtWidgets.QComboBox(self.centralwidget)
        self.ClassCmb.setGeometry(QtCore.QRect(10, 80, 151, 22))
        self.ClassCmb.setCurrentText("")
        self.ClassCmb.setObjectName("ClassCmb")

        self.StudentNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.StudentNumberLabel.setGeometry(QtCore.QRect(250, 170, 50, 18))
        font = QtGui.QFont()
        font.setItalic(True)
        self.StudentNumberLabel.setFont(font)
        self.StudentNumberLabel.setObjectName("StudentNumberLabel")

        self.StudentNicknameLabel = QtWidgets.QLabel(self.centralwidget)
        self.StudentNicknameLabel.setGeometry(QtCore.QRect(250, 200, 50, 18))
        font = QtGui.QFont()
        font.setItalic(True)
        self.StudentNicknameLabel.setFont(font)
        self.StudentNicknameLabel.setObjectName("StudentNicknameLabel")
        
        self.StudentNumber = QtWidgets.QLabel(self.centralwidget)
        self.StudentNumber.setGeometry(QtCore.QRect(308, 170, 94, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StudentNumber.setFont(font)
        self.StudentNumber.setText("")
        self.StudentNumber.setObjectName("StudentNumber")

        self.StudentNickname = QtWidgets.QLabel(self.centralwidget)
        self.StudentNickname.setGeometry(QtCore.QRect(308, 200, 94, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StudentNickname.setFont(font)
        self.StudentNickname.setObjectName("StudentNickname")
        
        ExamLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExamLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        ExamLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExamLogin)
        self.statusbar.setMinimumSize(QtCore.QSize(0, 20))
        self.statusbar.setMaximumSize(QtCore.QSize(588, 20))
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        ExamLogin.setStatusBar(self.statusbar)

        self.retranslateUi(ExamLogin)
        self.buttonBox.accepted.connect(ExamLogin.login_okaybutton_clicked)
        self.buttonBox.rejected.connect(ExamLogin.login_cancelbutton_clicked)
        self.PasswordShowButton.clicked.connect(ExamLogin.password_show_button_clicked)
        self.InputPassword.returnPressed.connect(ExamLogin.login_okaybutton_clicked)
        self.ClassCmb.currentIndexChanged['int'].connect(ExamLogin.class_name_changed)
        self.StudentNameCmb.currentIndexChanged['int'].connect(ExamLogin.student_name_change)
        QtCore.QMetaObject.connectSlotsByName(ExamLogin)
        ExamLogin.setTabOrder(self.ClassCmb, self.StudentNameCmb)
        ExamLogin.setTabOrder(self.StudentNameCmb, self.InputPassword)
        ExamLogin.setTabOrder(self.InputPassword, self.PasswordShowButton)

    def retranslateUi(self, ExamLogin):
        _translate = QtCore.QCoreApplication.translate
        ExamLogin.setWindowTitle(_translate("ExamLogin", "Exam Login"))
        self.ClassLabel.setText(_translate("ExamLogin", "Class"))
        self.StudentNameCmb.setToolTip(_translate("ExamLogin", "Click arrow to choose your name!"))
        self.StudentNameCmb.setStatusTip(_translate("ExamLogin", "Choose a name"))
        self.EnterNameLabel.setText(_translate("ExamLogin", "Choose your name from the list below"))
        self.InputPassword.setToolTip(_translate("ExamLogin", "Password goes here!"))
        self.InputPassword.setStatusTip(_translate("ExamLogin", "Input your password"))
        self.InputPaswordLabel.setText(_translate("ExamLogin", "Password"))
        self.ClassCmb.setToolTip(_translate("ExamLogin", "Choose your class!"))
        self.ClassCmb.setStatusTip(_translate("ExamLogin", "Choose your class first"))
        self.StudentNumberLabel.setText(_translate("ExamLogin", "Number:"))
        self.StudentNicknameLabel.setText(_translate("ExamLogin", "Nickname:"))
        self.StudentNickname.setText(_translate("ExamLogin", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExamLogin = QtWidgets.QMainWindow()
    ui = Ui_ExamLogin()
    ui.setupUi(ExamLogin)
    ExamLogin.show()
    sys.exit(app.exec_())
