function plotkvals(k_cells)
%Meant to plot ellipsoids for all the k-cells.
%Not very useful in matlab, as it turns out.
imax=size(k_cells,1);
jmax=size(k_cells,2);
    for i=1:imax,
        for j=1:jmax,
            subplot(imax,jmax,j+jmax*(i-1));
            m_ellipsoid(fromsymmcells(k_cells{i,j}));
            axis([-3 3 -3 3 -3 3]);
        end
    end
end
