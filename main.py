'''
EXAM APPLICATION LAUNCHER developed by Mr Steven J walden
    Nov. 2019
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license at end of file]

'''

#!/usr/bin/env python

__author__ = 'Steven Walden'
__version__ = '1.0'

import os
import sys
import csv

from Student_Login_Gui import Ui_ExamLogin
from Exam_main_window import Ui_ExamQuestions
from settings import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox #, QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt


# QT_VER = Qt.__binding__
# PY_VER = sys.version[:3]

class App(QtWidgets.QWidget):
	"""docstring for App"""
	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		#setup app windows and theme
		
		self.dark_theme()

		self.load_data()
		self.open_login_window()
		

	def load_data(self):
		self.class_list = ['Choose your class','M1/1','M2/1','M3/1']
		self.string_convert = {'A':1,'B':2,'C':3,'D':4}
		self.student_names, self.student_nicknames, self.student_passwords, = [], [], []
		self.exam_questions, self.exam_AnswerA, self.exam_AnswerB, self.exam_AnswerC, self.exam_AnswerD, self.exam_Rightanswer = [],[],[],[],[],[]
		self.question_list1 = {1:['In Python what is a list?', 'A block of code.', 'A variable.', 'A list of strings or variables.', 'A shopping list.', 'C'],2:['What does turtle.speed(10) do?','Closes the turtle.','Opens the turtle.','Sets the turtle speed.','Changes the turtle colour.','C'],3:['Python is what type of programming language?','SQL.','Visual Basic.','Script.','Machine.','C']}

		self.score = 0
		self.answer = 0
		self.question_number = 1
		self.admin = False
		
	def dark_theme(self):
		app.setStyle("Fusion")

		self.dark_palette = QPalette()

		self.dark_palette.setColor(QPalette.Window,QColor(53,53,53))
		self.dark_palette.setColor(QPalette.WindowText, Qt.white)
		self.dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
		self.dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
		self.dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
		self.dark_palette.setColor(QPalette.ToolTipText, Qt.white)
		self.dark_palette.setColor(QPalette.Text, Qt.white)
		self.dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
		self.dark_palette.setColor(QPalette.ButtonText, Qt.white)
		self.dark_palette.setColor(QPalette.BrightText, Qt.red)
		self.dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
		self.dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
		self.dark_palette.setColor(QPalette.HighlightedText, Qt.black)

		app.setPalette(self.dark_palette)

		app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

	def screen_location(self, wn):
		ag = QDesktopWidget().availableGeometry()
		sg = QDesktopWidget().screenGeometry()

		self.widget = wn.geometry()
		x = ag.width() / 2 - self.widget.width() / 2
		y = ag.height() / 2 - self.widget.height() / 2
		wn.move(x, y)

	def read_csv(self, clas):
		self.student_names.clear()
		self.student_nicknames.clear()
		self.student_passwords.clear()

		with change_dir('resources'):
			with open('Student_Details_CSV_M' + str(clas) + '-1.csv','r') as csv_file:
				csv_reader = csv.DictReader(csv_file)			

				for line in csv_reader:
					self.student_names.append(line['Name'])
					self.student_nicknames.append(line['Nicknames'])
					self.student_passwords.append(line['Passwords'])

	def open_login_window(self):
		self.examLogin = QtWidgets.QMainWindow()
		self.login_gui = Ui_ExamLogin()

		#Connect button methods from student login gui code
		self.examLogin.login_okaybutton_clicked = self.login_okaybutton_clicked
		self.examLogin.login_cancelbutton_clicked = self.login_cancelbutton_clicked
		self.examLogin.password_show_button_clicked = self.password_show_button_clicked
		self.examLogin.class_name_changed = self.class_name_changed
		self.examLogin.student_name_change = self.student_name_change

		self.login_gui.setupUi(self.examLogin)

		self.screen_location(self.examLogin)

		#populate the combo boxes
		self.login_gui.ClassCmb.addItems(self.class_list)
		#limit the number of items in the student name combo box
		self.login_gui.StudentNameCmb.setStyleSheet("QComboBox { combobox-popup: 0; }")
		self.login_gui.StudentNameCmb.setMaxVisibleItems(10)
		#start with the class combobox 
		self.login_gui.ClassCmb.setFocus()

		self.examLogin.show()

	def login_okaybutton_clicked(self):
		try:
			#open main window and pass vairables		
			self.password_input = self.login_gui.InputPassword.text()
			
			if self.password_input == self.student_passwords[self.student_number]:
				self.examLogin.close()
				self.open_exam_window()
			elif self.student_number == 0:
				pass
				#print('Please choose a student name')
			else:
				self.login_gui.InputPassword.clear()
		except (AttributeError, KeyError):
			pass
			#print('Choose a class',sys.exc_info()[0])

	def password_show_button_clicked(self):
		if self.login_gui.PasswordShowButton.isDown():
		 	self.login_gui.InputPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
		else:
			self.login_gui.InputPassword.setEchoMode(QtWidgets.QLineEdit.Password)

	def class_name_changed(self, cls):
		self.class_name = self.login_gui.ClassCmb.itemText(cls)
		self.year_chosen = cls
		
		if cls > 0:
			self.read_csv(cls)
			self.class_name = self.class_list[cls]
			self.login_gui.ClassLabel.setText(self.class_list[cls])
			self.login_gui.StudentNameCmb.clear()
			self.login_gui.StudentNameCmb.addItems(self.student_names)
		else:
			self.login_gui.ClassLabel.setText('Class')
			self.login_gui.StudentNameCmb.clear()
			self.login_gui.StudentNumber.setText('')
			self.login_gui.StudentNickname.setText('')

	def student_name_change(self, st):
		#links student cmb box with the photo display
		self.student_number = st		

		with change_dir('img'):
			if st > 0:
				self.path_test = path.join('M' + str(self.year_chosen) + '-1', str(st) + '.png')
				if path.exists(self.path_test):
					self.login_gui.StudentPhoto.setPixmap(QtGui.QPixmap(path.join('M' + str(self.year_chosen) + '-1', str(st) + '.png')))
				else:
					self.login_gui.StudentPhoto.setPixmap(QtGui.QPixmap(path.join('blank_girl.png')))

				self.login_gui.StudentNumber.setText(str(st))
				self.login_gui.StudentNickname.setText(self.student_nicknames[st])
			else:
				self.login_gui.StudentPhoto.setPixmap(QtGui.QPixmap(path.join('blank_girl.png')))
				self.login_gui.StudentNumber.setText('')
				self.login_gui.StudentNickname.setText('')
	
	def login_cancelbutton_clicked(self):
		#exit the app
		app.exit()

	def open_exam_window(self):
		#Initialise exam window
		self.examWindow = QtWidgets.QMainWindow()
		self.exam_gui = Ui_ExamQuestions()
		
		#Connect button methods from Exam main window code
		self.examWindow.logout_button_clicked = self.logout_button_clicked
		self.examWindow.exam_refresh_button_clicked = self.exam_refresh_button_clicked
		self.examWindow.forward_button_clicked = self.forward_button_clicked
		self.examWindow.back_button_clicked = self.back_button_clicked

		self.exam_gui.setupUi(self.examWindow)

		#hide back button in student mode
		if not self.admin:
			self.exam_gui.BackButton.hide()

		#connect any button group
		self.exam_gui.AnswerButtonGroup.setId(self.exam_gui.AnswerACheckBox,1)
		self.exam_gui.AnswerButtonGroup.setId(self.exam_gui.AnswerBCheckBox,2)
		self.exam_gui.AnswerButtonGroup.setId(self.exam_gui.AnswerCCheckBox,3)
		self.exam_gui.AnswerButtonGroup.setId(self.exam_gui.AnswerDCheckBox,4)
		self.exam_gui.FalsecheckBox.hide()
		self.exam_gui.AnswerButtonGroup.buttonClicked[QtWidgets.QAbstractButton].connect(self.check_answer)

		self.read_exam_questions_csv()

		#set the text etc
		self.exam_gui.ClassLabel.setText(self.class_name)
		self.exam_gui.StudentNumberLabel.setText(str(self.student_number))
		self.exam_gui.StudentNicknameLabel.setText(self.student_nicknames[self.student_number])
		self.exam_gui.StudentNameLabel.setText(self.student_names[self.student_number])
		with change_dir('img'):
			self.exam_gui.StudentPhotoLabel.setPixmap(QtGui.QPixmap(path.join('M' + str(self.year_chosen) + '-1', str(self.student_number) + '.png')))
		self.exam_gui.tabWidget.setCurrentIndex(0)

		#Show window
		self.populate_boxes(self.question_number)
		self.screen_location(self.examWindow)
		self.examWindow.show()
		self.examLogin.hide()

	def read_exam_questions_csv(self):
		self.exam_questions.clear()
		self.exam_AnswerA.clear()
		self.exam_AnswerB.clear()
		self.exam_AnswerC.clear()
		self.exam_AnswerD.clear()
		self.exam_Rightanswer.clear()

		with change_dir('resources'):
			with open('Exam_Questions.csv','r') as csv_file:
				csv_reader = csv.DictReader(csv_file)

				for line in csv_reader:
					self.exam_questions.append(line['Questions'])
					self.exam_AnswerA.append(line['AnswerA'])
					self.exam_AnswerB.append(line['AnswerB'])
					self.exam_AnswerC.append(line['AnswerC'])
					self.exam_AnswerD.append(line['AnswerD'])
					self.exam_Rightanswer.append(line['Rightanswer'])

	def logout_button_clicked(self):
		self.msgbox = QMessageBox()
		self.msgbox.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
		self.msgbox.setWindowTitle('Save your work')
		self.msgbox.setText('Do you want to save your progress?')
		self.msgbox.setIcon(QMessageBox.Question)
		self.msgbox.setStandardButtons(QMessageBox.Ok|QMessageBox.No)

		choice = self.msgbox.exec_()

		if choice == QMessageBox.Ok:
			pass
		if choice == QMessageBox.No:
			pass

		self.examWindow.close()
		self.open_login_window()

	def exam_refresh_button_clicked(self):
		pass

	def forward_button_clicked(self):
		if self.answer > 0:
			self.question_number += 1
			if self.question_number >= (len(self.exam_questions) -1):
				self.question_number = (len(self.exam_questions) -1)
			self.exam_gui.tabWidget.setCurrentIndex(0)
			self.exam_gui.FalsecheckBox.setChecked(True)

			self.populate_boxes(self.question_number)
		
	def back_button_clicked(self):
		self.question_number -= 1
		if self.question_number <= 0:
			self.question_number = 1
		self.exam_gui.tabWidget.setCurrentIndex(0)
		self.populate_boxes(self.question_number)

	def populate_boxes(self,quest):
		#Set text on exam questions and answers from list/csv
		self.answer = 0

		self.exam_gui.QuestionNumber.setText(str(self.question_number))
		self.exam_gui.Questions.setText(self.exam_questions[quest])
		self.exam_gui.AnswerTextA.setText(self.exam_AnswerA[quest])
		self.exam_gui.AnswerTextB.setText(self.exam_AnswerB[quest])
		self.exam_gui.AnswerTextC.setText(self.exam_AnswerC[quest])
		self.exam_gui.AnswerTextD.setText(self.exam_AnswerD[quest])
        
	def check_answer(self, btn):
		self.answer = self.exam_gui.AnswerButtonGroup.checkedId()
		if self.answer == self.convert(self.exam_Rightanswer[self.question_number]):
			self.score += 1


		
	def convert(self, val):
		return self.string_convert[val]

	def write_score(self):
		pass



print(sys.executable)

if __name__ == '__main__':
    # print (PY_VER)
    # print (QT_VER)
    app = QtWidgets.QApplication(sys.argv)
    main_app = App()

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
