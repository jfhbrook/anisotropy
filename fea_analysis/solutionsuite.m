%angles = 0:15:90;
%save('angles.mat', 'angles');
kxy = [0.3];
kz = [0.1, 0.2, 0.3, 0.4, 0.5];
%ks = linspace(0.2,0.4,4);
worker(kxy, kz);
