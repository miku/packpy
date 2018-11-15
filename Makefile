Slides.pdf: Slides.md
	pandoc -t beamer $< -o $@

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf hellopkg.egg-info/
	rm -rf hellopkg.pex
	rm -f Slides.pdf

sdist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

hellopkg.pex:
	pex . -c hellopkg-cli -o $@

