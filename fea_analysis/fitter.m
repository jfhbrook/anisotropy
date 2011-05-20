function k = fitter(t,T,rset,params)
    logt = log(t(t>1));
    T = T(t>1);

    disp('Finding linear portion...');    
    for i=1:length(logt)-1
        C = corrcoef(logt(i:length(logt)), T(i:length(T)));
        r = sqrt(C(2,1));
        if r > rset %adjust this to get 'good' values
            disp(['linear fitting to ' num2str((length(logt)-i)) ' points from t=' num2str(exp(logt(i))) ' to t=' num2str(exp(logt(length(logt)))) '...']);
            x = polyfit(logt(i:length(logt)),T(i:length(T)), 1);
            break
        end
    end

    %plot(logt,T,'*');
    %hold on;
    %plot(logt, x(1)*logt + x(2));
    k = (params.q_needle)/(4*pi*x(1));

end
