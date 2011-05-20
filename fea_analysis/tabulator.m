%tabulator
%turns lame structures into some csv action

%given params:
%  answers
%  angles
%  kxy
%  kz

% Bad style, but I'm dealing with a cluttered namespace because I'm not functionalizing these.
% This is because parameter passing is a pita. So, leave me alone.
[Kxy, Kz] = meshgrid(kxy, kz);

fprintf('angle, kxy, kz, kmeas \n');
for t=1:length(angles),
    for pt=1:size(Kxy,1)*size(Kxy,2),
        fprintf([ num2str(angles(t)) ', ' num2str(Kxy(pt)) ', ' num2str(Kz(pt)) ', ' num2str(answers{t}{pt}{1}) '\n']);
    end
end
