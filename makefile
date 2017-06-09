
root   = $(CURDIR)
imgDir = $(root)/images/
data   = $(ls $(imgDir)data *.txt)
crossPre = $(imgDir)crossPlots/HepHe-
cross  = $(crossPre)300.eps $(crossPre)201.eps $(crossPre)111.eps $(crossPre)120.eps $(crossPre)102.eps\
			$(crossPre)030.eps $(crossPre)021.eps $(crossPre)012.eps $(crossPre)003.eps

$(cross): $(data) $(imgDir)hephe-cross-plots.py
	python $(imgDir)hephe-cross-plots.py

hephe.pdf: hephe.tex hephe.bib $(cross)
	latexmk -f -pdf -pdflatex="pdflatex -interaction=nonstopmode" -bibtex -use-make hephe.tex

clean:
	latexmk -C

