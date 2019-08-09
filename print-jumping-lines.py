#!/usr/bin/python3

from sys import argv

n = int(argv[2])
start = int(argv[3])
name = argv[1]
i = 0

with open(name, 'rt') as f:
	line = '' #f.readline()
	for i in range(start-1):
		line = f.readline()
	while line != '':
		print(line, end='')
		while i < n and line != '':
			line = f.readline()
			i += 1
		i = 0
