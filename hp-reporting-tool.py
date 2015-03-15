#!/usr/bin/python

__author__ = 'vvu'

import sys
import requests

post_url = sys.argv[1]
data = sys.argv[2]

with open(data, 'rb') as payload:
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(post_url,
                      data=payload, verify=False, headers=headers)