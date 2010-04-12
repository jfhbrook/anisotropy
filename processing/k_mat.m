function k=cond_mat(kxy,kz,v)
    %base k matrix action
    D=eye(3)*[kxy;kxy;kz];

    %rotation action
    e1=[1;0;0];%x unit vector
    %Calculate the rotation matrix corresponding to v
    angle=acos(dot(v,e1));
    axis=cross(v,e1);
    Q=rotmat(axis,angle);

    %rotate, k, rotate back
    %produces a symmetrical K matrix
    k=Q'*D*Q;
end
