import threading               # 스레드 관련 라이브러리
import socket                  # 소켓 관련 라이브러리
import time                    # 시간 라이브러리


 
resultLock = threading.Semaphore(value=1)    # 결과 출력을 제어할 세마포어
maxConnection = 100             # 스레드 개수를 제어할 세마포어
connection_lock = threading.BoundedSemaphore(value=maxConnection) 
port_result = {}    # 결과를 저장하는 dict
 
# 스레드 함수
def scanPort(tgtHost, portNum):
    try:                        # 접속 시도
        with socket.socket() as s:
            data = None
            
            s.settimeout(2)
            s.connect((tgtHost, portNum))
            s.send("Python Connect\n".encode())

            data = s.recv(1024).decode()
            
    except Exception as e :
        if str(e) == "timed out":
                data = str(e)
        else : data = 'error'
    finally:
        if data is None:
            data = "no_data"
        elif data == 'error':
            connection_lock.release() # 스레드 세마포어 해제
            return
        resultLock.acquire()# 출력 세마포어 설정
        print("[+] Port {} openend: {}".format(portNum, data[:20]).strip())
        resultLock.release()# 출력 세마포어 해제
        port_result[portNum]= data
        connection_lock.release() # 스레드 세마포어 해제
 
# 메인 함수
def main():
    tgtHost = "172.30.1.24" # 스캔 대상 tgtHost

    for portNum in range(1024): # 반복문 수행 0~1024 포트
        connection_lock.acquire()
        t = threading.Thread(target=scanPort, args =(tgtHost, portNum)) # 쓰레드 초기화
        t.start() # 스레드 실행
    time.sleep(5)

    print(port_result)
            
 
    # csv 파일 저장
    with open("portScanResult.csv",'w') as f: # 결과를 저장할 csv 파일 열기
        f.write("portNum, banner\n") # 컬럼 쓰기
        for p in sorted(port_result.keys()):       
            f.write("{}, {}".format(p, port_result[p]))

    # 결과 출력
    print("\n\n\n+++++++++++ the result +++++++++++")
    print('portNum' + '\t' + 'banner')
    for p in sorted(port_result.keys()):       
        print("{} \t {}".format(p, port_result[p][:20].strip()))
    print(">> the result in portScanResult.csv")
 
if __name__ == "__main__":
    startTime = time.time()
    main()
    endTime = time.time()
    print("exceuted Time:", (endTime-startTime))
