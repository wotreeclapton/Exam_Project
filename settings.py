'''
 App developed by Mr Steven J walden
'''

import os
from os import path
from contextlib import contextmanager

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
