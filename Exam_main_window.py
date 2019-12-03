# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exam_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExamQuestions(object):
    def setupUi(self, ExamQuestions):
        ExamQuestions.setObjectName("ExamQuestions")
        ExamQuestions.resize(1200, 944)
        ExamQuestions.setMinimumSize(QtCore.QSize(1200, 944))
        ExamQuestions.setMaximumSize(QtCore.QSize(1200, 944))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/ep_program_logo_user_acc_zrP_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExamQuestions.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ExamQuestions)
        self.centralwidget.setObjectName("centralwidget")
        self.RefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshButton.setGeometry(QtCore.QRect(1080, 860, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.RefreshButton.setFont(font)
        self.RefreshButton.setObjectName("RefreshButton")
        self.LogoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogoutButton.setGeometry(QtCore.QRect(960, 860, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LogoutButton.setFont(font)
        self.LogoutButton.setObjectName("LogoutButton")
        self.TopWidget = QtWidgets.QWidget(self.centralwidget)
        self.TopWidget.setGeometry(QtCore.QRect(100, 8, 1090, 103))
        self.TopWidget.setObjectName("TopWidget")
        self.ExamTitle = QtWidgets.QLabel(self.TopWidget)
        self.ExamTitle.setGeometry(QtCore.QRect(10, 10, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ExamTitle.setFont(font)
        self.ExamTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ExamTitle.setObjectName("ExamTitle")
        self.ClassLabel = QtWidgets.QLabel(self.TopWidget)
        self.ClassLabel.setGeometry(QtCore.QRect(300, 4, 90, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ClassLabel.setFont(font)
        self.ClassLabel.setObjectName("ClassLabel")
        self.StudentNicknameLabel = QtWidgets.QLabel(self.TopWidget)
        self.StudentNicknameLabel.setGeometry(QtCore.QRect(300, 50, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.StudentNicknameLabel.setFont(font)
        self.StudentNicknameLabel.setObjectName("StudentNicknameLabel")
        self.ForwardButton = QtWidgets.QPushButton(self.TopWidget)
        self.ForwardButton.setGeometry(QtCore.QRect(920, 50, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ForwardButton.setFont(font)
        self.ForwardButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/ep_program_logo_user_acc_zrP_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ForwardButton.setIcon(icon1)
        self.ForwardButton.setObjectName("ForwardButton")
        self.BackButton = QtWidgets.QPushButton(self.TopWidget)
        self.BackButton.setGeometry(QtCore.QRect(780, 50, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../06Icons_and_Logos/ep_program_logo_user_acc_zrP_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon2)
        self.BackButton.setObjectName("BackButton")
        self.QuestionNumber = QtWidgets.QLabel(self.TopWidget)
        self.QuestionNumber.setGeometry(QtCore.QRect(980, 10, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.QuestionNumber.setFont(font)
        self.QuestionNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QuestionNumber.setObjectName("QuestionNumber")
        self.StudentNameLabel = QtWidgets.QLabel(self.TopWidget)
        self.StudentNameLabel.setGeometry(QtCore.QRect(300, 74, 260, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.StudentNameLabel.setFont(font)
        self.StudentNameLabel.setObjectName("StudentNameLabel")
        self.StudentNumberLabel = QtWidgets.QLabel(self.TopWidget)
        self.StudentNumberLabel.setGeometry(QtCore.QRect(300, 28, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.StudentNumberLabel.setFont(font)
        self.StudentNumberLabel.setObjectName("StudentNumberLabel")
        self.StudentPhotoLabel = QtWidgets.QLabel(self.TopWidget)
        self.StudentPhotoLabel.setGeometry(QtCore.QRect(200, 4, 75, 90))
        self.StudentPhotoLabel.setText("")
        self.StudentPhotoLabel.setPixmap(QtGui.QPixmap("../img/blank_girl.png"))
        self.StudentPhotoLabel.setScaledContents(True)
        self.StudentPhotoLabel.setObjectName("StudentPhotoLabel")
        self.QuestionNumberLabel = QtWidgets.QLabel(self.TopWidget)
        self.QuestionNumberLabel.setGeometry(QtCore.QRect(785, 10, 186, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.QuestionNumberLabel.setFont(font)
        self.QuestionNumberLabel.setObjectName("QuestionNumberLabel")
        self.Questions = QtWidgets.QLabel(self.centralwidget)
        self.Questions.setGeometry(QtCore.QRect(10, 116, 612, 314))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Questions.setFont(font)
        self.Questions.setFrameShape(QtWidgets.QFrame.Panel)
        self.Questions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Questions.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Questions.setWordWrap(True)
        self.Questions.setObjectName("Questions")
        self.CompletedProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.CompletedProgressBar.setGeometry(QtCore.QRect(560, 860, 371, 23))
        self.CompletedProgressBar.setProperty("value", 24)
        self.CompletedProgressBar.setObjectName("CompletedProgressBar")
        self.StartTime = QtWidgets.QLabel(self.centralwidget)
        self.StartTime.setGeometry(QtCore.QRect(110, 860, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.StartTime.setFont(font)
        self.StartTime.setObjectName("StartTime")
        self.VideoFrame = QtWidgets.QFrame(self.centralwidget)
        self.VideoFrame.setGeometry(QtCore.QRect(630, 116, 560, 314))
        self.VideoFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.VideoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VideoFrame.setObjectName("VideoFrame")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 440, 1177, 351))
        self.tabWidget.setMaximumSize(QtCore.QSize(1177, 351))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.AnswerATab = QtWidgets.QWidget()
        self.AnswerATab.setObjectName("AnswerATab")
        self.AnswerTextA = QtWidgets.QLabel(self.AnswerATab)
        self.AnswerTextA.setGeometry(QtCore.QRect(330, 10, 830, 340))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.AnswerTextA.setFont(font)
        self.AnswerTextA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.AnswerTextA.setWordWrap(True)
        self.AnswerTextA.setObjectName("AnswerTextA")
        self.tabWidget.addTab(self.AnswerATab, "")
        self.AnswerBTab = QtWidgets.QWidget()
        self.AnswerBTab.setObjectName("AnswerBTab")
        self.AnswerTextB = QtWidgets.QLabel(self.AnswerBTab)
        self.AnswerTextB.setGeometry(QtCore.QRect(330, 10, 830, 340))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.AnswerTextB.setFont(font)
        self.AnswerTextB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.AnswerTextB.setWordWrap(True)
        self.AnswerTextB.setObjectName("AnswerTextB")
        self.tabWidget.addTab(self.AnswerBTab, "")
        self.AnswerCTab = QtWidgets.QWidget()
        self.AnswerCTab.setObjectName("AnswerCTab")
        self.AnswerTextC = QtWidgets.QLabel(self.AnswerCTab)
        self.AnswerTextC.setGeometry(QtCore.QRect(330, 10, 830, 340))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.AnswerTextC.setFont(font)
        self.AnswerTextC.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.AnswerTextC.setWordWrap(True)
        self.AnswerTextC.setObjectName("AnswerTextC")
        self.tabWidget.addTab(self.AnswerCTab, "")
        self.AnswerDTab = QtWidgets.QWidget()
        self.AnswerDTab.setObjectName("AnswerDTab")
        self.AnswerTextD = QtWidgets.QLabel(self.AnswerDTab)
        self.AnswerTextD.setGeometry(QtCore.QRect(330, 10, 830, 340))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.AnswerTextD.setFont(font)
        self.AnswerTextD.setTextFormat(QtCore.Qt.PlainText)
        self.AnswerTextD.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.AnswerTextD.setWordWrap(True)
        self.AnswerTextD.setObjectName("AnswerTextD")
        self.tabWidget.addTab(self.AnswerDTab, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 800, 1180, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.AnswerACheckBox = QtWidgets.QCheckBox(self.frame)
        self.AnswerACheckBox.setGeometry(QtCore.QRect(30, 10, 20, 17))
        self.AnswerACheckBox.setText("")
        self.AnswerACheckBox.setObjectName("AnswerACheckBox")
        self.AnswerButtonGroup = QtWidgets.QButtonGroup(ExamQuestions)
        self.AnswerButtonGroup.setObjectName("AnswerButtonGroup")
        self.AnswerButtonGroup.addButton(self.AnswerACheckBox)
        self.Alabel = QtWidgets.QLabel(self.frame)
        self.Alabel.setGeometry(QtCore.QRect(4, 4, 26, 26))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Alabel.setFont(font)
        self.Alabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Alabel.setObjectName("Alabel")
        self.AnswerBCheckBox = QtWidgets.QCheckBox(self.frame)
        self.AnswerBCheckBox.setGeometry(QtCore.QRect(80, 10, 20, 17))
        self.AnswerBCheckBox.setText("")
        self.AnswerBCheckBox.setObjectName("AnswerBCheckBox")
        self.AnswerButtonGroup.addButton(self.AnswerBCheckBox)
        self.Blabel = QtWidgets.QLabel(self.frame)
        self.Blabel.setGeometry(QtCore.QRect(54, 4, 26, 26))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Blabel.setFont(font)
        self.Blabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Blabel.setObjectName("Blabel")
        self.AnswerCCheckBox = QtWidgets.QCheckBox(self.frame)
        self.AnswerCCheckBox.setGeometry(QtCore.QRect(130, 10, 20, 17))
        self.AnswerCCheckBox.setText("")
        self.AnswerCCheckBox.setObjectName("AnswerCCheckBox")
        self.AnswerButtonGroup.addButton(self.AnswerCCheckBox)
        self.Clabel = QtWidgets.QLabel(self.frame)
        self.Clabel.setGeometry(QtCore.QRect(104, 4, 26, 26))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Clabel.setFont(font)
        self.Clabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Clabel.setObjectName("Clabel")
        self.AnswerDCheckBox = QtWidgets.QCheckBox(self.frame)
        self.AnswerDCheckBox.setGeometry(QtCore.QRect(180, 10, 20, 17))
        self.AnswerDCheckBox.setText("")
        self.AnswerDCheckBox.setObjectName("AnswerDCheckBox")
        self.AnswerButtonGroup.addButton(self.AnswerDCheckBox)
        self.Dlabel = QtWidgets.QLabel(self.frame)
        self.Dlabel.setGeometry(QtCore.QRect(154, 4, 26, 26))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Dlabel.setFont(font)
        self.Dlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Dlabel.setObjectName("Dlabel")
        self.FalsecheckBox = QtWidgets.QCheckBox(self.frame)
        self.FalsecheckBox.setGeometry(QtCore.QRect(210, 10, 70, 17))
        self.FalsecheckBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.FalsecheckBox.setText("")
        self.FalsecheckBox.setObjectName("FalsecheckBox")
        self.AnswerButtonGroup.addButton(self.FalsecheckBox)
        self.MsgLabel = QtWidgets.QLabel(self.frame)
        self.MsgLabel.setGeometry(QtCore.QRect(340, 4, 1000, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.MsgLabel.setFont(font)
        self.MsgLabel.setObjectName("MsgLabel")
        self.ArrowLabel = QtWidgets.QLabel(self.frame)
        self.ArrowLabel.setGeometry(QtCore.QRect(256, 5, 60, 30))
        self.ArrowLabel.setText("")
        self.ArrowLabel.setPixmap(QtGui.QPixmap("../06Icons_and_Logos/Left_Arrow.png"))
        self.ArrowLabel.setObjectName("ArrowLabel")
        self.StartTimelabel = QtWidgets.QLabel(self.centralwidget)
        self.StartTimelabel.setGeometry(QtCore.QRect(10, 860, 93, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.StartTimelabel.setFont(font)
        self.StartTimelabel.setObjectName("StartTimelabel")
        self.SchoolLabel = QtWidgets.QLabel(self.centralwidget)
        self.SchoolLabel.setGeometry(QtCore.QRect(10, 10, 75, 97))
        self.SchoolLabel.setText("")
        self.SchoolLabel.setPixmap(QtGui.QPixmap("../img/School logo75x97_grad.png"))
        self.SchoolLabel.setObjectName("SchoolLabel")
        self.TimeLeft = QtWidgets.QLabel(self.centralwidget)
        self.TimeLeft.setGeometry(QtCore.QRect(330, 860, 111, 30))
        self.TimeLeft.setObjectName("TimeLeft")
        self.TimeLeftlabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLeftlabel.setGeometry(QtCore.QRect(230, 860, 93, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TimeLeftlabel.setFont(font)
        self.TimeLeftlabel.setObjectName("TimeLeftlabel")
        ExamQuestions.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExamQuestions)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        ExamQuestions.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExamQuestions)
        self.statusbar.setObjectName("statusbar")
        ExamQuestions.setStatusBar(self.statusbar)

        self.retranslateUi(ExamQuestions)
        self.tabWidget.setCurrentIndex(0)
        self.LogoutButton.clicked.connect(ExamQuestions.logout_button_clicked)
        self.RefreshButton.clicked.connect(ExamQuestions.exam_refresh_button_clicked)
        self.BackButton.clicked.connect(ExamQuestions.back_button_clicked)
        self.ForwardButton.clicked.connect(ExamQuestions.forward_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(ExamQuestions)
        ExamQuestions.setTabOrder(self.tabWidget, self.AnswerACheckBox)
        ExamQuestions.setTabOrder(self.AnswerACheckBox, self.AnswerBCheckBox)
        ExamQuestions.setTabOrder(self.AnswerBCheckBox, self.AnswerCCheckBox)
        ExamQuestions.setTabOrder(self.AnswerCCheckBox, self.AnswerDCheckBox)
        ExamQuestions.setTabOrder(self.AnswerDCheckBox, self.ForwardButton)
        ExamQuestions.setTabOrder(self.ForwardButton, self.LogoutButton)
        ExamQuestions.setTabOrder(self.LogoutButton, self.BackButton)
        ExamQuestions.setTabOrder(self.BackButton, self.RefreshButton)

    def retranslateUi(self, ExamQuestions):
        _translate = QtCore.QCoreApplication.translate
        ExamQuestions.setWindowTitle(_translate("ExamQuestions", "Exam Questions"))
        self.RefreshButton.setText(_translate("ExamQuestions", "Refresh"))
        self.LogoutButton.setStatusTip(_translate("ExamQuestions", "Click to Log out user."))
        self.LogoutButton.setText(_translate("ExamQuestions", "Log Out"))
        self.LogoutButton.setShortcut(_translate("ExamQuestions", "Esc"))
        self.ExamTitle.setText(_translate("ExamQuestions", "C21202\n"
"Midterm Exam "))
        self.ClassLabel.setText(_translate("ExamQuestions", "Class"))
        self.StudentNicknameLabel.setText(_translate("ExamQuestions", "Nickname"))
        self.ForwardButton.setStatusTip(_translate("ExamQuestions", "Click to go to the next question."))
        self.ForwardButton.setText(_translate("ExamQuestions", "Next"))
        self.ForwardButton.setShortcut(_translate("ExamQuestions", "Right, Return"))
        self.BackButton.setText(_translate("ExamQuestions", "Back     "))
        self.BackButton.setShortcut(_translate("ExamQuestions", "Left"))
        self.QuestionNumber.setText(_translate("ExamQuestions", "QNum"))
        self.StudentNameLabel.setText(_translate("ExamQuestions", "Full Name"))
        self.StudentNumberLabel.setText(_translate("ExamQuestions", "Num"))
        self.QuestionNumberLabel.setText(_translate("ExamQuestions", "Question Number:"))
        self.Questions.setText(_translate("ExamQuestions", "Questions"))
        self.CompletedProgressBar.setStatusTip(_translate("ExamQuestions", "Amount you have completed."))
        self.CompletedProgressBar.setFormat(_translate("ExamQuestions", "%p%"))
        self.StartTime.setText(_translate("ExamQuestions", "Time"))
        self.tabWidget.setStatusTip(_translate("ExamQuestions", "Click to view possible answers."))
        self.AnswerTextA.setText(_translate("ExamQuestions", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnswerATab), _translate("ExamQuestions", "A"))
        self.AnswerTextB.setText(_translate("ExamQuestions", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnswerBTab), _translate("ExamQuestions", "B"))
        self.AnswerTextC.setText(_translate("ExamQuestions", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnswerCTab), _translate("ExamQuestions", "C"))
        self.AnswerTextD.setText(_translate("ExamQuestions", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnswerDTab), _translate("ExamQuestions", "D"))
        self.AnswerACheckBox.setStatusTip(_translate("ExamQuestions", "Click to choose Answer A."))
        self.AnswerACheckBox.setShortcut(_translate("ExamQuestions", "A"))
        self.Alabel.setText(_translate("ExamQuestions", "A"))
        self.AnswerBCheckBox.setStatusTip(_translate("ExamQuestions", "Click to choose Answer B."))
        self.AnswerBCheckBox.setShortcut(_translate("ExamQuestions", "B"))
        self.Blabel.setText(_translate("ExamQuestions", "B"))
        self.AnswerCCheckBox.setStatusTip(_translate("ExamQuestions", "Click to choose Answer C."))
        self.AnswerCCheckBox.setShortcut(_translate("ExamQuestions", "C"))
        self.Clabel.setText(_translate("ExamQuestions", "C"))
        self.AnswerDCheckBox.setStatusTip(_translate("ExamQuestions", "Click to choose Answer D."))
        self.AnswerDCheckBox.setShortcut(_translate("ExamQuestions", "D"))
        self.Dlabel.setText(_translate("ExamQuestions", "D"))
        self.MsgLabel.setText(_translate("ExamQuestions", "Please choose an answer"))
        self.StartTimelabel.setText(_translate("ExamQuestions", "Start Time"))
        self.TimeLeft.setText(_translate("ExamQuestions", "Time"))
        self.TimeLeftlabel.setText(_translate("ExamQuestions", "Time Left:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExamQuestions = QtWidgets.QMainWindow()
    ui = Ui_ExamQuestions()
    ui.setupUi(ExamQuestions)
    ExamQuestions.show()
    sys.exit(app.exec_())
