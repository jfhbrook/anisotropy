function a=symmetric_tocell(A)
    % Converts a symmetric matrix A into a cell containing the values, comsol-style.
    %I need to make sure comsol likes them nx1 instead of 1xn.

    %test for squareness
    assert(size(A,1)==size(A,2), 'Dawg that matrix aint square much less symmetric');
    %test for symmetry
    for i=1:size(A,1),
        for j=i:size(A,1),
            if (A(i,j)~=A(j,i)),
                disp(['Warning: Dawg that matrix aint square (A(' int2str(i) int2str(j) ')=' num2str(A(i,j)) ' != A(' int2str(j) int2str(i) ')=' num2str(A(j,i)) ' ! )']);
            end
        end
    end

    %The actual heavy lifting.
    a={};
    for m=1:size(A,1),
        for element=A(1:m,m)' %Takes upper-triangular section of mth column
            a{size(a,1)+1,1}=element;
        end
    end

end

function t=triangle(n)
    t=(n^2+n)/2;
end
