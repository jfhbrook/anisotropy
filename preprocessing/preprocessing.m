%preprocessing.m
%makes up gigantic data set of k-matrices for comsol to crunch out.
kmin=0.1;
kmax=0.2;

%these values were picked to result in a dataset that was sufficiently
%detailed yet able to get crunched in a reasonable amount of time.
kres=4;
sphres=9;

[k_mats,k_mats_props]=k_generator(kmin,kmax,kres,sphres);

save ../data/k_mats k_mats
save ../data/k_mats_props k_mats_props
