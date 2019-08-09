#!/usr/bin/python3

from sys import argv

tokens = []

with open(argv[1], 'rt') as f:
	line = f.readline().rstrip('\n')
	token = ''
	while(line != ''):
		for i in range(len(line)):
			if(line[i] != ' '):
				token += line[i]
			elif(token != ''):
				tokens.append(token)
				token = ''
		line = f.readline().rstrip('\n')

for i in range(len(tokens)):
	print("configure vlan {} add ports {} tagged".format(tokens[i], "2:54"))	
