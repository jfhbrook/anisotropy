function list=areplicate(n,a)
    % returns a 1xn cell, each element being "a" (inspired by haskell).
    list=zeros(1,n);
    for i=1:n,
        list(1,i)=a;
    end
    if ischar(a),
        list=arrayfun(@char, list);
    end
end
