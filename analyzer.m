%analyzer
%Does some analyzing of the simulation results

%Solutions location
%load solutions-19-Sep-2010/solutions-all.mat;

%Things I already know :)
ks = linspace(0.2, 0.4, 6);
ks = [0.2,0.4];
[kxy, kz] = meshgrid(ks, ks);
angles = 0:15:90;
angles = [0 90];

%For an obvious color gradient, from red to blue right now.
colores = @(i,n) [sin((i/n)*pi/2), 0, cos((i/n)*pi/2)];

disp('Showing overlaid plots (YES ALL OF THEM) to make sure they "look" right:');
figure;
hold on;
for theta = 1:length(angles)
    for i=1:length(ks)^2
        tT = answers{theta}{i}{2};
        plot(log(tT(1,tT(1,:) > 1 )),tT(2,tT(1,:) > 1), 'color', colores(i,length(ks)^2));
    end
end

disp('Sanity checking results for isotropic cases');
figure;
hold on;
kmsold = 0 * cellfun(@(prison) prison{1}, answers{1});
for i=1:length(angles)
    %Extracts all the measured k's from the data
    % "prison" refers to cell representing particular k combination in answers{theta}
    kms = cellfun(@(prison) prison{1}, answers{i});
    if kms == kmsold,
        disp('wtf exactly equivalent kms''s');
    end
    %diag(kms)
    %diag(kxy)
    errs = 100*(diag(kms) - diag(kxy))./diag(kxy);
    %Not necessary to be 3d anymore :)
    plot3(diag(kxy), errs, angles(i)*ones(size(diag(kxy))), '*-', 'color', colores(i,length(angles)) );
    xlabel('k_{actual}');
    ylabel('error (%)');
    zlabel('angle (degrees)');
end

disp('Figuring out T_surf_avg at time T:');
%figure;
%hold on;
for theta=1:length(angles)
    tavgs = cellfun(@(prison) prison{3}, answers{theta});
    try
        assert(all(all(tavgs< 0.001)));
    catch
        disp(['Warning: average surface temps are a bit high at theta=' num2str(angles(theta))] );
        disp(tavgs);
    end
    %This simulation should *probably* be done on the same basis as the
    if theta == length(angles)
        figure;
        hold on;
        contourf(kxy,kz,tavgs);
        colorbar;
        colormap('pink');
        title('Average Surface Temperature at End of Heating Curve Simulation for a representative angle');
        xlabel('K_{xy}');
        ylabel('K_{zz}');
    end
end

%dimensions changed to be in order kxy, then rows are angle and columns are kzz
disp('Plotting k_{meas}/k_{xy} vs. \theta and k_{z}/k_{xy}...');
kms=cell(size(ks));
for i=1:length(angles)
    kmsbyangle = cellfun(@(prison) prison{1}, answers{i});
    for j=1:length(ks)
        kms{j} = [kms{j}; kmsbyangle(:,j)'/ks(j)]; %Normalize by particular kxy
    end
end
figure;
hold on;
[kgrid, anggrid] = meshgrid(ks, angles);
for n=1:length(ks)
    plot3(reshape(anggrid',[],1), reshape(kgrid'/ks(n),[],1), reshape(kms{n}',[],1), '*-', 'color', colores(n, length(ks)));
end
%legend(arrayfun(@(x) num2str(x),ks, 'UniformOutput', false));
xlabel('angle (degrees)');
ylabel('k_{zz}/k_{xy}');
zlabel('k_{meas}/k_{xy}');

