function k = fitter(t,T,params)

    opts = optimset('lsqcurvefit');
    opts.MaxFunEvals = 10e5;
    opts.MaxIter = 10e5;
    opts.TolFun = 10e-11;
    opts.TolX = 10e-11;
    opts.Display = 'off';

    fprintf('|');
    x = lsqcurvefit(@ (x,a) x(1).*real(expint(x(2)./a)),[0.05 -0.0001],t(t>0),T(t>0),[],[],opts);
    plot(log(t),T);
    hold on;
    plot(log(t), x(1)*log(t));
    k = (params.q_needle)/(4*pi*x(1));

end
