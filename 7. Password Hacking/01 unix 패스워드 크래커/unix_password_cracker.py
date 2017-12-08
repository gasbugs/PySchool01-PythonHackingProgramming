#! python
# -*- coding: UTF-8 -*-
# unix password crack program
 
# import 실패 시 프로그램 종료 : crypt 파일이 Unix & Linux 파일에만 존재
try:
    import crypt
    import optparse
    import sys
except Exception as e:
    print ("This tool for Unix or Linux System")
    sys.exit(0)
    
# optparse
parser = optparse.OptionParser('uage %prog -t <taget shadow file> -d <dictionary file>')
parser.add_option('-t', dest='shadowfile', type='string', help='specify target shadow file')
parser.add_option('-d', dest='dicfile', type='string', help='specify dictionary file>')
 
# 전역변수 초기화
(option, args) = parser.parse_args()
shadowfile = option.shadowfile
dicfile = option.dicfile
 
# 입력값 검증
if (shadowfile == None) | (dicfile == None):
    print(parser.usage)
    sys.exit(0)                  
    
# 패스워드 테스트 함수
def testPass(cryptPass):
    # 만약 패스워드가 존재할 시에... (패스워드 필드를 $로 구분함)
    if cryptPass.find('$')==-1:
        return
    
    # 필드를 쪼개어 패스워드 필드를 추출해냄
    cryptPass1 = cryptPass.split('$')
    hashtype = cryptPass1[1]
    salt = cryptPass1[2]
    pass1 = cryptPass1[3]
    
    # 딕셔너리의 단어 해시 값과 실제 패스워드 해시 값을 비교
    dictFile = open(dicfile,'r')
    for word in dictFile.readlines():
        cryptWord = crypt.crypt(word[:-1],'$'+hashtype+'$'+salt)
        list1=cryptWord.split('$')
        cryptWord=list1[3]
        if(cryptWord == pass1):
            print ("[+] Found Password : "+word[:-1])
            return
    print ("[-] Password Not Found. ")
    return
 
# main 함수
def main():
    passFile = open(shadowfile)
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password For: " + user)
            testPass(cryptPass)
            
if __name__=="__main__":
    main()
