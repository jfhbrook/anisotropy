function m_ellipsoid(A)
    %plot not an ellipsoid using matrix A,
    %but a shape such that the distance from a pt
    %to the center is the reciprocal of the corresponding
    %distance for an ellipsoid.
    %Looks kinda neat!
    %x'*A*x=1;
    n=20;
    [x y z]=sphere(n);
    for i=1:n+1,
        for j=1:n+1,
            v=[x(i,j); y(i,j); z(i,j)];
            v=(v'*A*v)^(0.5)*v;
            x(i,j)=v(1);
            y(i,j)=v(2);
            z(i,j)=v(3);
        end
    end
    surf(x,y,z);
end
