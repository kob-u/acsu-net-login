#!/usr/bin/python
################################
#Write your id and password
username = "";
password = "";
################################

import sys
import getpass
try:
    import requests
except:
    print("Need requests lib")
    exit()



#shinshu-u acsu network login url
url = "https://login.shinshu-u.ac.jp/cgi-bin/Login.cgi"


argvs = sys.argv
argc = len(argvs)

if argc > 2:
    username = argvs[1]
    password = argvs[2]

if not username:
    username = input("Input username : ")
if not password:
    password = getpass.getpass("Input password : ")

payload = {'uid' : username, 'pwd' : password}

try:
    r = requests.post(url, data=payload)
except:
    print("Cannot connect : " +url)
    exit()

print("Server Status : " + requests.status_codes._codes[r.status_code][0])

if r.status_code != 200:
    print("exit")
    exit()

if r.text.find('Login Success') >=0:
    print("Login Success")
else:
    print("username or password Incorrect")
