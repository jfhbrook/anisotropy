function fprime=listDerivative(x,f,n)
    % Returns the nth derivative of f with respect to x, 
    % where zip(x,f) are datapoints using lagrange
    % interpolating polynomials using o points.
    % This is a port of a similar function which I wrote in python.

    o=5; %Should make this an optional arg
    assert(mod(o,2) == 1); %should be odd imo
    derivative=[];
    for i=1:length(f)
        start=i-(o-1)/2;
        if start < 1,
            start = 1;
        end
        theend=start+o;
        if theend >= length(f),
            theend = length(f);
            start = theend-o;
        end
        spline=lagrange(x(start:theend),f(start:theend));
        for i=1:n
            spline=polyder(spline);
        end
        derivative = [ derivative polyval(spline,x(i))];
    end
    fprime = derivative;
end
