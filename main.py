'''
EXAM APPLICATION LAUNCHER developed by Mr Steven J walden
    Nov. 2019
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license at end of file]

'''

#!/usr/bin/env python

__author__ = 'Mr Steven J Walden'
__version__ = '1.0.0'


import os
import sys
import csv
import datetime, time

from App_Guis import Ui_ExamLogin, Ui_ExamQuestions
from methods import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget #, QApplication, QMainWindow, QDesktopWidget
#from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QT_VERSION_STR, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

PY_VER = sys.version[:3]

class App(QtWidgets.QWidget):
	"""docstring for App"""
	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		#setup app windows and theme
		dark_theme(app)
		#self.dark_theme()
		self.load_data()
		self.open_login_window()

	def load_data(self):
		self.class_list = ['Choose your class','M1/1','M2/1','M3/1']
		self.string_convert = {'A':1,'B':2,'C':3,'D':4}
		self.student_names, self.student_nicknames, self.student_passwords, = [], [], []
		self.exam_questions, self.exam_AnswerA, self.exam_AnswerB, self.exam_AnswerC, self.exam_AnswerD, self.exam_Rightanswer, self.exam_photoquestion = [],[],[],[],[],[],[]

		self.correct_answers = 0
		self.answer = 0
		
		self.admin = False

	def read_csv(self, clas):
		'''
		Function to get student details information from a .CSV file
		Reads a .CSV file from the resourses directory and appends the infomation to 3 lists.
		Arguments:
			clas {[integer]} -- [This is the selected school year number to be used as the first part of the .CSV filename i.i M1
		'''
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
		self.login_gui = Ui_ExamLogin()
		screen_location(self.login_gui)

		#Connect the methods
		self.login_gui.buttonBox.accepted.connect(self.login_okaybutton_clicked)
		self.login_gui.buttonBox.rejected.connect(self.login_cancelbutton_clicked)
		self.login_gui.PasswordShowButton.clicked.connect(self.password_show_button_clicked)
		self.login_gui.InputPassword.returnPressed.connect(self.login_okaybutton_clicked)
		self.login_gui.ClassCmb.currentIndexChanged['int'].connect(self.class_name_changed)
		self.login_gui.StudentNameCmb.currentIndexChanged['int'].connect(self.student_name_change)

		#populate the combo boxes
		self.login_gui.ClassCmb.addItems(self.class_list)
		#limit the number of items in the student name combo box
		self.login_gui.StudentNameCmb.setStyleSheet("QComboBox { combobox-popup: 0; }")
		self.login_gui.StudentNameCmb.setMaxVisibleItems(10)
		#start with the class combobox
		self.login_gui.ClassCmb.setFocus()

		self.login_gui.show()

	def login_okaybutton_clicked(self):
		try:
			#open main window and pass vairables
			self.password_input = self.login_gui.InputPassword.text()
			if self.password_input == self.student_passwords[self.student_number]:
				self.login_gui.close()
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
		app.exit()

	def open_exam_window(self):
		#Initialise exam window
		self.exam_gui = Ui_ExamQuestions()
		screen_location(self.exam_gui)
		self.question_number = 1

		#Set the times for the exam
		self.allowed_time = 20 * 600
		self.start_time = datetime.datetime.today()
		self.end_time = self.start_time + datetime.timedelta(hours=0, minutes=int(self.allowed_time / 600))

		#hide back button in student mode
		if not self.admin:
			self.exam_gui.BackButton.hide()

		#connect butoons to methods
		self.exam_gui.LogoutButton.clicked.connect(self.logout_button_clicked)
		self.exam_gui.BackButton.clicked.connect(self.back_button_clicked)
		self.exam_gui.ForwardButton.clicked.connect(self.forward_button_clicked)
		self.exam_gui.AnswerButtonGroup.setId(self.exam_gui.AnswerACheckBox,1)
		self.exam_gui.AnswerButtonGroup.setId(self.exam_gui.AnswerBCheckBox,2)
		self.exam_gui.AnswerButtonGroup.setId(self.exam_gui.AnswerCCheckBox,3)
		self.exam_gui.AnswerButtonGroup.setId(self.exam_gui.AnswerDCheckBox,4)
		self.exam_gui.FalsecheckBox.hide()
		self.exam_gui.AnswerButtonGroup.buttonClicked[QtWidgets.QAbstractButton].connect(self.check_answer)
		self.exam_gui.mediaPlayer.stateChanged.connect(self.repeat_video)

		self.read_exam_questions_csv()

		#set the text etc
		self.exam_gui.setWindowTitle(self.exam_questions[0] + " " + self.exam_AnswerA[0] + " Questions")
		self.exam_gui.ExamTitle.setText(self.exam_questions[0]+ "\n" + self.exam_AnswerA[0])
		self.exam_gui.StartTime.setText(self.start_time.strftime("%H:%M:%S"))
		self.exam_gui.EndTime.setText(self.end_time.strftime("%H:%M:%S"))
		self.exam_gui.ClassLabel.setText(self.class_name)
		self.exam_gui.StudentNumberLabel.setText(str(self.student_number))
		self.exam_gui.StudentNicknameLabel.setText(self.student_nicknames[self.student_number])
		self.exam_gui.StudentNameLabel.setText(self.student_names[self.student_number])
		with change_dir('img'):
			self.exam_gui.StudentPhotoLabel.setPixmap(QtGui.QPixmap(path.join('M' + str(self.year_chosen) + '-1', str(self.student_number) + '.png')))
		#self.exam_gui.tabWidget.setCurrentIndex(0)

		self.exam_gui.TimeLeftProgressBar.setMaximum(self.allowed_time)
		self.exam_gui.TimeLeftProgressBar.setMinimum(0)
		self.exam_gui.TimeLeftProgressBar.setValue(self.allowed_time)
		self.exam_gui.MinLeftLabel.setText(str(int(self.allowed_time / 600)) + " Min Left")
		
		#Create list of answerlabels and answer texts
		self.answer_label_list = [self.exam_gui.AnswerTextA,self.exam_gui.AnswerTextB,self.exam_gui.AnswerTextC,self.exam_gui.AnswerTextD]
		self.exam_answers_list = [self.exam_AnswerA,self.exam_AnswerB,self.exam_AnswerC,self.exam_AnswerD]

		#Show window
		self.populate_boxes(self.question_number)
		
		self.exam_gui.show()
		self.login_gui.hide()
		self.counters()

	def read_exam_questions_csv(self):
		self.exam_questions.clear()
		self.exam_AnswerA.clear()
		self.exam_AnswerB.clear()
		self.exam_AnswerC.clear()
		self.exam_AnswerD.clear()
		self.exam_Rightanswer.clear()
		self.exam_photoquestion.clear()

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
					self.exam_photoquestion.append(line['Photoquestion'])

	def counters(self):
		self.scroll_thread = ScrollThread(parent=None, alloted_time=self.allowed_time)
		self.scroll_thread.start()
		self.scroll_thread.time_value.connect(self.set_progress_bar)

		self.time_thread = TimeThread(parent=None, alloted_time=self.allowed_time)
		self.time_thread.start()
		self.time_thread.time_value.connect(self.set_time_label)

	def set_progress_bar(self, left_time):
		self.exam_gui.TimeLeftProgressBar.setValue(left_time)
		if left_time <= 0:
			self.message_boxes(msg='Time finished!', msg_type=1)

	def set_time_label(self, left_time):
		self.exam_gui.MinLeftLabel.setText(str(left_time) + " Min Left")

	def logout_button_clicked(self):
		self.message_boxes(msg='Logout?', msg_type=0)

	def message_boxes(self, msg, msg_type):
		self.msgbox = QMessageBox()
		self.msgbox.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
		self.msgbox.setWindowTitle(msg)
		self.msgbox.setDefaultButton(QMessageBox.Ok)

		if msg_type == 1:
			self.msgbox.setText('Your score is ' + str(self.correct_answers) + '/' + str(len(self.exam_questions)))
			self.msgbox.setIcon(QMessageBox.Information)
			self.msgbox.setStandardButtons(QMessageBox.Ok)
			self.save_results()
		else:
			self.msgbox.setText('Caution! \n You will loose your score.')
			self.msgbox.setIcon(QMessageBox.Warning)
			self.msgbox.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)

		if self.msgbox.exec() == QMessageBox.Ok:
			self.allowed_time = 20 * 600
			self.question_number = 1
			self.scroll_thread.is_running = False
			self.time_thread.is_running = False
			self.exam_gui.close()
			self.open_login_window()

	def save_results(self):
		pass

	def forward_button_clicked(self):
		if self.answered > 0:
			self.question_number += 1
			if self.question_number > (len(self.exam_questions) -1):
				self.question_number = (len(self.exam_questions) -1)
				self.message_boxes(msg='Exam finished!', msg_type=1)
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
		self.answered = 0
		self.exam_gui.QuestionNumber.setText(str(self.question_number))
		self.exam_gui.Questions.setText(self.exam_questions[quest])
		#Loop through label & answer lists and populate the labels with the answers
		num = 0
		for answer_label in self.answer_label_list:
			if len(self.exam_answers_list[num][quest]) > 4 and self.exam_answers_list[num][quest][-4:] == '.jpg':
				with change_dir('img'):
					answer_label.setPixmap(QtGui.QPixmap(self.exam_answers_list[num][quest]))
					answer_label.setScaledContents(True)
			else:
				answer_label.setText(self.exam_answers_list[num][quest])
			num+=1

		#Set video media
		fileName = "img/" + self.exam_photoquestion[quest]
		try:
			if self.exam_photoquestion[quest] != 'None':
				self.exam_gui.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
				self.exam_gui.mediaPlayer.play()
				
		except Exception as e:
			pass

	def repeat_video(self, video_state):
		if video_state == 0:
			self.exam_gui.mediaPlayer.play()

	def check_answer(self, btn):
		self.answered = self.exam_gui.AnswerButtonGroup.checkedId()
		if self.answered == self.convert(self.exam_Rightanswer[self.question_number]):
			self.correct_answers += 1

	def convert(self, val):
		return self.string_convert[val]

	def write_score(self):
		pass



print(sys.executable)

if __name__ == '__main__':
    print("Qt version:", QT_VERSION_STR)
    print("Author:", __author__)
    print("App version:",__version__)

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
