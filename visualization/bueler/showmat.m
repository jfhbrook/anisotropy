function showmat(A);
% SHOWMAT      showmat(A):
%   Picture of a 2 by 2 matrix A,
%   with eigenvalues, singular values, and corresponding vectors.
%   Try:   >> showmat(2*randn(2,2)-ones(2,2))
%          >> showmat([.2 .01; 1 .2])
%          >> showmat([1 -1; -1 2])
%          >> showmat([1 0; -1 2])
%          >> showmat([1 0; -5 2])

if ~min((size(A)==[2 2])), error('matrix A is not 2 by 2'), end

[U,S,V]=svd(A);
[EV,D]=eig(A);

% input space picture
clf, th=linspace(0,2*pi,100); x=cos(th); y=sin(th);
subplot(1,2,1), plot(x,y,'--'), hold on
% normalize eigenvectors
if ~any(imag(D)) 
    for j=1:2, EV(:,j)=EV(:,j)/norm(EV(:,j),2); end
else, text(-1.0,-1.0,'IMAGINARY EIGENVALUES','Color',[.2 .8 0]), end
for j=1:2
    plot([0 V(1,j)],[0 V(2,j)],'r')
    text(.5*V(1,j),.5*V(2,j),['v_' num2str(j)])
    if ~any(imag(D)) 
        plot([0 EV(1,j)],[0 EV(2,j)],'Color',[.2 .8 0])
        text(.5*EV(1,j),.5*EV(2,j),['w_' num2str(j)])    
    end, end
axis equal, axis([-1.2 1.2 -1.2 1.2]), hold off

% text description
text(1.4,.25,'A maps'), text(1.5,0,'--->')
text(-.7,2.2,[num2str(A(1,1),'%5.4f') '    ' num2str(A(1,2),'%5.4f')])  
text(-1.0,2.1,'A = ')
text(-.7,2.0,[num2str(A(2,1),'%5.4f') '    ' num2str(A(2,2),'%5.4f')])  
text(-1.0,1.75,['\sigma_1 = ' num2str(S(1,1),'%6.4f') ', \sigma_2 = ' num2str(S(2,2),'%6.4f')])
text(-1.0,1.5,['\lambda_1 = ' num2str(D(1,1),'%6.4f') ', \lambda_2 = ' num2str(D(2,2),'%6.4f')])
text(-1.0,-1.6,'Singular vectors and values:  A v_j = \sigma_j u_j','Color','r')
text(-1.0,-1.9,'Eigenvectors and values:  A w_j = \lambda_j w_j','Color',[.2 .8 0])
text(-1.2,-2.3,'SHOWMAT:  Matrix Visualization  by  Ed Bueler')

out=A*[x; y]; subplot(1,2,2), plot(out(1,:),out(2,:),'--'), hold on
for j=1:2
    sig=S(j,j); ex=sig*U(1,j); ey=sig*U(2,j);
    plot([0 ex],[0 ey],'r')
    text(.5*ex,.5*ey,['\sigma_' num2str(j) ' u_' num2str(j)])
    if ~any(imag(D)) 
        lam=D(j,j); ewx=lam*EV(1,j); ewy=lam*EV(2,j);
        plot([0 ewx],[0 ewy],'Color',[.2 .8 0])
        text(.5*ewx,.5*ewy,['\lambda_' num2str(j) ' w_' num2str(j)])    
    end, end
mox=max(abs(out(1,:))); moy=max(abs(out(2,:)));
axis equal, axis([-1.4*mox 1.4*mox -1.1*moy 1.1*moy]), hold off
if any(imag(D)), text(-mox,-moy,'IMAGINARY EIGENVECTORS','Color',[.2 .8 0]), end

