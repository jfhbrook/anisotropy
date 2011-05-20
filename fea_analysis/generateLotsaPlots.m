%Generate a plot for EVERY TSD in the suite!

ks = linspace(0.2, 0.4, 6);
ks = [0.2,0.4];
[kxy, kz] = meshgrid(ks, ks);
angles = 0:15:90;
angles = [0 90];

%For an obvious color gradient, from red to blue right now.
colores = @(i,n) [sin((i/n)*pi/2), 0, cos((i/n)*pi/2)];

figure;
hold on;
for theta = 1:length(angles)
    for i=1:length(ks)^2
        tT = answers{theta}{i}{2};
        plot(log(tT(1,tT(1,:) > 1 )),tT(2,tT(1,:) > 1), 'o-', 'color', colores(i,length(ks)^2));
        title([num2str(angles(theta)) ' degrees and kxy = ' num2str(ks( mod(i, length(ks)) + 1 )) ' and ' num2str(ks(floor((i-1)/length(ks))+1)) ]);
        figure;
    end
end
