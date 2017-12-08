import threading                       # 스레드 라이브러리
import time                                 # 시간 라이브러리
import random                               # 난수 라이브러리
 
numOfToilet = threading.Semaphore(value=3)  # 화장실이 3개 존재한다.
 
# 스레드 함수
def useToilet(peopleNum):                   # 스레드를 돌릴 함수를 정의해야 한다.
    time.sleep(random.randint(5,10))       # 화장실 사용 시간(5~10초 랜덤생성)
                                           #     해당 시간 동안 슬립
    print("he's happy now, people #{}\n".format(peopleNum), end="")
    numOfToilet.release()                   # 도어락 해제
    
# 메인 함수
def main():
    print("10 people start using 3 toilets...")
    for peopleNum in range(10):             # 10명의 사람들이 대기 중
        numOfToilet.acquire()               # 도어락 설정
        t=threading.Thread(target=useToilet, args=(str(peopleNum))) # 스레드 생성
        t.start()                             # 스레드 시작
    time.sleep(11)
    print("All People Happy~~~!!!")    # 모든 사람들 사용 종료
    
 
if __name__ =='__main__':
    main()
