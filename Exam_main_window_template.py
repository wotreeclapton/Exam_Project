'''
Exam main window Gui developed by Mr Steven J Walden
    Dec. 2019
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license at end of file]
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaPlayer
#from PyQt5.QtWidgets import QWidget

class Ui_ExamQuestions(QtWidgets.QMainWindow):
	"""docstrbing for MyApp"""
	def __init__(self, parent=None):
		super(Ui_ExamQuestions, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.resize(1200, 944)
		self.setMinimumSize(1200, 944)
		self.setMaximumSize(1200, 944)
		self.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
		self.setWindowTitle("Exam Questions")

		self.add_widgets()
		self.add_layouts()
		self.add_labels()
		self.add_textboxes()
		self.add_buttons()
		self.add_comboboxes()
		self.tool_status_tips()
		self.tab_order()

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

	def add_layouts(self):
		self.verticalLayoutWidget = QtWidgets.QWidget(self)
		self.verticalLayoutWidget.setGeometry(630, 120, 551, 311)
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)

		self.verticalLayout.addWidget(self.videoWidget)
		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
		self.mediaPlayer.setVideoOutput(self.videoWidget)

	def add_labels(self):
		self.SchoolLabel = QtWidgets.QLabel(self)
		self.SchoolLabel.setGeometry(10, 10, 75, 97)
		self.SchoolLabel.setPixmap(QtGui.QPixmap("img/School logo75x97_grad.png"))

		self.StudentPhotoLabel = QtWidgets.QLabel(self.TopWidget)
		self.StudentPhotoLabel.setGeometry(200, 4, 75, 90)
		self.StudentPhotoLabel.setPixmap(QtGui.QPixmap("img/blank_girl.png"))
		self.StudentPhotoLabel.setScaledContents(True)

		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		self.ExamTitle = QtWidgets.QLabel(self.TopWidget)
		self.ExamTitle.setGeometry(10, 10, 201, 71)
		self.ExamTitle.setFont(font)
		self.ExamTitle.setAlignment(QtCore.Qt.AlignTop)
		self.ExamTitle.setText("C21202\n""Midterm Exam ")

		font.setPointSize(14)
		font.setItalic(True)
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

	def add_textboxes(self):
		pass

	def add_buttons(self):
		pass

	def add_comboboxes(self):
		pass

	def tool_status_tips(self):
		pass

	def tab_order(self):
		pass


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main_app = Ui_ExamQuestions()
	main_app.show()


sys.exit(app.exec_())

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