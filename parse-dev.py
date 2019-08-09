#!/usr/bin/python3

line = input()
try:
	while True:
		print(line)
		line = input()
except EOFError:
	exit(0)
