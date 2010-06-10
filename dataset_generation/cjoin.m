function result=cjoin(cellular, string)
    % Inspired by str.join(') from python
    % returns an array with all the boxes in the cell joined by 
    % `string` in reading order
    for m=1:size(cellular,1),
        for n=1:size(cellular,2),
            if m==1 && n==1,
                result=[cellular{1,1}];
            else,
                result=[result string cellular{m,n}];
            end
        end
    end
end
