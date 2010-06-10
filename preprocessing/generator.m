function dataset=dataset_generator
    %generates the dataset. Parameters hidden here!

    % PARAMETERS
    kmin=0.15
    kmax=0.45
    kres=0.25
    dimension=2

    toeval = ["[" ...
    init(flatten([areplicate(dimension,"X")' ...
                  int2str([1:dimension]') ...
                  areplicate(dimension,",")' ])) ...
    "]=meshgrid(" cjoin(areplicate(dimension,"kmin:kres:kmax"),',') ")"]
    disp(toeval)
    
end

a=[amap(@char,cell2array(replicate(5,"X"))') int2str([1:5]')]


