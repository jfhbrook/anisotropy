% Trying out different ways of getting k
% Make sure data's loaded.

    opts = optimset('lsqcurvefit');
    opts.MaxFunEvals = 10e5;
    opts.MaxIter = 10e5;
    opts.TolFun = 10e-11;
    opts.TolX = 10e-11;
    opts.Display = 'off';

    [kxy,kz]=meshgrid(ks);
    for i=1:length(ks),
        for j=1:length(ks),
            fprintf('k results for kxy=%1.2f and kz=%1.2f',kxy(i,j),kz(i,j));
            % Some fits to try extracting k out of the heating curve
            t=solutions{i,j}{1}(1,:);
            T=solutions{i,j}{1}(2,:);

            % 1) Curve fit to expint() solution
            % Impression: Tweakable to get decent results
            Q = 0.12; %W/m 

            figure;
            plot(log(t(t>0)),T(t>0), 'ko');
            hold on;

            %imo this results in a horrible curve fit, though it might be tweakable.
            [a,r2] = lsqcurvefit(@ (x,a) x(1).*real(expint(x(2)./a)),[0.05 -0.0001],t(t>0),T(t>0),[],[],opts);

            fprintf('\nResult of expint fit: %1.6f\n',Q/4/pi/a(1));
            fprintf('R^2: %3.3f', r2);
            plot(log(t(t>0)), a(1).*real(expint(a(2)./t(t>0))),'r-*');

            % 2) Naive linear fit to latter "half" of heating curve
            % Seems relatively close

            % 10 secs chosen from experience, not procedurally.
            % Extra param coerces polyfit to do a better job
            [b,S] = polyfit(log(t(t>=10)),T(t>=10),1);

            fprintf('\nResult of linear fit: %1.6f\n', Q/4/pi/b(1));
            plot(log(t(t>=10)),b(1)*log(t(t>=10))+b(2), 'b-*');
        end
    end
