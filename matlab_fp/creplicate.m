function list=creplicate(n,a)
    % returns a 1xn cell, each element being "a" (inspired by haskell).
    list=cell(1,n);
    for i=1:n,
        list{1,i}=a;
    end
end
