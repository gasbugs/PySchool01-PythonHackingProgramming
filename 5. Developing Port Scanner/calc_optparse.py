#! python
#! -*- coding: utf-8 -*-
# simple optparse calculater

import sys
import optparse
 
# optparse
parser = optparse.OptionParser('usage Calc.py -n <tgtNum> -o <operation>')
parser.add_option('-n', dest='tgtNum', type='string', help='write numbers with comma')
parser.add_option('-o', dest='operation', type='string', help='specify operation + - * / %')
option, args = parser.parse_args()

if len(sys.argv) < 5 :
    print(parser.usage)
    exit()
 
# 전역 변수 초기화
tgtNum = option.tgtNum.split(',')
oper = option.operation
operStr = ""
 
# 연산자 붙이기
for num in tgtNum:
    operStr += num + oper
 
# 마지막 연산자 제거
operStr = operStr[:-1]
 
#결과 출력
print('result is ' + str(eval(operStr)))
