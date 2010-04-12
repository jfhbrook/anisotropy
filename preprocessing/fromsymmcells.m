function A=fromsymmcells(a)
    % inverts tosymmcells.

    %(Should test for symmetry)

    A=[a{1} a{2} a{4}; ...
       a{2} a{3} a{5}; ...
       a{4} a{5} a{6}];
