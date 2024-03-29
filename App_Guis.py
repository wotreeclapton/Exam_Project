'''Exam app Guis developed by Mr Steven J Walden
    Dec. 2019-2020
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
		self.resize(588, 280)
		self.setMinimumSize(588, 280)
		self.setMaximumSize(588, 280)
		self.setWindowIcon(QtGui.QIcon("img/Ep_window_icon.ico"))
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
		self.ClassLabel.setGeometry(180, 5, 300, 60)#10, 10, 300, 60
		font = QtGui.QFont()
		font.setPointSize(30)
		font.setBold(True)
		font.setItalic(True)
		#font.setWeight(75)
		self.ClassLabel.setFont(font)
		self.ClassLabel.setText("Class")
		#Add label for exam choice combobox
		self.ExamChoiceLabel = QtWidgets.QLabel("Choose your exam", self)
		self.ExamChoiceLabel.setGeometry(15, 54, 180, 16)
		#Add label for student name combobox
		self.EnterNameLabel = QtWidgets.QLabel("Choose your name from the list below", self)
		self.EnterNameLabel.setGeometry(15, 114, 211, 16)
		#Label for password box
		self.InputPaswordLabel = QtWidgets.QLabel("Password", self)
		self.InputPaswordLabel.setGeometry(15, 172, 131, 16)
		#Display school logo
		self.Logolabel = QtWidgets.QLabel(self)
		self.Logolabel.setGeometry(320, 20, 75, 97)
		self.Logolabel.setPixmap(QtGui.QPixmap("img/School logo75x97_light.png"))
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
		self.StudentPhoto.setGeometry(414, 30, 160, 192)
		self.StudentPhoto.setFrameShape(QtWidgets.QFrame.Panel)
		self.StudentPhoto.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.StudentPhoto.setPixmap(QtGui.QPixmap("img/blank_girl.png"))

	def add_textboxes(self):
		#Textbox input for password
		self.InputPassword = QtWidgets.QLineEdit(self)
		self.InputPassword.setGeometry(10, 200, 221, 20)
		self.InputPassword.setEchoMode(QtWidgets.QLineEdit.Password)

	def add_buttons(self):
		bfont = QtGui.QFont()
		bfont.setPointSize(8)
		# bfont.setBold(True)
		bfont.setItalic(True)
		#Button box setup for OKay and cancel buttons
		self.buttonBox = QtWidgets.QDialogButtonBox(self)
		self.buttonBox.setGeometry(418, 236, 156, 23)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		#Button for showing the password temporarily
		self.PasswordShowButton = QtWidgets.QPushButton(self)
		self.PasswordShowButton.setGeometry(211, 201, 20, 18)
		self.PasswordShowButton.setFocusPolicy(QtCore.Qt.NoFocus)
		self.PasswordShowButton.setIcon(QtGui.QIcon("img/Password_Icon_20x20_light.png"))
		self.PasswordShowButton.setIconSize(QtCore.QSize(20, 18))
		self.PasswordShowButton.setCheckable(False)
		self.PasswordShowButton.setAutoRepeat(True)
		self.PasswordShowButton.setAutoRepeatDelay(200)
		#Button for switchiong to darkmode
		self.DarkModeButton = QtWidgets.QPushButton(self)
		self.DarkModeButton.setGeometry(534, 5, 40, 20)
		self.DarkModeButton.setFocusPolicy(QtCore.Qt.NoFocus)		
		self.DarkModeButton.setCheckable(True)
		self.DarkModeButton.setFont(bfont)
		self.DarkModeButton.setText("Dark")

	def add_comboboxes(self):
		#Combobox setup to choose the class
		self.ClassCmb = QtWidgets.QComboBox(self)
		self.ClassCmb.setGeometry(10, 20, 140, 22)#10, 80, 151, 22
		#Combox set to choose the student
		self.StudentNameCmb = QtWidgets.QComboBox(self)
		self.StudentNameCmb.setGeometry(10, 140, 391, 22)
		#Combox setup to choose the exam
		self.ExamChoiceCmb = QtWidgets.QComboBox(self)
		self.ExamChoiceCmb.setGeometry(10, 80, 151, 22)

	def tool_status_tips(self):
		#Setup any tool and status bar tips
		self.StudentNameCmb.setToolTip("Click arrow to choose your name!")
		self.ClassCmb.setToolTip("Choose your class!")
		self.InputPassword.setToolTip("Password goes here!")

		self.StudentNameCmb.setStatusTip("Choose a name")
		self.InputPassword.setStatusTip("Input your password")
		self.ClassCmb.setStatusTip("Choose your class first")
		self.ExamChoiceCmb.setStatusTip("Choose your exam")

	def tab_order(self):
		self.setTabOrder(self.ClassCmb, self.ExamChoiceCmb)
		self.setTabOrder(self.ExamChoiceCmb, self.StudentNameCmb)
		self.setTabOrder(self.StudentNameCmb, self.InputPassword)
		self.setTabOrder(self.InputPassword, self.PasswordShowButton)
		self.setTabOrder(self.PasswordShowButton, self.DarkModeButton)


class Ui_ExamQuestions(QtWidgets.QMainWindow):
	"""docstrbing for MyApp"""
	def __init__(self, screen_size, parent=None):
		super(Ui_ExamQuestions, self).__init__(parent)
		self.screen_height = screen_size.height()
		self.screen_width = round((self.screen_height - 32) * 1.3)
		# self.screen_height = screen_size[1]
		# self.screen_width = round((self.screen_height - 32) * 1.3)
		#print("Ori W=1200 New W={} Ori H=924 New W={}".format(self.screen_width,self.screen_height))
		self.initUI()

	def initUI(self):
		self.resize(self.screen_width, self.screen_height - 32)
		self.setMinimumSize(800, 600) # orig size was 1200x924
		self.setMaximumSize(1200, self.screen_height - 32)
		self.setWindowIcon(QtGui.QIcon("img/Ep_window_icon.ico"))
		self.setWindowTitle("Exam Questions")

		self.add_widgets()
		self.add_layouts()
		self.add_labels()
		self.add_checkboxes()
		self.add_buttons()
		self.tool_status_tips()
		self.tab_order()
		self.kb_shortcuts()

	def add_widgets(self):
		self.centralwidget = QtWidgets.QWidget(self)

		self.MainVerticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

		self.TopWidget = QtWidgets.QFrame(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		self.TopWidget.setSizePolicy(sizePolicy)
		self.TopWidget.setMinimumWidth(600)
		self.TopWidget.setMinimumHeight(103)
		self.TopWidget.setMaximumHeight(103)

		self.TopWidget1 = QtWidgets.QFrame(self.centralwidget)
		self.TopWidget1.setSizePolicy(sizePolicy)
		self.TopWidget1.setMinimumWidth(1)
		self.TopWidget1.setMinimumHeight(103)
		self.TopWidget1.setMaximumHeight(103)

		self.TopWidget2 = QtWidgets.QFrame(self.centralwidget)
		self.TopWidget2.setSizePolicy(sizePolicy)
		self.TopWidget2.setMinimumWidth(290)
		self.TopWidget2.setMinimumHeight(103)
		self.TopWidget2.setMaximumHeight(103)

		self.videoWidget = QtMultimediaWidgets.QVideoWidget(self.centralwidget)

		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.tabWidget.setFont(font)

		self.AnswerATab = QtWidgets.QWidget()
		self.TabTextLayoutA = QtWidgets.QHBoxLayout(self.AnswerATab)
		self.TabTextLayoutA.setContentsMargins(330, -1, -1, -1)
		self.tabWidget.addTab(self.AnswerATab, "Answer-A")

		self.AnswerBTab = QtWidgets.QWidget()
		self.TabTextLayoutB = QtWidgets.QHBoxLayout(self.AnswerBTab)
		self.TabTextLayoutB.setContentsMargins(330, -1, -1, -1)		
		self.tabWidget.addTab(self.AnswerBTab, "Answer-B")

		self.AnswerCTab = QtWidgets.QWidget()
		self.TabTextLayoutC = QtWidgets.QHBoxLayout(self.AnswerCTab)
		self.TabTextLayoutC.setContentsMargins(330, -1, -1, -1)
		self.tabWidget.addTab(self.AnswerCTab, "Answer-C")

		self.AnswerDTab = QtWidgets.QWidget()
		self.TabTextLayoutD = QtWidgets.QHBoxLayout(self.AnswerDTab)
		self.TabTextLayoutD.setContentsMargins(330, -1, -1, -1)
		self.tabWidget.addTab(self.AnswerDTab, "Answer-D")

		self.CheckboxFrame = QtWidgets.QFrame(self.centralwidget)
		self.CheckboxFrame.setSizePolicy(sizePolicy)
		self.CheckboxFrame.setMinimumWidth(600)
		self.CheckboxFrame.setMinimumHeight(46)
		self.CheckboxFrame.setMaximumHeight(46)

		self.CheckboxFrame1 = QtWidgets.QFrame(self.centralwidget)
		self.CheckboxFrame1.setSizePolicy(sizePolicy)
		self.CheckboxFrame1.setMinimumWidth(1)
		self.CheckboxFrame1.setMinimumHeight(46)
		self.CheckboxFrame1.setMaximumHeight(46)

		self.CheckboxFrame2 = QtWidgets.QFrame(self.centralwidget)
		self.CheckboxFrame2.setSizePolicy(sizePolicy)
		self.CheckboxFrame2.setMinimumWidth(278)
		self.CheckboxFrame2.setMinimumHeight(46)
		self.CheckboxFrame2.setMaximumHeight(46)


		self.BottomFrame = QtWidgets.QFrame(self.centralwidget)
		self.BottomFrame.setSizePolicy(sizePolicy)
		self.BottomFrame.setMinimumWidth(390)
		self.BottomFrame.setMaximumWidth(390)
		self.BottomFrame.setMinimumHeight(38)
		self.BottomFrame.setMaximumHeight(38)

		self.BottomFrame2 = QtWidgets.QFrame(self.centralwidget)
		self.BottomFrame2.setSizePolicy(sizePolicy)
		self.BottomFrame2.setMinimumWidth(240)
		self.BottomFrame2.setMaximumWidth(240)
		self.BottomFrame2.setMinimumHeight(38)
		self.BottomFrame2.setMaximumHeight(38)

		self.AnswerButtonGroup = QtWidgets.QButtonGroup(self.centralwidget)

		self.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(self.centralwidget)

	def add_layouts(self):
		self.TopLayout = QtWidgets.QHBoxLayout()
		self.MainVerticalLayout.addLayout(self.TopLayout)
		self.TopLayout.addWidget(self.TopWidget)
		self.TopLayout.addWidget(self.TopWidget1)
		self.TopLayout.addWidget(self.TopWidget2)
		# self.MainVerticalLayout.addWidget(self.TopWidget)
		self.QuestionsAndVideoLayoutLayout = QtWidgets.QHBoxLayout()
		self.MainVerticalLayout.addLayout(self.QuestionsAndVideoLayoutLayout)

		self.MainVerticalLayout.addWidget(self.tabWidget)


		#add a layout to the checkbox frame
		self.CheckBoxLayout = QtWidgets.QHBoxLayout()
		self.MainVerticalLayout.addLayout(self.CheckBoxLayout)

		self.CheckBoxLayout.addWidget(self.CheckboxFrame)
		self.CheckBoxLayout.addWidget(self.CheckboxFrame1)
		self.CheckBoxLayout.addWidget(self.CheckboxFrame2)

		self.BottomLayout = QtWidgets.QHBoxLayout()
		self.MainVerticalLayout.addLayout(self.BottomLayout)
		self.BottomLayout.addWidget(self.BottomFrame)
		#create scroll bar and add to the bottom layout
		self.add_scrollbars()
		self.BottomLayout.addWidget(self.TimeLeftProgressBar)
		self.BottomLayout.addWidget(self.BottomFrame2)

		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
		self.mediaPlayer.setVideoOutput(self.videoWidget)

		self.setStatusBar(self.statusbar)

	def add_labels(self):
		self.SchoolLabel = QtWidgets.QLabel(self.TopWidget)
		self.SchoolLabel.setMinimumSize(QtCore.QSize(75, 97))
		self.SchoolLabel.setGeometry(4, 4, 75, 97)
		self.SchoolLabel.setPixmap(QtGui.QPixmap("img/School logo75x97_light.png"))

		self.StudentPhotoLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentPhotoLabel.setGeometry(285, 4, 75, 90)
		self.StudentPhotoLabel.setPixmap(QtGui.QPixmap("img/blank_girl.png"))
		self.StudentPhotoLabel.setScaledContents(True)

		self.ArrowLabel = QtWidgets.QLabel(self.CheckboxFrame)
		self.ArrowLabel.setGeometry(244, 8, 60, 30)
		self.ArrowLabel.setPixmap(QtGui.QPixmap("img/Left_Arrow.png"))

		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		self.ExamTitle = QtWidgets.QLabel(self.TopWidget)
		self.ExamTitle.setGeometry(95, 10, 201, 71)
		self.ExamTitle.setText("Just testing")
		self.ExamTitle.setFont(font)
		self.ExamTitle.setAlignment(QtCore.Qt.AlignTop)

		font.setPointSize(15)
		self.Alabel = QtWidgets.QLabel(self.CheckboxFrame)
		self.Alabel.setGeometry(4, 9, 26, 26)
		self.Alabel.setFont(font)
		self.Alabel.setAlignment(QtCore.Qt.AlignCenter)
		self.Alabel.setText("A")

		self.Blabel = QtWidgets.QLabel(self.CheckboxFrame)
		self.Blabel.setGeometry(54, 9, 26, 26)
		self.Blabel.setFont(font)
		self.Blabel.setAlignment(QtCore.Qt.AlignCenter)
		self.Blabel.setText("B")

		self.Clabel = QtWidgets.QLabel(self.CheckboxFrame)
		self.Clabel.setGeometry(104, 9, 26, 26)
		self.Clabel.setFont(font)
		self.Clabel.setAlignment(QtCore.Qt.AlignCenter)
		self.Clabel.setText("C")

		self.Dlabel = QtWidgets.QLabel(self.CheckboxFrame)
		self.Dlabel.setGeometry(154, 9, 26, 26)
		self.Dlabel.setFont(font)
		self.Dlabel.setAlignment(QtCore.Qt.AlignCenter)
		self.Dlabel.setText("D")

		font.setPointSize(10)
		self.StartTime = QtWidgets.QLabel(self.BottomFrame)
		self.StartTime.setGeometry(110, 5, 90, 30)
		self.StartTime.setFont(font)
		self.StartTime.setText("Time")

		self.EndTime = QtWidgets.QLabel(self.BottomFrame)
		self.EndTime.setGeometry(310, 5, 71, 30)
		self.EndTime.setFont(font)
		self.EndTime.setText("Time")

		self.MinLeftLabel = QtWidgets.QLabel(self.BottomFrame2)
		self.MinLeftLabel.setGeometry(10, 5, 101, 30)
		self.MinLeftLabel.setFont(font)
		self.MinLeftLabel.setText("Mins Left")

		font.setPointSize(16)
		font.setItalic(True)
		self.MsgLabel = QtWidgets.QLabel(self.CheckboxFrame)
		self.MsgLabel.setGeometry(328, 7, 1000, 32)
		self.MsgLabel.setFont(font)
		self.MsgLabel.setText("Please choose an answer")

		font.setPointSize(14)
		self.ClassLabel = QtWidgets.QLabel(self.TopWidget)
		self.ClassLabel.setGeometry(385, 4, 90, 16)
		self.ClassLabel.setFont(font)
		self.ClassLabel.setText("Class")

		self.QuestionNumberLabel = QtWidgets.QLabel(self.TopWidget2)
		self.QuestionNumberLabel.setGeometry(10, 30, 186, 30)
		self.QuestionNumberLabel.setFont(font)
		self.QuestionNumberLabel.setText("Question Number:")

		self.QuestionNumber = QtWidgets.QLabel(self.TopWidget2)
		self.QuestionNumber.setGeometry(196, 30, 30, 30)
		self.QuestionNumber.setFont(font)
		self.QuestionNumber.setText("60")

		self.OutOfQuestionLabel = QtWidgets.QLabel(self.TopWidget2)
		self.OutOfQuestionLabel.setGeometry(226, 30, 42, 30)
		self.OutOfQuestionLabel.setFont(font)
		self.OutOfQuestionLabel.setText("/60")

		font.setPointSize(12)
		self.StudentNicknameLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentNicknameLabel.setGeometry(385, 50, 160, 20)
		self.StudentNicknameLabel.setFont(font)
		self.StudentNicknameLabel.setText("Nickname")

		self.StudentNumberLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentNumberLabel.setGeometry(385, 28, 70, 16)
		self.StudentNumberLabel.setFont(font)
		self.StudentNumberLabel.setText("Num")

		self.StudentNameLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentNameLabel.setGeometry(385, 74, 260, 20)
		self.StudentNameLabel.setFont(font)
		self.StudentNameLabel.setText("Full Name")

		self.StartTimelabel = QtWidgets.QLabel(self.BottomFrame)
		self.StartTimelabel.setGeometry(10, 5, 93, 30)
		self.StartTimelabel.setFont(font)
		self.StartTimelabel.setText("Start Time:")

		self.EndTimelabel = QtWidgets.QLabel(self.BottomFrame)
		self.EndTimelabel.setGeometry(210, 5, 93, 30)
		self.EndTimelabel.setFont(font)
		self.EndTimelabel.setText("End Time:")

		font.setPointSize(20)
		self.Questions = QtWidgets.QLabel(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHeightForWidth(self.Questions.sizePolicy().hasHeightForWidth())
		self.Questions.setSizePolicy(sizePolicy)
		self.Questions.setFont(font)
		self.Questions.setFrameShape(QtWidgets.QFrame.Panel)
		self.Questions.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Questions.setAlignment(QtCore.Qt.AlignTop)
		self.Questions.setWordWrap(True)
		self.Questions.setText("Questions")
		self.QuestionsAndVideoLayoutLayout.addWidget(self.Questions)

		self.QuestionsAndVideoLayoutLayout.addWidget(self.videoWidget)

		self.AnswerTextA = QtWidgets.QLabel(self.AnswerATab)
		self.AnswerTextA.setFont(font)
		self.AnswerTextA.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextA.setWordWrap(True)
		self.AnswerTextA.setText("TextLabel")
		self.TabTextLayoutA.addWidget(self.AnswerTextA)

		self.AnswerTextB = QtWidgets.QLabel(self.AnswerBTab)
		self.AnswerTextB.setFont(font)
		self.AnswerTextB.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextB.setWordWrap(True)
		self.AnswerTextB.setText("TextLabel")
		self.TabTextLayoutB.addWidget(self.AnswerTextB)

		self.AnswerTextC = QtWidgets.QLabel(self.AnswerCTab)
		self.AnswerTextC.setFont(font)
		self.AnswerTextC.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextC.setWordWrap(True)
		self.AnswerTextC.setText("TextLabel")
		self.TabTextLayoutC.addWidget(self.AnswerTextC)

		self.AnswerTextD = QtWidgets.QLabel(self.AnswerDTab)
		self.AnswerTextD.setFont(font)
		self.AnswerTextD.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextD.setWordWrap(True)
		self.AnswerTextD.setText("TextLabel")
		self.TabTextLayoutD.addWidget(self.AnswerTextD)

	def add_checkboxes(self):
		self.AnswerACheckBox = QtWidgets.QCheckBox(self.CheckboxFrame)
		self.AnswerACheckBox.setGeometry(30, 14, 20, 20)
		self.AnswerButtonGroup.addButton(self.AnswerACheckBox)

		self.AnswerBCheckBox = QtWidgets.QCheckBox(self.CheckboxFrame)
		self.AnswerBCheckBox.setGeometry(80, 14, 20, 20)
		self.AnswerButtonGroup.addButton(self.AnswerBCheckBox)

		self.AnswerCCheckBox = QtWidgets.QCheckBox(self.CheckboxFrame)
		self.AnswerCCheckBox.setGeometry(130, 14, 20, 20)
		self.AnswerButtonGroup.addButton(self.AnswerCCheckBox)

		self.AnswerDCheckBox = QtWidgets.QCheckBox(self.CheckboxFrame)
		self.AnswerDCheckBox.setGeometry(180, 14, 20, 20)
		self.AnswerButtonGroup.addButton(self.AnswerDCheckBox)

		self.FalsecheckBox = QtWidgets.QCheckBox(self.CheckboxFrame)
		self.FalsecheckBox.setGeometry(210, 10, 70, 17)
		self.FalsecheckBox.setFocusPolicy(QtCore.Qt.NoFocus)
		self.AnswerButtonGroup.addButton(self.FalsecheckBox)

	def add_buttons(self):
		bfont = QtGui.QFont()
		bfont.setPointSize(12)
		bfont.setBold(True)
		bfont.setItalic(True)
		self.BackButton = QtWidgets.QPushButton(self.CheckboxFrame2)
		self.BackButton.setGeometry(10, 6, 130, 32)
		self.BackButton.setFont(bfont)
		self.BackButton.setText("       Back")
		self.BackButton.setIcon(QtGui.QIcon("img/back_button.png"))
		self.BackButton.setIconSize(QtCore.QSize(32,32))

		self.ForwardButton = QtWidgets.QPushButton(self.CheckboxFrame2)
		self.ForwardButton.setGeometry(142, 6, 130, 32)
		self.ForwardButton.setFont(bfont)
		self.ForwardButton.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.ForwardButton.setText("         Next")
		self.ForwardButton.setIcon(QtGui.QIcon("img/forward_button.png"))
		self.ForwardButton.setIconSize(QtCore.QSize(32,32))

		self.LogoutButton = QtWidgets.QPushButton(self.BottomFrame2)
		self.LogoutButton.setGeometry(120, 5, 110, 30)
		self.LogoutButton.setFont(bfont)
		self.LogoutButton.setText("Log Out")

		bfont = QtGui.QFont()
		bfont.setPointSize(8)
		bfont.setItalic(True)
		#Button for switchiong to darkmode
		self.DarkModeButton = QtWidgets.QPushButton(self.TopWidget2)
		self.DarkModeButton.setGeometry(226, 5, 40, 20)
		self.DarkModeButton.setFocusPolicy(QtCore.Qt.NoFocus)		
		self.DarkModeButton.setCheckable(True)
		self.DarkModeButton.setFont(bfont)
		self.DarkModeButton.setText("Dark")

	def add_scrollbars(self):
		self.TimeLeftProgressBar = QtWidgets.QProgressBar()
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		self.TimeLeftProgressBar.setSizePolicy(sizePolicy)
		self.TimeLeftProgressBar.setMinimumWidth(100)
		self.TimeLeftProgressBar.setMinimumHeight(23)
		self.TimeLeftProgressBar.setMaximumHeight(23)
		self.TimeLeftProgressBar.setTextVisible(False)

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

class Ui_StartupWindow(QtWidgets.QMainWindow):
	"""docstring for Ui_AboutWindow"""
	def __init__(self, parent=None):
		super(Ui_StartupWindow, self).__init__(parent)
		self.resize(320, 360)
		self.setMinimumSize(320, 360)
		self.setMaximumSize(320, 360)
		self.setWindowIcon(QtGui.QIcon("img/Ep_window_icon.ico"))
		self.setWindowFlags(QtCore.Qt.WindowTransparentForInput)

		self.add_labels()

	def add_labels(self):
		self.AppLogo = QtWidgets.QLabel(self)
		self.AppLogo.setMinimumSize(QtCore.QSize(162, 162))
		self.AppLogo.setGeometry(int(self.geometry().width()/2 - self.AppLogo.width() / 2), 16, 160, 160)
		self.AppLogo.setPixmap(QtGui.QPixmap("img/Ep logo160x160.png"))
		self.AppLogo.setAlignment(QtCore.Qt.AlignCenter)

		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		self.AppName = QtWidgets.QLabel(self)
		self.AppName.setMinimumSize(QtCore.QSize(180, 50))
		self.AppName.setGeometry(int(self.geometry().width()/2 - self.AppName.width() / 2), 184, 160, 50)
		self.AppName.setText("Exam Application")
		self.AppName.setFont(font)
		self.AppName.setAlignment(QtCore.Qt.AlignCenter)

		font.setPointSize(12)
		font.setBold(False)
		self.VersionLabel = QtWidgets.QLabel(self)
		self.VersionLabel.setMinimumSize(QtCore.QSize(160, 50))
		self.VersionLabel.setGeometry(int(self.geometry().width()/2 - self.VersionLabel.width() / 2), 214, 120, 50)
		self.VersionLabel.setText("Loading please wait!")
		self.VersionLabel.setFont(font)
		self.VersionLabel.setAlignment(QtCore.Qt.AlignCenter)

		font.setPointSize(11)
		self.CopyrightLabel = QtWidgets.QLabel(self)
		self.CopyrightLabel.setMinimumSize(QtCore.QSize(280, 50))
		self.CopyrightLabel.setGeometry(int(self.geometry().width()/2 - self.CopyrightLabel.width() / 2), 260, 280, 50)
		self.CopyrightLabel.setText("Copyright 2020 Mr Steven J Walden.")
		self.CopyrightLabel.setFont(font)
		self.CopyrightLabel.setAlignment(QtCore.Qt.AlignCenter)

		font.setPointSize(10)
		self.RightsLabel = QtWidgets.QLabel(self)
		self.RightsLabel.setMinimumSize(QtCore.QSize(120, 50))
		self.RightsLabel.setGeometry(int(self.geometry().width()/2 - self.RightsLabel.width() / 2), 290, 120, 50)
		self.RightsLabel.setText("All rights reserved.")
		self.RightsLabel.setFont(font)
		self.RightsLabel.setAlignment(QtCore.Qt.AlignCenter)

# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	main_app = Ui_ExamLogin()
# 	# main_app = Ui_ExamQuestions(screen_size=(1920,1080))
# 	# main_app = Ui_StartupWindow()
# 	main_app.show()

# sys.exit(app.exec_())


# Copyright (c) 2019-2020 Steven Walden
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