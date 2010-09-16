function k = fitter(t,T,Q)
    opts = optimset('lsqcurvefit');
    opts.MaxFunEvals = 10e5;
    opts.MaxIter = 10e5;
    opts.TolFun = 10e-11;
    opts.TolX = 10e-11;
    opts.Display = 'off';

    fprintf('|');
    k = lsqcurvefit(@ (x,a) x(1).*real(expint(x(2)./a)),[0.05 -0.0001],t(t>0),T(t>0),[],[],opts);

end