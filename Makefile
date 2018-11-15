Slides.pdf: Slides.md
	pandoc -t beamer $< -o $@

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf hellopkg.egg-info/
	rm -f Slides.pdf

sdist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

