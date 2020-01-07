#!/usr/bin/python
# -*- coding: utf-8 -*-
# <bitbar.title>Gold Price Tracker</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>Hoa Nguyen Manh</bitbar.author>
# <bitbar.author.github>hoanguyenmanh</bitbar.author.github>
# <bitbar.desc>Keep an eye on the gold price !</bitbar.desc>
# <bitbar.image>https://nothingreally.botler.me/bitbar.currency-tracker.png</bitbar.image>

import urllib2
import json

url = "https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD"

result = urllib2.urlopen(url).read()

list = json.loads(result)

price = "undefined"
for item in list:
	topo = item["topo"]
	server = topo["server"]
	spreadProfilePrices = item["spreadProfilePrices"]

	if server == "Real1":
		for spread in spreadProfilePrices:
			spreadProfile = spread["spreadProfile"]
			if spreadProfile == "Prime":
				price = spread["ask"]

print price