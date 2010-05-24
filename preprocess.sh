#!/usr/bin/env bash
# Runs ./preprocessing/preprocessing.m in matlab.
# Also runs ~/.profile. On the ARSCputers, this lets us run matlab.

. ~/.profile

cd preprocessing
matlab -nosplash -nodisplay -r 'preprocessing; exit'
