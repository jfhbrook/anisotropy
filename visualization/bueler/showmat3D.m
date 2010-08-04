function showmat3D(A)
% SHOWMAT3D   showmat3D(A)
%   Pictures a 3 by 3 matrix by showing its action on the unit sphere
%      and its eigenspaces.
%   Try " showmat3D([1 0 1;0 2 3;1 3 -1]) " for a symmetric case and
%       " showmat3D([1 0 1;0 2 3;0 1 -1]) " for a nearly defective case.

% Tim Carlson 2002
% ELB 10/8/03

if ~all(size(A)==[3 3]), error('Matrix not 3 by 3.  Use "showmat" for 2 by 2.'), end
if cond(A)>1e15, disp('The matrix entered is badly conditioned (nearly singular).')
   disp('Rotate the plot in figure 2; not ellipsoid nearly flat.  '), end

[v,d]=eig(A);
L=max(max(abs(d))); % max eigenvalue suggests length of lines

clf, axis([-L L -L L -L L]); hold on
t=-1:1;
plot3(2*L*t*v(1,1),2*L*t*v(2,1),2*L*t*v(3,1));
plot3(2*L*t*v(1,2),2*L*t*v(2,2),2*L*t*v(3,2));
plot3(2*L*t*v(1,3),2*L*t*v(2,3),2*L*t*v(3,3));

% spherical coord grid on unit sphere; apply A
n = 20; theta = pi*(-n:2:n)/n; phi = (pi/2)*(-n:2:n)'/n;
X = cos(phi)*cos(theta);
Y = cos(phi)*sin(theta);
Z = sin(phi)*ones(size(theta));
xx=A(1,1)*X+A(1,2)*Y+A(1,3)*Z;
yy=A(2,1)*X+A(2,2)*Y+A(2,3)*Z;
zz=A(3,1)*X+A(3,2)*Y+A(3,3)*Z;

colormap([0 1 0]); mesh(xx,yy,zz)
title('The unit sphere under the linear transformation A.  Lines are eigenspaces.' )
axis square, hold off



