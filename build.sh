pdflatex --shell-escape thesis
pdflatex --shell-escape thesis
bibtex thesis
pdflatex --shell-escape thesis
# Stupid hack to get separate appendices to work. In future, look at:
# http://tex.stackexchange.com/questions/8211/list-of-appendices (2nd answer)
# and fix, for everyone else's benefit.
# This will only work automagically if NO SECTIONS ARE ADDED OR DELETED btw
# cp thesis.toc.bk thesis.toc
# cp thesis.loa.bk thesis.loa
pdflatex --shell-escape thesis
