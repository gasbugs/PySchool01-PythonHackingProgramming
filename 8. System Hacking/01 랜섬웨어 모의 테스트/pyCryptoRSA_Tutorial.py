#! python 2.7
# -*- coding: UTF-8 -*-
# RasnomWare

import pyCryptoRSA

#1. 키 생성하기!
print("[*]Generate keys...")
private_key, public_key = pyCryptoRSA.generate_RSA(bits=2048)

public_key_loc = "public_key"
private_key_loc = "private_key"

try:
    with open(public_key_loc, 'wb') as f:
        f.write(public_key)

    with open(private_key_loc, 'wb') as f:
        f.write(private_key)

    print("[+]Generated keys very well")

except Exception as e :
    print("[Err] Key Genrater has err: {}".format(e))
    
#2. 생성한 공개 키로 문자 암호화하기
message = b"I love my job!"
package = pyCryptoRSA.encrypt_RSA(public_key_loc, message)

#3. 암호화한 파일 개인 키로 문자 복호화하기
decode = pyCryptoRSA.decrypt_RSA(private_key_loc, package)
print(decode)
