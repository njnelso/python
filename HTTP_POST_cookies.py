#!/usr/bin/env python3

import requests

url = 'http://shell.fullstackacademy.com:8861/'
cookies = {'amount': '7'}
### headers = {'Accept-Encoding': 'identity'} >> apparently not needed, thought i needed to specify that the output would be html
r = requests.post(url, cookies=cookies)
print(r.text)