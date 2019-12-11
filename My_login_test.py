'''
Template Gui by Mr Steven J Walden

This is a basic GUi starting point
'''

import sys
from PyQt5 import QtWidgets, QtGui
#from PyQt5.QtWidgets import QWidget

class Ui_ExamLogin(QtWidgets.QWidget):
	"""docstrbing for MyApp"""
	def __init__(self, parent=None):
		super(Ui_ExamLogin, self).__init__(parent)
		self.initUI()
		self.add_labels()

	def initUI(self):
		self.resize(588, 270)
		self.setMinimumSize(588, 270)
		self.setMaximumSize(588, 270)
		self.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
		self.setWindowTitle("Exam Login")

	def add_labels(self):

		self.ClassLabel = QtWidgets.QLabel("Class", self)
		self.ClassLabel.setGeometry(10, 10, 300, 60)
		font = QtGui.QFont()
		font.setPointSize(30)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.ClassLabel.setFont(font)
		self.ClassLabel.setText("Class")

		self.EnterNameLabel = QtWidgets.QLabel("Choose your name from the list below", self)
		self.EnterNameLabel.setGeometry(10, 114, 211, 16)

		self.InputPaswordLabel = QtWidgets.QLabel("Password", self)
		self.InputPaswordLabel.setGeometry(10, 172, 131, 16)

		self.Logolabel = QtWidgets.QLabel("Logolabel", self)
		self.Logolabel.setGeometry(320, 20, 75, 97)
		self.Logolabel.setPixmap(QtGui.QPixmap("img/School logo75x97_grad.png"))

		self.StudentNumberLabel = QtWidgets.QLabel("Number:",self)
		self.StudentNumberLabel.setGeometry(250, 170, 50, 18)
		font = QtGui.QFont()
		font.setItalic(True)
		self.StudentNumberLabel.setFont(font)

		self.StudentNicknameLabel = QtWidgets.QLabel("Nickname:", self)
		self.StudentNicknameLabel.setGeometry(250, 200, 50, 18)
		self.StudentNicknameLabel.setFont(font)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main_app = Ui_ExamLogin()
	main_app.show()


sys.exit(app.exec_())

