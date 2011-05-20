#!/usr/bin/env bash

pdflatex resume
xelatex proposal
bibtex proposal
xelatex proposal
xelatex proposal
pdflatex compilation
