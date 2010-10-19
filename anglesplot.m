% This was used to plot angles from the one-slice data.

plot(0:5:90, cellfun(@(x) x{1}{1}, answers));
