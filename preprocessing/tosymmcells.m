function a=tosymmcells(A)
    % Converts a symmetric matrix A into a cell containing the values, comsol-style.

    %(Should test for symmetry)

    a={A(1,1); A(1,2); A(2,2); A(3,1); A(3,2); A(3,3)};
