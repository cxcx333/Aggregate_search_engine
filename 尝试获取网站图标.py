import re
import requests
from time import ctime

with open('engines.csv', 'r', encoding='utf8') as f:
    content = f.readlines()

domains = []
for i in content:
    list_ = i.split(',')[-1].split('/')

    domains.append('{}//{}/favicon.ico'.format(list_[0], list_[2]))

# print(domains)

for domain in domains:
    # try:
    #     res = requests.get(domain)
    #     if res.status_code == 200:
    #         with open(ctime().split(':')[-1] + '.ico', 'wb') as f:
    #             f.write(res.content)
    # except Exception as e:
    #     print(e)
    a = re.search(r'^((http://)|(https://))?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(/)', domain)
    print(a.group())