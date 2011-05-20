function answers=brokedAssembler(directory)
%Assembles solutions from from first semi-successful run-through
%Soon won't be needed hopefully
    cd(directory);
    d = dir();
    answers = [];
    for i=3:length(d),
        disp(['Opening ' d(i).name '...']);
        load(d(i).name);
        solutions = solutions(1);
        answers = [answers, solutions];
    end
    cd('..');

    answers = reFitter(answers, params);

end

function fixed=reFitter(broked, params)
    fixed = broked;
    for i=1:length(fixed),
        fixed{i} = cellfun(@(kset) {fitHelper(kset{2}, params), kset{2}, kset{3}}, fixed{i}, 'UniformOutput', false);
    end
end

function fitted=fitHelper(tT, params)
    fitted = fitter(tT(1,:),tT(2,:),params);
end
