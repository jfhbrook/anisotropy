#!/usr/bin/env bash

. ~/.profile

cd preprocessing
matlab -nosplash -nodisplay -r 'preprocessing; exit'
