'''
Contains Methods classes for the Exam Application.

EXAM APPLICATION LAUNCHER developed by Mr Steven J walden
    Nov. 2019
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license at end of file]

'''
__author__ = 'Mr Steven J Walden'
__version__ = '1.0'

import os
import datetime, time

from os import path
from contextlib import contextmanager
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QColor
#from PyQt5.QtCore import Qt

# #set up app folders
# APP_FOLDER = path.dirname(__file__)
# IMG_FOLDER = path.join(APP_FOLDER, 'img')
# SOUND_FOLDER = path.join(APP_FOLDER, 'snd')
# RESOURCES_FOLDER = path.join(APP_FOLDER, 'resources')

@contextmanager
def change_dir(destination): #change directory function
	try:
		try:
			cwd = os.getcwd()
			os.chdir(destination)
			yield
		except FileNotFoundError: #On location not exsisting save to App folder resources
			cwd = os.getcwd()
			os.chdir('resources')
			yield
	finally:
		os.chdir(cwd)

def dark_theme(app):
	#Darl theme option for QMainwindow
	app.setStyle("Fusion")

	dark_palette = QPalette()

	dark_palette.setColor(QPalette.Window,QColor(53,53,53))
	dark_palette.setColor(QPalette.WindowText, QtCore.Qt.white)
	dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
	dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ToolTipBase, QtCore.Qt.white)
	dark_palette.setColor(QPalette.ToolTipText, QtCore.Qt.white)
	dark_palette.setColor(QPalette.Text, QtCore.Qt.white)
	dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
	dark_palette.setColor(QPalette.ButtonText, QtCore.Qt.white)
	dark_palette.setColor(QPalette.BrightText, QtCore.Qt.red)
	dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	dark_palette.setColor(QPalette.HighlightedText, QtCore.Qt.black)

	app.setPalette(dark_palette)

	app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

def screen_location(wn, win_type, avail_geom):
	#Set the screen location of a gui [wn = passed gui object, avail_geom = available screen size]
	#ag = QDesktopWidget().availableGeometry()
	#sg = QDesktopWidget().screenGeometry()

	widget = wn.geometry()
	x = avail_geom.width() / 2 - widget.width() / 2
	y = avail_geom.height() / 2 - widget.height() / 2
	if win_type: #Check if the gui in the main one
		wn.move(x,0)
	else:
		wn.move(x, y)

class ScrollThread(QtCore.QThread):
	time_value = QtCore.pyqtSignal(int)
	"""Seperate thread used to a countdown implemented in the main GUI"""
	def __init__(self, parent, alloted_time):
		super(ScrollThread, self).__init__(parent)
		self.allowed_time = alloted_time
		self.is_running = True

	def run(self):
		while self.allowed_time >= 0 and self.is_running == True:
			self.allowed_time -= 1
			time.sleep(0.1)
			self.time_value.emit(self.allowed_time)

			if self.allowed_time <= 0:
				self.is_running = False


class TimeThread(QtCore.QThread):
	time_value = QtCore.pyqtSignal(int)
	"""Seperate thread used to a countdown implemented in the main GUI"""
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


# Copyright (c) 2019 Steven J Walden
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
