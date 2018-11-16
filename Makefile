Slides.pdf: Slides.md
	touch Slides.pdf && osascript marp.scpt
	# pandoc -t beamer $< -o $@

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf hellopkg.egg-info/
	rm -rf hellopkg.pex
	rm -f Slides.pdf
	find . -type d -name "__pycache__" -exec rm -rf {} \;

sdist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

hellopkg.pex:
	pex . -c hellopkg-cli -o $@

