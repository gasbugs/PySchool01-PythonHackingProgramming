import requests, json

server = "172.30.1.43"

with requests.Session() as s:
    #get cookie
    url = "http://"+server+"/bWAPP/login.php"
    # login
    post_param = {"login":"bee","password":"bug","security_level":"0","form":"submit"}
    res = s.post(url, data=post_param)
    print(s.cookies)
    
    # connect after login
    url = "http://{}/bWAPP/htmli_get.php".format(server)
    res = s.post(url)
    print(res)
