function output=cfoldl(fxn,x0,xs)
    % inspired by foldl' from haskell
    % Folds right over a mxn cell structure
    %a craptacular hack. stfu.
    for n=1:size(xs,2),
        output = fxn(x0,xs{1,n});
        for m=2:size(xs,1),
            output = fxn(output,xs{m,n});
        end
    end
end
