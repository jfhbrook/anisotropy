%worker.m
%does the working

function worker(kxy,kz)
    load('angles.mat', 'angles');
    angles
    [kxy,kz] = meshgrid(kxy,kz);

    %flreport('off');

    params=struct('rsnow', 0.4, ...
                  'rneedle', 0.00025, ...
                  'lneedle', 0.1, ...
                  'density_snow', 200, ...
                  'density_needle', 8000, ...
                  'cp_snow', 2050, ...
                  'cp_needle', 460, ...
                  'q_needle', 0.5, ...
                  'k_needle', 160, ...
                  'time', [logspace(0.1,1,15) logspace(1,3,15)], ...
                  'angles', angles );

    saveroot=['./solutions-' date '/'];

    mesh = mesher(0,params);
    for angle=angles,
        try
            solutions = arrayfun(@(x,y) solver(x,y,mesh,angle,params), kxy,kz, 'UniformOutput', false);
            save solutions
            fprintf('Fitting solutions...\n');
            solutions = {cellfun(@(tsd) {fitter(tsd{1}(1,:),tsd{1}(2,:),0.999,params), tsd{1}, tsd{2}}, solutions, 'UniformOutput', false)};
            fprintf('Omigosh, a solution set is actually done!');
            system('echo "A solution just finished on" `hostname` | mutt -s "A solution got did!" josh.holbrook@gmail.com');
        catch exception
            system(['echo "Shit broke on" `hostname` | mutt -s "Hey man your shit''s broke!--' exception.message '" josh.holbrook@gmail.com']);
        end
        angles = angles(2:length(angles));
        save('angles.mat', 'angles');
        %solutions
        mkdir(saveroot);
        save([saveroot 'solution-' num2str(angle)],'solutions','angle','kxy','kz','params');
    end

    % Emails me when everything's done
    system('echo "You should check out your results on" `hostname` | mutt -s "Hey man your shit''s done!" josh.holbrook@gmail.com');
    system('touch down');
end
