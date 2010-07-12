function A=symmetric_fromcell(a)
    % inverts cell form of symmetric matrix.
    % dependencies: triangle.m, triangle_inv.m

    n=triangle_inv(size(a,1));

    % should check for cell dimensions. This needs to be tested.
    assert(mod(n,1)==0, 'cells must be nx1!'); %makes sure n for nxn matrix implied by t is whole
    assert(size(a,2)==1,  'cells must be nx1 where n is a triangular number!'); %makes sure other dimension is 1

    % The heavy lifting.
    A=[];
    for m = 1:n,
        i=(m^2-m+2)/2:(m^2+m)/2; %slice of cells to wrap around A
        A=[A,init([a{i}])'; a{i}];
    
end

function n=triangle_inv(t)
    n = (sqrt(8*t+1)-1)/2;
end
