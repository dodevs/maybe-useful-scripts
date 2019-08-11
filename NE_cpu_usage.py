#!/usr/bin/python3

from urllib.request import urlopen

cpus = {}

# Só um pull request
content = urlopen('http://localhost:9100/metrics').read().decode().split('\n')

for line in content:
	if(len(line) != 0 and line[0] != '#'):
		if(len(line) > 38):
			if(line[0:22] == 'node_cpu_seconds_total'):
				print(line)
