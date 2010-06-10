function result=ajoin(array, string)
    % Inspired by str.join(') from python
    % returns an array with all the rows in the original array joined by 
    % `string` in reading order
    % TODO: add to-string conversions

    for m=1:size(array,1),
        if m==1,
            result=[amap(@num2str, array(1,:))];
        else,
            result=[result string amap(@num2str, array(m,:))];
        end
    end
end
