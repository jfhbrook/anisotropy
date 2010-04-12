function m_ellipsoid(A)
    %plot an ellipsoid using matrix A
    %x'*A*x=1;
    n=40;
    [x y z]=sphere(n);
    for i=1:n+1,
        for j=1:n+1,
            v=[x(i,j); y(i,j); z(i,j)];
            v=(v'*A*v)^(-0.5)*v;
            x(i,j)=v(1);
            y(i,j)=v(2);
            z(i,j)=v(3);
        end
    end
    mesh(x,y,z);
    colormap(bone);
end
