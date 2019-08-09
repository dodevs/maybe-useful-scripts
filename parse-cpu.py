#!/usr/bin/python3

from sys import argv

start = int(argv[2])
time = 0

with open(argv[1], 'rt') as f:
	#line = f.readline()
	for i in range(start):
		line = f.readline()
	while line != '':
		s = line.split(';')
		print(time, 100 - float(s[-1].replace(',', '.')), sep=';')
		line = f.readline()
		time += 1
