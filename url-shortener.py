#!/usr/bin/python

import sys
import requests


longUrl = raw_input("Long URL (ie: https://www.google.com): ")

apiKey = "363fb900c4f01464d672559ec122c63843f16593"

url = "https://api-ssl.bitly.com/v3/shorten"

cargo = {
	"access_token" : "363fb900c4f01464d672559ec122c63843f16593",
	"longUrl": longUrl,
	"format": "json"
	}

r = requests.get(url,params=cargo)
res = r.json()

print("Bit.ly Link:" + res['data']['url'])





