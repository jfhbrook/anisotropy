#!/usr/bin/env bash
# Runs ./dataset_generation/dataset_generator.m in matlab.
# Also sources ~/.profile. On the ARSCputers, this lets us run matlab.

. ~/.profile

cd dataset_generation
matlab -nosplash -nodisplay -r 'dataset_generator; exit'
cd ..
