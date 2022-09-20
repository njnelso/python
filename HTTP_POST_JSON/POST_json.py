#!/usr/bin/env python3

import json
import requests

response = requests.post('http://shell.fullstackacademy.com:16201/', json={'handle': 'Nick', 'movie': 'Bambi', 'command': 'grep'})

print(response.json())

## send an HTTP post with a json object
### solution to a cyberlab problem
