%creates a file and that's it.
function touch(filename)
   fid = fopen(filename, 'a');
   fclose(fid);
end
