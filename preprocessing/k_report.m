function k_report(k_mats_props, filename)
    %takes k_mats_props and generates a human-readable report.
    %k_report(k_mats_props, filename)
    fopen('k_report.txt', 'w');
    for i=1:size(k_mats_props,1),
        for j=1:size(k_mats_props,2),
            f
end