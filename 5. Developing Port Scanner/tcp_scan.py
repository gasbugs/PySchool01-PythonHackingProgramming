# tcp scan
import socket

with socket.socket() as s:
    addr = ("127.0.0.1",80)
    try:
        s.connect(addr)
        print("80 tcp socket is opened")
    except:
        print("80 tcp socket is closed")
        
    
    
