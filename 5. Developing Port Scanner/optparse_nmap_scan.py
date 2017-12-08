#! python
# -*- coding: utf-8 -*-
# PortScanProgram with nmap Library
 
import nmap
import time
import datetime
import os.path
import os
import optparse
 
#optparse
parser = optparse.OptionParser('usage PortScanner -t <tgtHost> -p <tgtPort> -n <nmapOption>')
parser.add_option('-t', dest='tgtHost', type='string', help='must specify target Host')
parser.add_option('-p', dest='tgtPort', type='string', help='must specify target Port')
parser.add_option('-n', dest='nmapOption', type='string', help='specify nmapOption')
(option, args) = parser.parse_args()
 
if (option.tgtHost == None) | (option.tgtPort == None):
    print(parser.usage)
    exit(0) 
 
# 전역 변수 초기화
startTime = time.time()                # 시작 시간 기록
nm = nmap.PortScanner()                # nmap 객체 생성
hostList = option.tgtHost.split(',')                # 호스트 리스트 작성
portList = option.tgtPort              # 포트 리스트 작성
if option.nmapOption:
        myArg = option.nmapOption      # 옵션 설정
 
# 폴더 생성        
fileList = [] # 파일 이름 저장할 리스트 생성
dirName = 'scan_result'  # 폴더 이름 지정
if not os.path.exists('./' + dirName): # 폴더 없을 시 폴더 생성
    os.system('mkdir ' + dirName)
    print(dirName + " directory is made\n")
else: # 폴더 존재 시 폴더 생성 안 함
    print(dirName + " directory exists already\n")
if not os.path.isdir(dirName): # 해당 파일이 폴더가 아닐 경우 오류 발생
        print("Err: Same name file exists with directory name")
        exit()  # 프로그램 종료
 
# 스캔 시작
for host in hostList:
        host = host.strip() # 사용자가 공백을 입력했을 경우를 위해 스트립함
        print("scan {}:{}\nOptions: {}".format(host,portList,myArg))
        result = nm.scan(hosts=host,
                         ports=portList,
                         arguments=myArg) # 스캔 수행
        
        ntime = str(datetime.datetime.now()).replace(':','_') # 날짜 기록
        ntime = ntime.replace(' ','_')
        filename=ntime+'_'+host+'_result.csv' # 파일 이름 생성

        with open('./'+dirName+'/'+filename,'w') as f: # 파일 열기
            try: f.write("os info : " + (result['scan'][host]['osmatch'][0]['name']) + '\n')
            except : f.write("os info : unknown\n")
            f.write(nm.csv().replace(';',',')) # ms-csv형식으로 쓰기
        fileList.append(filename) # 파일 리스트에 목록 추가
 
# 결과 출력 : [2) python-nmap 체험하기]에서 사용한 코드를 그대로 사용하였다.
        for host in nm.all_hosts():
                print('\n\n------------------------result-------------------------')
                print('Host : %s ( %s)' %(host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                try:                            # OS 정보 출력
                        print('OS : '+ result['scan'][host]['osmatch'][0]['name'] + '\n')
                except:
                        print('OS : unknown\n')
                proto = 'tcp'
                print('--------')
                print('Protocol : %s' %proto)
                lport = nm[host][proto].keys()
                sorted(lport)
                for port in lport:
                        print('port : %s\tstate : %s' % (port,
                                str(nm[host][proto][port]['state'])))
                print("\n\n----------------------------------------------------------")
 
print("It's Finished!!")
 
endTime = time.time() # 종료 시간 기록
 
print("\n\n----------------------------------------------------------")
print("executed Time : " + str(endTime - startTime)) # 실행 시간 출력
 
print("\n\n>>>>>>>>>>> please check your result files")
print("This is your path:\n\t" + os.path.realpath(dirName) + '\n')
for fileName in fileList: # 생성한 파일 목록 출력
        print(fileName)
