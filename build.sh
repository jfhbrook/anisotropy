pdflatex --shell-escape thesis
pdflatex --shell-escape thesis
bibtex thesis
pdflatex --shell-escape thesis
cp thesis.toc.bk thesis.toc
cp thesis.loa.bk thesis.loa
pdflatex --shell-escape thesis
