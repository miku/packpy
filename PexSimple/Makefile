SHELL = /bin/bash

my_application.pex:
	pex requests -o $@

clean:
	rm -f my_application.pex

run: my_application.pex
	./$<

