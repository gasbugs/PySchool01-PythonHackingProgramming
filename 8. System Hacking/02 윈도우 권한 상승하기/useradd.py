import win32net
import win32netcon

def useradd(USER = "Boan", GROUP = "Administrators"):    
        user_info = {
               "name": USER,
               "password": "!qhdkscjfwj@",
               "priv": win32netcon.USER_PRIV_USER,
               "home_dir": None,
               "comment": None,
               "flags": win32netcon.UF_SCRIPT,
               "script_path": None
                }

        user_group_info = {"domainandname": USER}

        try:
            win32net.NetUserAdd (None, 1, user_info)
            win32net.NetLocalGroupAddMembers (None, GROUP, 3, [user_group_info])
        except Exception as e:
            print(e)
            
useradd()
