#!/usr/bin/python
import os
import glob

__author__ = 'vvu'

import sys
import requests

post_url = sys.argv[1]
data = sys.argv[2]

for filename in os.listdir(data):
	with open(data+"/"+filename, 'rb') as payload:
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		r = requests.post(post_url,
			data=payload, verify=False, headers=headers, timeout=0.1)
files = glob.glob(data+"/*")
for f in files:
	os.remove(f)