'''
Contains Methods classes for the Exam Application.

EXAM APPLICATION LAUNCHER developed by Mr Steven J walden
    Nov. 2019
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license.txt file]

'''
__author__ = 'Mr Steven J Walden'
__version__ = '1.0'

import os
import datetime
import time

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
def change_dir(destination, logger): #change directory function
	try:
		try:
			cwd = os.getcwd()
			os.chdir(destination)
			yield
		except FileNotFoundError: #On location not exsisting save to App folder resources
			logger.error(" Unable to connect to network location: {}".format(destination))
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

