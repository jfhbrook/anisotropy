function p=lagrange(x,w)
    %Returns the Lagrange interpolating polynomial of the datapoints (x,y)
    %Was a (mostly) direct port of scipy.interpolate.lagrange() for matlab
    %Turns out lagrange(x,w) is effectively a special case of polyfit().
    p = polyfit(x,w,length(x)-1);
end
