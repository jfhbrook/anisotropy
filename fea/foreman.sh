#!/usr/bin/bash


. /u1/uaf/holbrook/.profile
cd /scratch/holbrook/fea

nohup comsol matlab -np 4 -ml -nosplash -ml -nodisplay -r "worker($@)" &
