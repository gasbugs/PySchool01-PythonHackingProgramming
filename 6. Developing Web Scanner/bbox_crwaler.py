# htmli_get.php test
from bs4 import BeautifulSoup
import requests, json
import re

server = "192.168.187.139"

def crawl(session, html, url, ip):
    urlList = {}
    bsObj = BeautifulSoup(html, "html.parser")
    path = url.split(url.split("/")[-1])[0]
    
    a = bsObj.findAll("a", href=re.compile("^https?://[a-z..]"+ip))
    for link in a :
        urlList[link['href'].split(ip)[1]] = None
    
    a = bsObj.findAll("a", href=re.compile("^\/"))
    for link in a :
        urlList[link['href']] = None

    a = bsObj.findAll("a", href=re.compile("^[^http.\/]"))
    for link in a :
        urlList[path + link['href']] = None

    print(bsObj)
    return urlList


with requests.Session() as s:
    #get cookie
    url = "http://"+server+"/bWAPP/login.php"
    # login
    post_param = {"login":"bee","password":"bug","security_level":"0","form":"submit"}
    res = s.post(url, data=post_param)
    print(s.cookies)
    
    # crawl
    result = crawl(s, res.text, "/bWAPP/portal.php", server)
    print(result)

    
