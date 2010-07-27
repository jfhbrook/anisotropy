%worker.m
%works the comsol machinery

function worker(angles)
%worker(angles)
%Runs FEA jobs for the supplied list of angles.

    flreport('off');

    ks = linspace(0.2,0.4,8);
    %ks = linspace(0.2,0.4,2);
    [kxy,kz] = meshgrid(ks,ks);
    % Some parameters we won't want to iterate through
    params=struct('rsnow', 0.4, ...
                  'rneedle', 0.0005, ...
                  'lneedle', 0.1, ...
                  'density_snow', 200, ...
                  'density_needle', 8000, ...
                  'cp_snow', 2050, ...
                  'cp_needle', 460, ...
                  'q_needle', 0.5, ...
                  'k_needle', 160, ...
                  'time', [logspace(0.1,1,15) logspace(1,3,15)], ...
                  'saveroot', './solutions/');

    %note: angles in degrees!
    for angle=angles,
        % mesh
        mesh = mesher(angle,params);
        % fea
        solutions = arrayfun(@(x,y) solver(x,y,mesh,params), kxy,kz, 'UniformOutput', false);
        % curve fit
        solutions = cellfun(@(x) {x{1} x{2} fitter(x{1}(1,:),x{1}(2,:))},solutions);
        save([params.saveroot 'solution-' date '-' num2str(angle)],'solutions','angle','ks','params');
        system(['tar -rf /archive/u1/uaf/holbrook/fea_sols.tar ' params.saveroot 'solution-' date '-' num2str(angle) '.mat']);
    end
end
