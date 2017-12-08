import servicemanager
import win32serviceutil
import win32service
import win32api
import os, time, ctypes

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

        with open('C:/Temp/isAdmin.txt','w') as f:
            if ctypes.windll.shell32.IsUserAnAdmin():
                    f.write('[*] Admin account:)')
            else:
                    f.write('[*] Not admin account:( ')
                    
        while self.runflag:
            time.sleep(1)
            
                
    def stop(self):
         self.runflag=False



if __name__ == '__main__':    
    servicemanager.Initialize() 
    servicemanager.PrepareToHostSingle(Svc)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Svc)

