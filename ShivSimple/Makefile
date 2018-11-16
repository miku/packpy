SHELL = /bin/bash

requests.pyz:
	shiv requests -o requests.pyz

clean:
	rm -f requests.pyz

run: requests.pyz
	./$<

