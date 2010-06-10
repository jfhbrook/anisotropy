function dataset=dataset_generator
    %generates the dataset. Parameters hidden here!

    % PARAMETERS
    kmin=0.15;
    kmax=0.45;
    kres=0.25;
    dimension=3;

    krange=kmin:kres:kmax;

    %generates a string akin to "[X1,X2,X3]"
    matrixlist=[ ...
    init(flatten([areplicate(dimension,"X")' ...
                  int2str([1:dimension]') ...
                  areplicate(dimension,",")' ]))];

    toeval = ["[" matrixlist "]=meshgrid(" cjoin(creplicate(dimension,"krange"),',') ");\n"];
    toeval = [toeval "{" matrixlist "}"];
    disp(toeval)
    
end
