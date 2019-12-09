'''
EXAM APPLICATION LAUNCHER developed by Mr Steven J walden
    Nov. 2019
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license at end of file]

'''

import os
import datetime, time

from os import path
from contextlib import contextmanager
from PyQt5 import QtCore

APPNAME = 'Exam App V1.0'


#set up app folders
APP_FOLDER = path.dirname(__file__)
IMG_FOLDER = path.join(APP_FOLDER, 'img')
SOUND_FOLDER = path.join(APP_FOLDER, 'snd')
RESOURCES_FOLDER = path.join(APP_FOLDER, 'resources')

@contextmanager
def change_dir(destination): #change directory function
	try:
		cwd = os.getcwd()
		os.chdir(destination)
		yield
	finally:
		os.chdir(cwd)

class ScrollThread(QtCore.QThread):
	time_value = QtCore.pyqtSignal(int)
	"""docstring for ScrollThread"""
	def __init__(self, parent, alloted_time):
		super(ScrollThread, self).__init__(parent)
		self.allowed_time = alloted_time
		self.is_running = True

	def run(self):
		while self.allowed_time >= 0 and self.is_running == True:
			self.allowed_time -= 1
			time.sleep(0.1)
			self.time_value.emit(self.allowed_time)

			if self.allowed_time < 0:
				self.is_running = False


class TimeThread(QtCore.QThread):
	time_value = QtCore.pyqtSignal(int)
	"""docstring for TimeThread"""
	def __init__(self, parent, alloted_time):
		super(TimeThread, self).__init__(parent)
		self.allowed_time = int(alloted_time / 600)
		self.is_running = True

	def run(self):
		while self.allowed_time >= 0 and self.is_running == True:
			self.allowed_time -= 1
			time.sleep(60.0)
			self.time_value.emit(self.allowed_time)

			if self.allowed_time < 0:
				self.is_running = False


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





#SPRITESHEET = "Exam_App_image_sheet.png"

		# self.pass_word_list = {}
		# self.pass_word_list['M1/1'] = ['passwords','1123','1456','1789']
		# self.pass_word_list['M1/2'] = ['passwords','2123','2456','2789']
		# self.pass_word_list['M1/3'] = ['passwords','3123','3456','3789']

		# self.student_photo_list = {}
		# self.student_photo_list['M1/1'] = [path.join(IMG_FOLDER, 'Blank_Person_160x192.png'),path.join(M1_1_FOLDER, '1.png'), path.join(M1_1_FOLDER, '2.png'), path.join(M1_1_FOLDER, '3.png')]

		# self.student_photo_list['M1/2'] = [path.join(IMG_FOLDER, 'Blank_Person_160x192.png'),path.join(M1_2_FOLDER, '1.png'), path.join(M1_2_FOLDER, '2.png'), path.join(M1_2_FOLDER, '3.png')]

		# self.student_photo_list['M1/3'] = [path.join(IMG_FOLDER, 'Blank_Person_160x192.png'),path.join(M1_3_FOLDER, '1.png'), path.join(M1_3_FOLDER, '2.png'), path.join(M1_3_FOLDER, '3.png')]

		# self.student_name_list = {}
		# self.student_name_list['M1/1'] = ['Choose your name','Palakun Pangpougkaew', 'Kittisukphat Yoo', 'Kitipat Thiangtham']
		# self.student_name_list['M1/2'] = ['Choose your name','Kitsakorn Polchai', 'Chuthawit Thongprasert', 'Naddanai Saelim']
		# self.student_name_list['M1/3'] = ['Choose your name','Kittipat', 'Naphat Chinnanno', 'Natnaris Sangrung']

		# self.student_nickname_list = {}
		# self.student_nickname_list['M1/1'] = ['nickname', 'Jaonaay', 'Khunmuen', 'Tor']
		# self.student_nickname_list['M1/2'] = ['nickname','Kew', 'Krap', 'Pooh']
		# self.student_nickname_list['M1/3'] = ['nickname','Nill', 'Boss', 'Santa']



		#self.login_gui.ClassCmb.currentIndexChanged.connect(self.class_name_changed)
		
		#self.login_gui.StudentNameCmb.currentIndexChanged.connect(self.student_name_change)

		#connect the buttons
		#self.login_gui.buttonBox.accepted.connect(self.login_okaybutton_clicked)
		#self.login_gui.buttonBox.rejected.connect(self.login_cancelbutton_clicked)
		#self.login_gui.PasswordShowButton.clicked.connect(self.password_show_button_clicked)
		#self.login_gui.InputPassword.returnPressed.connect(self.login_okaybutton_clicked)

		# self.exam_gui.LogoutButton.clicked.connect(self.logout_button_clicked)
		# self.exam_gui.RefreshButton.clicked.connect(self.exam_refresh_button_clicked)
