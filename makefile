
diss.pdf: hephe.tex hephe.bib
	latexmk -f -pdf -pdflatex="pdflatex -interaction=nonstopmode" -bibtex -use-make hephe.tex

clean:
	latexmk -C

