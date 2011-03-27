#!/usr/bin/env octave

% Using gnumeric to do some stats stuff.

angle = [90 90 90 75 75 75 75 60 60 60 30 30 30 30 90 90 90 75 75 75 75 60 60 60 30 30 30 30];

meas = [0.223 0.247 0.256 0.213 0.233 0.208 0.226 0.239 0.226 0.218 0.227 0.226 0.221 0.223 0.243 0.246 0.318 0.224 0.232 0.226 0.238 0.244 0.224 0.217 0.238 0.247 0.242 0.221];

[fit, s] = polyfit(angle, meas, 2)

C = corrcoef(angle, polyval(fit, meas))
