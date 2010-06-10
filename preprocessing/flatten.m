function flat=flatten(x)
    % skooshes a given array into 1xn
    flat=reshape(x',1,size(x,1)*size(x,2));
end
