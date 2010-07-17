function p=lagrange(x,w)
    %Returns the Lagrange interpolating polynomial of the datapoints (x,y)
    %A (mostly) direct port of scipy.interpolate.lagrange() for matlab
    %I'd prefer using scipy, but the python situation on ARSC blows. >:(
    %Also, this is short, so it was easier
    M = length(x);
    p = [0];
    for j=1:M,
        pt = w(j);
        for k=1:M,
            if k != j,
                fac = x(j)-x(k);
                pt = conv(pt,[1,-x(k)])/fac;
            end
        end
        p = polyadd(p,pt);
    end
end

function pnew=polyadd(p1,p2)
    %polyadd(p1,p2)
    %adds two polynomials p1 and p2.
    %make vectors same length, pre-filling with zeros
    %Used to fill out the features contained in numpy's poly1d.
    lmax=max(length(p1),length(p2));
    p1 = [zeros(1,lmax-length(p1)) p1];
    p2 = [zeros(1,lmax-length(p2)) p2];
    pnew = p1+p2;
end
