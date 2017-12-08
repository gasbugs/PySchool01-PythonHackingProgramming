import socket

port = 53
addr = ("127.0.0.1",port) # DNS
socket.setdefaulttimeout(2)
#UDP
#소켓 오픈 : 응답이 없음 (반응없음)
#소켓 닫힘 : 응답이 있음 (소켓이 닫힘을 알림) 
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    try :
        s.sendto("Data".encode(),addr) # 데이터 전송
        s.recvfrom(1024)
        print("[+]{} udp port is opened".format(port))
    except Exception as e:
        print(e)
        if str(e) == "timed out":
            print("[+]{} udp port is opened".format(port))
        else :
            print("[-]{} udp port is closed".format(port))
