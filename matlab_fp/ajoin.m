function result=ajoin(array, string)
    % Inspired by str.join(') from python
    % returns an array with all the rows in the original array joined by 
    % `string` in reading order

    for m=1:size(array,1),
        if m==1,
            result=[arrayfun(@num2str, array(1,:))];
        else,
            result=[result string arrayfun(@num2str, array(m,:))];
        end
    end
end
