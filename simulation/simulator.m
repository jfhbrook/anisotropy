%This is a script that iterates through k_mats
%and sends it to comsol().
flreport('off');

%preprocessing.m
load ../data/k_mats

%Always something there to store results in...
%k_results=cell(size(k_mats));

%have some results half-done
load ../data/k_results


for i=1:size(k_results,1),
    for j=1:size(k_results,2),
    	if size(k_results{i,j},1)>0,
    		fprintf('Already calculated for k(%i,%i)...\n',i,j);
    	else,
    	        fprintf('Running comsol model on k(%i,%i)...', i , j);
            	k_results{i,j}=comsol(k_mats{i,j})
    	        fprintf('finished.\n');
            	fprintf('Saving data...');
    	        save k_results k_results
            	fprintf('Done.\n\n');
                %code for printing out results
                %I have it teh commented.
    	        %fprintf('Printing result for k(%i,%i):', i,j);
            	%k_results{i,j}
    	        %fprintf('\n\n\n')
    	end
    end
    touch('down') %Rocketman!
end

exit
