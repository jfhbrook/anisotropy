#!/usr/bin/bash

cd $SCRATCH/anisotropy/fea

screen comsol matlab -np 4 -ml -nosplash -ml -nodisplay -ml -r \''worker('$1'); ex
it'\'
