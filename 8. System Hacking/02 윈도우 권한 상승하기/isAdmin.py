import ctypes

def isAdmin():
	if ctypes.windll.shell32.IsUserAnAdmin():
		print('[*] Admin account:)')
	else:
		print('[*] Not admin account:( ')
    
isAdmin()
