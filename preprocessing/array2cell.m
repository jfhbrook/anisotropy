function a=array2cell(A)
    a=cell(size(A,1),size(A,2));
    %converts an array to a 2-d cell structure
    for m=1:size(A,1),
        for n=1:size(A,2),
            a{m,n}=A(m,n);
        end
    end
end
