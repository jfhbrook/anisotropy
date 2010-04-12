function [k_mats, k_mats_props]=k_generator(kmin,kmax,kres,sphres)
    %k_generator(kmin,kmax,kres,sphres)
    %generates a cell structure containing conductivity matrices
    %to run in a comsol model.
    %Also generates a cell structure containing more human-meaning stats
    %for each k-matrix: {kmin,kmax,v}.

    %generates needle orient's--x,y,z are O2 tensors
    [x y z]=sphere(sphres);

    
    
    %We only need one slice of the sphere due to symmetry.
    %That is, y~0, x>0 and z>0.
    %There's some floating point BS going on, so we have to compare about-ly for y.
    %i is the orientation index
    xpts=[];
    ypts=[];
    zpts=[];
    imax=(sphres+1)^2;
    for i=1:imax,
        if (x(i)>0)&(abs(y(i))<0.001)&(z(i)>0),
            xpts=[xpts x(i)];
            ypts=[xpts y(i)];
            zpts=[xpts z(i)];
        end
    end

   
    %generates range of conductivities to test
    kpts=linspace(kmin,kmax,kres);
    [kxy,kz]=meshgrid(kpts,kpts); %kxy and kz are O2 tensors
    %[kx,ky,kz]=meshgrid(k,k,k); %3-way anisotropy, O3 tensor version

    %i is the orientation index
    imax=size(xpts,2);
    %j is the conductivities index
    jmax=size(kxy,1)*size(kxy,2);

    %Creates empty cell structures to hold the data in
    k_mats=cell(imax,jmax);
    k_mats_props=cell(imax,jmax);
    
    for i=1:imax,
        for j=1:jmax,
            k_mats{i,j}=tosymmcells(cond_mat(kxy(j),kz(j),[xpts(i) ypts(i) zpts(i)]));
            k_mats_props{i,j}={kxy(j),kz(j),[xpts(i) ypts(i) zpts(i)]};
        end
    end
end
