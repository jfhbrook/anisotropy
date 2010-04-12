function R=rotmat(z,theta)
    %rotmat(z,theta)
    %Produces a matrix that rotates theta radians around z
    %implements http://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula
    %should look this up from a *cough* more reputable source probably.

    z=z./norm(z); %makes sure z is the right length
    if norm(z)==0,
        z
        theta
    end
    I=eye(3);
    R=I + sin(theta)*xprodmat(z) + (1-cos(theta))*(z*z' - I );

    function ax=xprodmat(a)
        %computes a cross-product matrix 
        %ie, ax*b = a x b where ax is the matrix
        %thx http://en.wikipedia.org/wiki/Cross_product#Conversion_to_matrix_multiplication
        ax=[0 -a(3) a(2); ...
            a(3) 0 -a(1); ...
            -a(2) a(1) 0];
    end
end
