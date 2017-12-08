# cnc.py
import socket

addr = ('0.0.0.0', 12345)
with socket.socket() as s:
    s.bind(addr)
    s.listen()
    print('cnc server is started...')

    conn, addr = s.accept()
    print('Connect by', addr)

    while True:
        try:
            # 받은 데이터 출력
            data = conn.recv(1024)
            if data :
                print(data.decode(), end='')
            # 보낼 데이터 전송
            data = input()
            conn.send(data.encode())
        except Exception as e:
            print(e)

print("{} is disconnected".format(addr))
