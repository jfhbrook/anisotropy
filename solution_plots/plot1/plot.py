from numpy import array, meshgrid, zeros
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
#from scipy.interpolate import bisplrep, bisplev
import csv


with open('./data_fea.csv') as f:
    fea = []
    for row in csv.reader(f):
        fea.append(row)
    fea = map(lambda x: array(x, dtype='float64'), zip(*fea))
    #data.csv = csv.read()

with open('./gridded.csv') as f:
    gridded = []
    for row in csv.reader(f):
        gridded.append(row)
    gridded = array(zip(*gridded), dtype='float64')
   
headers = ['angle', 'k_z', 'k_meas']

figure = plt.figure()
axes = figure.add_subplot(111, projection='3d')
(xn, yn, zn) = fea
xn = fea[0]
yn = fea[1]
zn = fea[2]

xg = gridded[0, 1::]
yg = gridded[1::, 0]
zg = gridded[1::, 1::]

(xg, yg) = meshgrid(xg, yg)

axes.scatter(xn, yn, zn, c='k', marker='o')
axes.plot_surface(yg, xg, zg, rstride=1,
                              cstride=1,
                              cmap = cm.winter,
                              linewidth = 0,
                              shade = True)

#If I can fix griddata
#(xmesh, ymesh) = meshgrid(arange(0, 90, 10), arange(0.6, 1.6, 0.2))
#zmesh = griddata((x,y), z, (xmesh, ymesh), method='cubic')


axes.set_xlabel(headers[0])
axes.set_ylabel(headers[1])
axes.set_zlabel(headers[2])

plt.show()

