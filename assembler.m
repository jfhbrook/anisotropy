function answers=assembler(directory)
    cd(directory);
    d = dir();
    load(d(3).name);
    answers = [solutions]
    for i=4:length(d),
        load(d(i).name);
        answers = [answers, solutions];
    end
end
