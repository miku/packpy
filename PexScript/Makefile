SHELL = /bin/bash

sphinx.pex:
	pex sphinx -c sphinx-quickstart -o $@

clean:
	rm -f sphinx.pex

run: sphinx.pex
	./$<
