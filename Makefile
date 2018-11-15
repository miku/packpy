Slides.pdf: Slides.md
	pandoc -t beamer $< -o $@

clean:
	rm -rf hellopkg.egg-info/
	rm -f Slides.pdf

