function output=afoldd(fxn,x0,xs)
    % inspired by foldl' from haskell
    % Folds down over an array.
    output=zeros(1,size(xs,2));
    for n=1:size(xs,2),
        output(n) = fxn(x0,xs(1,n));
        for m=2:size(xs,1),
            output(n) = fxn(output(n),xs(m,n));
        end
    end
end
