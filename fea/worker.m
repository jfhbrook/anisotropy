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
        mesh = num2cell(NaN*angles);
        solutions = cellfun(@(x) num2cell(NaN*kxy), num2cell(angles), 'UniformOutput', false);
        save feasols;
    else,
        load feasols;
        %note: angles in degrees!
        for i=1:length(angles),
            % mesh
            if size(mesh{i}(1))==1,
                mesh{i} = mesher(angles(i),params);
                save feasols;
            end
            % fea
            for j=1:size(solutions,1)*size(solutions,2),
                if (size(solutions{i}{j}) ~= 3),
                    solutions{i}{j} = solver(kxy(j),kz(j),mesh,params);
                    % curve fit
                    solutions{i}{j} = {solutions{i}{j} fitter(solutions{i}{j}{1}(1,:),solutions{i}{j}{1}(2,:))};
                    save feasols;
                else,
                    fprintf "Already did that one.";
                end
            end
            save feasols;
        end
    end
end
