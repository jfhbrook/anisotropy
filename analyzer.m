%analyzer
%Does some analyzing of the simulation results

%Solutions location
%load solutions-19-Sep-2010/solutions-all.mat;

%Things I already know :)
%ks = linspace(0.2, 0.4, 6);
ks = 0.3;
[kxy, kz] = meshgrid(ks, ks);
%angles = 0:15:90;
angles = 0;

%For an obvious color gradient, from red to blue right now.
colores = @(i,n) [sin(i*pi/2*n), 0, cos(i*pi/2*n)];

disp('Showing some plots to make sure they "look" right:');
for theta = 1:length(angles)
    figure;
    hold on;
    for i=1:length(ks)^2,
        tT = answers{1}{i}{2};
        plot(log(tT(1,:)),tT(2,:), 'color', colores(i,length(ks)));
    end
end

disp('Sanity checking results for isotropic cases');
figure;
hold on;
for theta=1:length(angles)
    %Extracts all the measured k's from the data
    kms = cellfun(@(prison) prison{1}(1), answers{theta});
    errs = (diag(kms) - diag(kxy))./diag(kxy);
    plot(diag(kxy), errs, 'linewidth', 2, 'color', colores(i,length(diag(kxy))) );
end

disp('Plotting out T_surf_avg at time T:');
figure;
hold on;
for theta=1:length(angles)
    tavgs = cellfun(@(prison) prison{3}, answers{theta});
    try
        assert(all(tavgs< 0.001));
    catch
        disp(['Warning: average surface temps are a bit high at theta=' num2str(angles(theta))] );
    end
    contourf(tavgs);
    colorbar;
    colormap('pink');
    title('Average Surface Temperature at End of Heating Curve Simulation');
    xlabel('K_{xy}');
    ylabel('K_{zz}');
end

kms=cell(size(ks));
for i=1:length(theta)
    %note, normed by kxy
    kmsbyangle = cellfun(@(prison) prison{1}(1), answers{theta})./kxy;
    for j=1:length(ks)
        kms{j} = [kms{j}; kmsbyangle(j,:)]
    end
end
kms

disp('Plotting out k_meas:');
figure;
hold on;
contour(kms);
    
disp('Plotting out k_meas in 3D');
figure;
hold on;
surf(kms);
