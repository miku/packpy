SHELL = /bin/bash

sphinx.pex:
	pex sphinx -c sphinx-quickstart -o sphinx.pex

clean:
	rm -f sphinx.pex

run: sphinx.pex
	./$<
