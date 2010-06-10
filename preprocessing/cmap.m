function out=cmap(fxn,in)
    %MATLAB implicitly maps all the time.
    %This is a crappy function that explicitly does so, with cells.
    for m=1:size(in,1),
        for n=1:size(in,2),
            out{m,n}=fxn(in{m,n});
        end
    end
end
