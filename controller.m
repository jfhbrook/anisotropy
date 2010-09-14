%controller.m
%does the controlling

angles = 0:10:90;
%angles = [0];
ks = linspace(0.2,0.4,6);

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
              'time', [logspace(0.1,1,15) logspace(1,3,15)]);

saveroot=['./solutions-' date '/'];


for angle=angles,
??? Index exceeds matrix dimensions.

Error in ==> @(tsd)fitter(tsd(1,:),tsd(2,:),params.q_needle)
    mesh = mesher(angle,params);
    solutions = arrayfun(@(x,y) solver(x,y,mesh,params), kxy,kz, 'UniformOutput', false);
    fprintf('Fitting solutions...\n');
    solutions = {cellfun(@(tsd) {fitter(tsd{1}(1,:),tsd{1}(2,:),params.q_needle), tsd{1}, tsd{2}}, solutions, 'UniformOutput', false) solutions{1} solutions{2} };
    save([saveroot 'solution-' num2str(angle)],'solutions','angle','ks','params');
end    solutions = {cellfun(@(tsd) {fitter(tsd{1}(1,:),tsd{1}(2,:),params.q_needle), tsd{1}, tsd{2}}, solutions, 'UniformOutput', false) solutions{1} solutions{2} };

% Emails me when everything's done
system('echo "You should check out your results on" `hostname` | mutt -s "Hey man your shit''s done!" josh.holbrook@gmail.com');