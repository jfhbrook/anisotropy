function out=amap(fxn,in)
    %MATLAB implicitly maps all the time.
    %This function allows to explicitly map a function over an array.
    %It is designed to allow for string concatenation.
    out=[];
    for m=1:size(in,1),
            outrow=[];
        for n=1:size(in,2),
            outrow = [ outrow fxn(in(m,n))];
        end
        out=[out; outrow];
    end
end
