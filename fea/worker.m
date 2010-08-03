%worker.m
%works the comsol machinery

function worker(angles)
%worker(angles)
%Runs FEA jobs for the supplied list of angles.

    flreport('off');
    %initialization
    if (exist('feasols.mat')~=2),
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
                      'time', [logspace(0.1,1,15) logspace(1,3,15)]);
        mesh = NaN*angles;
        solutions = num2cell(NaN*kxy);
        save feasols;
    else,
        load feasols;
        %note: angles in degrees!
        for i=1:length(angles),
            % mesh
            if (mesh(i)==NaN),
                mesh(i) = mesher(angles(i),params);
                save feasols;
            end
            % fea
            for j=1:shape(solutions,1)*shape(solutions,2),
                if (solutions{j}==NaN),
                    solutions{j} = solver(kxy(j),kz(j),mesh,params);
                    % curve fit
                    solutions{j} = {solutions{j} fitter(solutions{j}{1}(1,:),solutions{j}{1}(2,:))};
                    save feasols;
                else,
                    fprintf "Already did that one.";
                end
            end
            save feasols;
        end
    end
end
