function [fprime,x]=listDerivative(f,x,n)
    % [fprime,x]=listDerivative(f,x,n)
    % Returns f' for the nth derivative of f with respect to x, 
    % where zip(x,f) are datapoints using interpolating polyfits.

    %Ideally would be opts
    npts=7;
    o=3;
    assert(o < npts);
    derivative=[];
    for i=1:length(f)
        start=i-(npts-1)/2;
        if start < 1,
            start = 1;
        end
        theend=start+npts;
        if theend >= length(f),
            theend = length(f);
            start = theend-npts;
        end
        spline=polyfit(x(start:theend),f(start:theend),o);
        for i=1:n
            spline=polyder(spline);
        end
        derivative = [ derivative polyval(spline,x(i))];
    end
    fprime = derivative;
end
