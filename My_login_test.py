'''
Exam Login Gui developed by Mr Steven J Walden
    Dec. 2019
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license at end of file]
'''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
#from PyQt5.QtWidgets import QWidget

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
		self.setWindowTitle("Exam Login")

		self.statusbar = QtWidgets.QStatusBar(self)
		self.statusbar.setSizeGripEnabled(False)
		self.setStatusBar(self.statusbar)

		self.add_labels()
		self.add_textboxes()
		self.add_buttons()
		self.add_comboboxes()
		self.tool_status_tips()

	def add_labels(self):
		#Add Label for displaying the class name
		self.ClassLabel = QtWidgets.QLabel("Class", self)
		self.ClassLabel.setGeometry(10, 10, 300, 60)
		font = QtGui.QFont()
		font.setPointSize(30)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
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
		font.setWeight(75)
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

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main_app = Ui_ExamLogin()
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