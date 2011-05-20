function answers=assembler(directory)
    cd(directory);
    d = dir();
    answers = [];
    for i=3:length(d),
        disp(['Opening ' d(i).name '...']);
        load(d(i).name);
        answers = [answers, solutions];
    end
    cd('..');
end
