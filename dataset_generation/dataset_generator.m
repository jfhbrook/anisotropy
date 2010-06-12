function dataset_generator
    %generates the dataset. Parameters hidden here!

    % PARAMETERS %
    kmin=0.15;
    kmax=0.45;
    kres=0.25; %smaller is better!
    anglemin=0; %angles in degrees
    anglemax=90;
    angleres=5; %smaller is better
    dimension=2; %number of directions of anisotropy
    savepath='../data/dataset.mat';
    %============%

    %In this particular case, it doesn't make sense for dim>3
    assert(dimension <= 3)

    krange=kmin:kres:kmax;
    anglerange=(pi/180).*[anglemin:angleres:anglemax]; %angles now in rads

    % evaluates string akin to "[X1,X2,X3,X4]=ndgrid(anglerange,krange,krange,krange);"
    % TODO: Learn up about the subtle differences between meshgrid and ndgrid,
    % make sure they don't matter
    eval(['[' xsList(dimension+1) ']=ndgrid(anglerange,' argRep(dimension,'krange') ');']);

    %Creates empty cell structures to hold the data in
    dataset=cell(size(X1,1)*size(X1,2)); %assumes X1 was created

    %creates a string akin to 'diag([X2(i),X2(i),X3(i)])'
    KtoEval=['diag([' argRep(4-dimension,'X2(i)') ',' ajoin(feval(@(x) x(1:dimension-1,:), ['X3(i)';'X4(i)']),',') '])'];

    for i=1:size(dataset),
        dataset{i}={X1(i), eval(KtoEval)};
    end

disp('saving dataset...');

eval(['save ' savepath 'dataset'])

end

function list=xsList(n)
    %generates a string akin to "X1,X2,X3,X4" with n elements
    list=[init(flatten([areplicate(n,'X')' int2str([1:n]') areplicate(n,',')' ]))];
end

function list=argRep(n,arg)
    %generates a string akin to "k,k,k,k" with n elements
    list = cjoin(creplicate(n,arg),',');
end
