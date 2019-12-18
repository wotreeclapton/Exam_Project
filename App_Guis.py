'''
Exam app Guis developed by Mr Steven J Walden
    Dec. 2019
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license at end of file]
'''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaPlayer

class Ui_ExamLogin(QtWidgets.QMainWindow):
	"""docstrbing for MyApp"""
	def __init__(self, parent=None):
		super(Ui_ExamLogin, self).__init__(parent)
		self.initUI()

	def initUI(self):
		#Set up GUI
		self.resize(588, 270)
		self.setMinimumSize(588, 270)
		self.setMaximumSize(588, 270)
		self.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
		self.setWindowTitle("Login")

		self.statusbar = QtWidgets.QStatusBar(self)
		self.statusbar.setSizeGripEnabled(False)
		self.setStatusBar(self.statusbar)

		self.add_labels()
		self.add_textboxes()
		self.add_buttons()
		self.add_comboboxes()
		self.tool_status_tips()
		self.tab_order()

	def add_labels(self):
		#Add Label for displaying the class name
		self.ClassLabel = QtWidgets.QLabel("Class", self)
		self.ClassLabel.setGeometry(10, 10, 300, 60)
		font = QtGui.QFont()
		font.setPointSize(30)
		font.setBold(True)
		font.setItalic(True)
		#font.setWeight(75)
		self.ClassLabel.setFont(font)
		self.ClassLabel.setText("Class")
		#Add label for student name combobox
		self.EnterNameLabel = QtWidgets.QLabel("Choose your name from the list below", self)
		self.EnterNameLabel.setGeometry(10, 114, 211, 16)
		#Label for password box
		self.InputPaswordLabel = QtWidgets.QLabel("Password", self)
		self.InputPaswordLabel.setGeometry(10, 172, 131, 16)
		#Display school logo
		self.Logolabel = QtWidgets.QLabel(self)
		self.Logolabel.setGeometry(320, 20, 75, 97)
		self.Logolabel.setPixmap(QtGui.QPixmap("img/School logo75x97_grad.png"))
		#Label for student number box
		font = QtGui.QFont()
		font.setItalic(True)
		self.StudentNumberLabel = QtWidgets.QLabel("Number:",self)
		self.StudentNumberLabel.setGeometry(250, 170, 50, 18)
		self.StudentNumberLabel.setFont(font)
		#Label for student nickname box
		self.StudentNicknameLabel = QtWidgets.QLabel("Nickname:", self)
		self.StudentNicknameLabel.setGeometry(250, 200, 50, 18)
		self.StudentNicknameLabel.setFont(font)
		#Student number display box
		font = QtGui.QFont()
		font.setBold(True)
		#font.setWeight(75)
		self.StudentNumber = QtWidgets.QLabel(self)
		self.StudentNumber.setGeometry(308, 170, 94, 18)
		self.StudentNumber.setFont(font)
		#Student nickname display box
		self.StudentNickname = QtWidgets.QLabel(self)
		self.StudentNickname.setGeometry(308, 200, 94, 18)
		self.StudentNickname.setFont(font)
		#Student photo image display
		self.StudentPhoto = QtWidgets.QLabel(self)
		self.StudentPhoto.setGeometry(414, 10, 160, 192)
		self.StudentPhoto.setFrameShape(QtWidgets.QFrame.Panel)
		self.StudentPhoto.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.StudentPhoto.setPixmap(QtGui.QPixmap("img/blank_girl.png"))

	def add_textboxes(self):
		#Textbox input for password
		self.InputPassword = QtWidgets.QLineEdit(self)
		self.InputPassword.setGeometry(10, 200, 221, 20)
		self.InputPassword.setEchoMode(QtWidgets.QLineEdit.Password)

	def add_buttons(self):
		#Button box setup for OKay and cancel buttons
		self.buttonBox = QtWidgets.QDialogButtonBox(self)
		self.buttonBox.setGeometry(418, 216, 156, 23)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		#Button for showing the password temporarily
		self.PasswordShowButton = QtWidgets.QPushButton(self)
		self.PasswordShowButton.setGeometry(210, 201, 20, 18)
		self.PasswordShowButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.PasswordShowButton.setIcon(QtGui.QIcon("img/Password_Icon_20x20.png"))
		self.PasswordShowButton.setIconSize(QtCore.QSize(20, 18))
		self.PasswordShowButton.setCheckable(False)
		self.PasswordShowButton.setAutoRepeat(True)
		self.PasswordShowButton.setAutoRepeatDelay(200)

	def add_comboboxes(self):
		#Combobox setup to choose the class
		self.ClassCmb = QtWidgets.QComboBox(self)
		self.ClassCmb.setGeometry(10, 80, 151, 22)
		#Combox set to choose the student
		self.StudentNameCmb = QtWidgets.QComboBox(self)
		self.StudentNameCmb.setGeometry(10, 140, 391, 22)

	def tool_status_tips(self):
		#Setup any tool and status bar tips
		self.StudentNameCmb.setToolTip("Click arrow to choose your name!")
		self.ClassCmb.setToolTip("Choose your class!")
		self.InputPassword.setToolTip("Password goes here!")

		self.StudentNameCmb.setStatusTip("Choose a name")
		self.InputPassword.setStatusTip("Input your password")
		self.ClassCmb.setStatusTip("Choose your class first")

	def tab_order(self):
		self.setTabOrder(self.ClassCmb, self.StudentNameCmb)
		self.setTabOrder(self.StudentNameCmb, self.InputPassword)
		self.setTabOrder(self.InputPassword, self.PasswordShowButton)


class Ui_ExamQuestions(QtWidgets.QMainWindow):
	"""docstrbing for MyApp"""
	def __init__(self, screen_size, parent=None):
		super(Ui_ExamQuestions, self).__init__(parent)
		self.screen_height = screen_size.height()
		self.initUI()

	def initUI(self):
		
		#self.screen_width = round(self.screen_height * 1.3)
		self.resize(1200, self.screen_height - 32)
		self.setMinimumSize(1200, 600) # orig size was 1200x924
		self.setMaximumSize(1200, 1080)
		self.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
		self.setWindowTitle("Exam Questions")

		self.add_widgets()
		self.add_layouts()
		self.add_labels()
		self.add_checkboxes()
		self.add_buttons()
		self.add_scrollbars()
		self.tool_status_tips()
		self.tab_order()
		self.kb_shortcuts()

	def add_widgets(self):
		self.TopWidget = QtWidgets.QWidget(self)
		self.TopWidget.setGeometry(100, 8, 1090, 103)

		self.videoWidget = QtMultimediaWidgets.QVideoWidget()

		self.tabWidget = QtWidgets.QTabWidget(self)
		self.tabWidget.setGeometry(10, 440, 1177, 351)
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.tabWidget.setFont(font)

		self.AnswerATab = QtWidgets.QWidget()
		self.tabWidget.addTab(self.AnswerATab, "A")
		self.AnswerBTab = QtWidgets.QWidget()
		self.tabWidget.addTab(self.AnswerBTab, "B")
		self.AnswerCTab = QtWidgets.QWidget()
		self.tabWidget.addTab(self.AnswerCTab, "C")
		self.AnswerDTab = QtWidgets.QWidget()
		self.tabWidget.addTab(self.AnswerDTab, "D")

		self.AnswerButtonGroup = QtWidgets.QButtonGroup(self)

		self.statusbar = QtWidgets.QStatusBar(self)

	def add_layouts(self):
		self.verticalLayoutWidget = QtWidgets.QWidget(self)
		self.verticalLayoutWidget.setGeometry(630, 120, 551, 311)
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)

		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
		self.mediaPlayer.setVideoOutput(self.videoWidget)
		self.verticalLayout.addWidget(self.videoWidget)

		self.frame = QtWidgets.QFrame(self)
		self.frame.setGeometry(10, 800, 1174, 46)
		self.frame.setFrameShape(QtWidgets.QFrame.Panel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

		self.setStatusBar(self.statusbar)

	def add_labels(self):
		self.SchoolLabel = QtWidgets.QLabel(self)
		self.SchoolLabel.setGeometry(10, 10, 75, 97)
		self.SchoolLabel.setPixmap(QtGui.QPixmap("img/School logo75x97_grad.png"))

		self.StudentPhotoLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentPhotoLabel.setGeometry(200, 4, 75, 90)
		self.StudentPhotoLabel.setPixmap(QtGui.QPixmap("img/blank_girl.png"))
		self.StudentPhotoLabel.setScaledContents(True)

		self.ArrowLabel = QtWidgets.QLabel(self.frame)
		self.ArrowLabel.setGeometry(256, 8, 60, 30)
		self.ArrowLabel.setPixmap(QtGui.QPixmap("img/Left_Arrow.png"))

		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		self.ExamTitle = QtWidgets.QLabel(self.TopWidget)
		self.ExamTitle.setGeometry(10, 10, 201, 71)
		self.ExamTitle.setFont(font)
		self.ExamTitle.setAlignment(QtCore.Qt.AlignTop)
		
		font.setPointSize(15)
		self.Alabel = QtWidgets.QLabel(self.frame)
		self.Alabel.setGeometry(4, 9, 26, 26)
		self.Alabel.setFont(font)
		self.Alabel.setAlignment(QtCore.Qt.AlignCenter)
		self.Alabel.setText("A")

		self.Blabel = QtWidgets.QLabel(self.frame)
		self.Blabel.setGeometry(54, 9, 26, 26)
		self.Blabel.setFont(font)
		self.Blabel.setAlignment(QtCore.Qt.AlignCenter)
		self.Blabel.setText("B")

		self.Clabel = QtWidgets.QLabel(self.frame)
		self.Clabel.setGeometry(104, 9, 26, 26)
		self.Clabel.setFont(font)
		self.Clabel.setAlignment(QtCore.Qt.AlignCenter)
		self.Clabel.setText("C")

		self.Dlabel = QtWidgets.QLabel(self.frame)
		self.Dlabel.setGeometry(154, 9, 26, 26)
		self.Dlabel.setFont(font)
		self.Dlabel.setAlignment(QtCore.Qt.AlignCenter)
		self.Dlabel.setText("D")

		font.setPointSize(10)
		self.StartTime = QtWidgets.QLabel(self)
		self.StartTime.setGeometry(110, 860, 90, 30)
		self.StartTime.setFont(font)
		self.StartTime.setText("Time")

		self.EndTime = QtWidgets.QLabel(self)
		self.EndTime.setGeometry(310, 860, 71, 30)
		self.EndTime.setFont(font)
		self.EndTime.setText("Time")

		self.MinLeftLabel = QtWidgets.QLabel(self)
		self.MinLeftLabel.setGeometry(980, 860, 101, 30)
		self.MinLeftLabel.setFont(font)
		self.MinLeftLabel.setText("Mins Left")

		font.setPointSize(16)
		font.setItalic(True)
		self.MsgLabel = QtWidgets.QLabel(self.frame)
		self.MsgLabel.setGeometry(340, 7, 1000, 32)
		self.MsgLabel.setFont(font)
		self.MsgLabel.setText("Please choose an answer")

		font.setPointSize(14)
		self.ClassLabel = QtWidgets.QLabel(self.TopWidget)
		self.ClassLabel.setGeometry(300, 4, 90, 16)
		self.ClassLabel.setFont(font)
		self.ClassLabel.setText("Class")

		self.QuestionNumberLabel = QtWidgets.QLabel(self.TopWidget)
		self.QuestionNumberLabel.setGeometry(785, 10, 186, 30)
		self.QuestionNumberLabel.setFont(font)
		self.QuestionNumberLabel.setText("Question Number:")

		self.QuestionNumber = QtWidgets.QLabel(self.TopWidget)
		self.QuestionNumber.setGeometry(970, 10, 30, 30)
		self.QuestionNumber.setFont(font)
		self.QuestionNumber.setText("60")

		self.OutOfQuestionLabel = QtWidgets.QLabel(self.TopWidget)
		self.OutOfQuestionLabel.setGeometry(1000, 10, 42, 30)
		self.OutOfQuestionLabel.setFont(font)
		self.OutOfQuestionLabel.setText("/60")

		self.OutOfQuestionLabel = QtWidgets.QLabel(self.TopWidget)
		self.OutOfQuestionLabel.setGeometry(1000, 10, 42, 30)
		self.OutOfQuestionLabel.setFont(font)

		font.setPointSize(12)
		self.StudentNicknameLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentNicknameLabel.setGeometry(300, 50, 160, 20)
		self.StudentNicknameLabel.setFont(font)
		self.StudentNicknameLabel.setText("Nickname")

		self.StudentNumberLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentNumberLabel.setGeometry(300, 28, 70, 16)
		self.StudentNumberLabel.setFont(font)
		self.StudentNumberLabel.setText("Num")

		self.StudentNameLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentNameLabel.setGeometry(300, 74, 260, 20)
		self.StudentNameLabel.setFont(font)
		self.StudentNameLabel.setText("Full Name")

		self.StartTimelabel = QtWidgets.QLabel(self)
		self.StartTimelabel.setGeometry(10, 860, 93, 30)
		self.StartTimelabel.setFont(font)
		self.StartTimelabel.setText("Start Time:")

		self.EndTimelabel = QtWidgets.QLabel(self)
		self.EndTimelabel.setGeometry(210, 860, 93, 30)
		self.EndTimelabel.setFont(font)
		self.EndTimelabel.setText("End Time:")

		font.setPointSize(20)
		self.Questions = QtWidgets.QLabel(self)
		self.Questions.setGeometry(10, 116, 612, 314)
		self.Questions.setFont(font)
		self.Questions.setFrameShape(QtWidgets.QFrame.Panel)
		self.Questions.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Questions.setAlignment(QtCore.Qt.AlignTop)
		self.Questions.setWordWrap(True)
		self.Questions.setText("Questions")

		self.AnswerTextA = QtWidgets.QLabel(self.AnswerATab)
		self.AnswerTextA.setGeometry(330, 10, 830, 340)
		self.AnswerTextA.setFont(font)
		self.AnswerTextA.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextA.setWordWrap(True)
		self.AnswerTextA.setText("TextLabel")

		self.AnswerTextB = QtWidgets.QLabel(self.AnswerBTab)
		self.AnswerTextB.setGeometry(330, 10, 830, 340)
		self.AnswerTextB.setFont(font)
		self.AnswerTextB.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextB.setWordWrap(True)
		self.AnswerTextB.setText("TextLabel")

		self.AnswerTextC = QtWidgets.QLabel(self.AnswerCTab)
		self.AnswerTextC.setGeometry(330, 10, 830, 340)
		self.AnswerTextC.setFont(font)
		self.AnswerTextC.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextC.setWordWrap(True)
		self.AnswerTextC.setText("TextLabel")

		self.AnswerTextD = QtWidgets.QLabel(self.AnswerDTab)
		self.AnswerTextD.setGeometry(330, 10, 830, 340)
		self.AnswerTextD.setFont(font)
		self.AnswerTextD.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextD.setWordWrap(True)
		self.AnswerTextD.setText("TextLabel")

	def add_checkboxes(self):
 		self.AnswerACheckBox = QtWidgets.QCheckBox(self.frame)
 		self.AnswerACheckBox.setGeometry(30, 14, 20, 20)
 		self.AnswerButtonGroup.addButton(self.AnswerACheckBox)

 		self.AnswerBCheckBox = QtWidgets.QCheckBox(self.frame)
 		self.AnswerBCheckBox.setGeometry(80, 14, 20, 20)
 		self.AnswerButtonGroup.addButton(self.AnswerBCheckBox)

 		self.AnswerCCheckBox = QtWidgets.QCheckBox(self.frame)
 		self.AnswerCCheckBox.setGeometry(130, 14, 20, 20)
 		self.AnswerButtonGroup.addButton(self.AnswerCCheckBox)

 		self.AnswerDCheckBox = QtWidgets.QCheckBox(self.frame)
 		self.AnswerDCheckBox.setGeometry(180, 14, 20, 20)
 		self.AnswerButtonGroup.addButton(self.AnswerDCheckBox)

 		self.FalsecheckBox = QtWidgets.QCheckBox(self.frame)
 		self.FalsecheckBox.setGeometry(210, 10, 70, 17)
 		self.FalsecheckBox.setFocusPolicy(QtCore.Qt.NoFocus)
 		self.AnswerButtonGroup.addButton(self.FalsecheckBox)

	def add_buttons(self):
		bfont = QtGui.QFont()
		bfont.setPointSize(12)
		bfont.setBold(True)
		bfont.setItalic(True)
		self.BackButton = QtWidgets.QPushButton(self.frame)
		self.BackButton.setGeometry(898, 6, 130, 32)
		self.BackButton.setFont(bfont)
		self.BackButton.setText("       Back")
		self.BackButton.setIcon(QtGui.QIcon("img/back_button.png"))
		self.BackButton.setIconSize(QtCore.QSize(32,32))

		self.ForwardButton = QtWidgets.QPushButton(self.frame)
		self.ForwardButton.setGeometry(1036, 6, 130, 32)
		self.ForwardButton.setFont(bfont)
		self.ForwardButton.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.ForwardButton.setText("         Next")
		self.ForwardButton.setIcon(QtGui.QIcon("img/forward_button.png"))
		self.ForwardButton.setIconSize(QtCore.QSize(32,32))

		self.LogoutButton = QtWidgets.QPushButton(self)
		self.LogoutButton.setGeometry(1074, 860, 110, 30)
		self.LogoutButton.setFont(bfont)
		self.LogoutButton.setText("Log Out")

	def add_scrollbars(self):
		self.TimeLeftProgressBar = QtWidgets.QProgressBar(self)
		self.TimeLeftProgressBar.setGeometry(390, 864, 580, 23)
		self.TimeLeftProgressBar.setTextVisible(False)
		#self.TimeLeftProgressBar.setMaximum(50)
		#self.TimeLeftProgressBar.setProperty("value", 46)

	def tool_status_tips(self):
		self.LogoutButton.setStatusTip("Click to Log out user.")
		self.TimeLeftProgressBar.setStatusTip("Your time left")
		self.StartTime.setStatusTip("Time exam started")
		self.StartTimelabel.setStatusTip("Time exam started")
		self.MinLeftLabel.setStatusTip("How many minuets you have left")
		self.EndTime.setStatusTip("Exam finish time")
		self.EndTimelabel.setStatusTip("Exam finish time")
		self.tabWidget.setStatusTip("Click to view possible answers.")
		self.AnswerACheckBox.setStatusTip("Click to choose Answer A.")
		self.AnswerBCheckBox.setStatusTip("Click to choose Answer B.")
		self.AnswerCCheckBox.setStatusTip("Click to choose Answer C.")
		self.AnswerDCheckBox.setStatusTip("Click to choose Answer D.")
		self.ForwardButton.setStatusTip("Click to go to the next question.")

	def tab_order(self):
		self.tabWidget.setCurrentIndex(0)
		self.setTabOrder(self.tabWidget, self.AnswerACheckBox)
		self.setTabOrder(self.AnswerACheckBox, self.AnswerBCheckBox)
		self.setTabOrder(self.AnswerBCheckBox, self.AnswerCCheckBox)
		self.setTabOrder(self.AnswerCCheckBox, self.AnswerDCheckBox)
		self.setTabOrder(self.AnswerDCheckBox, self.ForwardButton)
		self.setTabOrder(self.ForwardButton, self.LogoutButton)
		self.setTabOrder(self.LogoutButton, self.BackButton)

	def kb_shortcuts(self):
		self.LogoutButton.setShortcut("Esc")
		self.AnswerACheckBox.setShortcut("A")
		self.AnswerBCheckBox.setShortcut("B")
		self.AnswerCCheckBox.setShortcut("C")
		self.AnswerDCheckBox.setShortcut("D")
		self.BackButton.setShortcut("Left")
		self.ForwardButton.setShortcut("Return")

# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	main_app = Ui_ExamLogin()
# 	main_app.show()

# sys.exit(app.exec_())


# Copyright (c) 2019 Steven Walden
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.