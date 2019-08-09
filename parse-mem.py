#!/usr/bin/python3

from sys import argv

line = ''
time = 0
start = int(argv[1])
for i in range(start):
	line = input()
try:
	while True:
		print(time, line, sep=';')
		line = input()
		time += 1
except EOFError:
	exit(0)
