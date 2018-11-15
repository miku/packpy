Slides.pdf: Slides.md
	pandoc -t beamer $< -o $@

clean:
	rm -f Slides.pdf

