%controller.m
%does the controlling

angles = 0:10:90;
%angles = [0];
ks = linspace(0.2,0.4,8);

[kxy,kz] = meshgrid(ks,ks);

%flreport('off');

% Some parameters we won't want to iterate through
params=struct('rsnow', 0.4, ...
              'rneedle', 0.00025, ...
              'lneedle', 0.1, ...
              'density_snow', 200, ...
              'density_needle', 8000, ...
              'cp_snow', 2050, ...
              'cp_needle', 460, ...
              'q_needle', 635500, ...
              'k_needle', 160, ...
              'time', [colon(0,0.1,1) colon(2,2,10) colon(20,10,100)]);

saveroot='./solutions';


for angle=angles,
    mesh = mesher(angle,params);
    solutions = arrayfun(@(x,y) solver(x,y,mesh,params), kxy,kz, 'UniformOutput', false);
    fprintf('Fitting solutions...\n');
    solutions = cellfun(@(tsd) fitter(tsd(1,:),tsd(2,:),params.q_needle), solutions{0}, 'UniformOutput', true);
    save([saveroot 'solution-' date '-' num2str(angle)],'solutions','angle','ks','params');
end
