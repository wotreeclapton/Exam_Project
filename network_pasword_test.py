import win32net
import win32file
import os
import pywintypes
import subprocess

#subprocess.call("net use * /d /y", shell=True)

network_add = '//192.168.88.250/exam_app_data'
netlogin = {'remote': network_add, 'local': '', 'username': 'exam_app', 'password': 'passyourexam'}

try:
    win32net.NetUseAdd(None, 2, netlogin)
    with open('//192.168.88.250/exam_app_data/test_file.txt', 'r') as file:
        contents = file.read()
    print(contents)
except pywintypes.error as e:
    print("Please contact your teacher.\n{}".format(str(e)))




subprocess.call("net use * /d /y", shell=True)
subprocess.call("klist purge", shell=True)

#win32net.NetUseDel(None, network_add, 2)


'''
net use * /d
klist purge
import subprocess
subprocess.run(["ls", "-l"])
subprocess.call("klist purge", shell=True)
subprocess.call("net use * /d /y", shell=True)
'''
