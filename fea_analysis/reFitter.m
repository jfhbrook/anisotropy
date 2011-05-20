function fixed=reFitter(broked, r, params)
    fixed = broked;
    for i=1:length(fixed),
        fixed{i} = cellfun(@(kset) {fitHelper(kset{2}, r, params), kset{2}, kset{3}}, fixed{i}, 'UniformOutput', false);
    end
end

function fitted=fitHelper(tT, r, params)
    fitted = fitter(tT(1,:),tT(2,:),r, params);
end
