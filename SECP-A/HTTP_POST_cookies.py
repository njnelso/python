#!/usr/bin/env python3

import requests

url = '<Insert URL here>'
cookies = {'name': 'value'}
### headers = {'Accept-Encoding': 'identity'} >> apparently not needed, thought i needed to specify that the output would be html
r = requests.post(url, cookies=cookies)
print(r.text)


### the cURL request in bash accomplishes the same task >> curl -X POST -b "cookie=value" <~Insert URL~>/ <<
