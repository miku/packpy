SHELL = /bin/bash

app.zip: __main__.py
	(cd pymarc && zip -r ../$@ pymarc)
	zip -ur $@ __main__.py

app: app.zip
	@echo '#!/usr/bin/env python' >> app
	@cat $< >> app
	chmod +x app

clean:
	rm -f app.zip
	rm -f app

run: app.zip
	python $< catalog.mrc
