import tablib
import re
#from enthought.mayavi import mlab
#from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot
from numpy import array, meshgrid, unique, floor, abs

table = tablib.Dataset()
#This having-to-extract-spaces stuff? Not gudt!
#Note: This csv has been pre-sorted with gnumeric.
table.csv = re.sub(' ', '', open('data_stripped.csv').read())

# fyi
# > print( table.headers )
# ['angle', 'kxy', 'kz', 'kmeas']

#This is a way to compute normalized values a'priori
#Keeps them good to 3 decimals
table.append(col = ['kz_n']
                   + map(lambda x,y: str(floor(1000*float(x)/float(y))/1000),
                         table['kz'], table['kxy']) )
table.append(col = ['kmeas_n']
                   + map(lambda x,y: str(floor(1000*float(x)/float(y))/1000),
                         table['kmeas'], table['kxy']) )

#Note, dtype is string. Will have to convert.
nptable = array(table._data)

#Used to weed out obvious garbage values--need to be more careful with this in the future
#print (array(table['angle']) == '90')*(abs(array(map(float,table['kmeas_n'])) - 1.1) > 0.11)

#Plotting surfs
#Doesn't work with my mpl and pip has promblems
"""
for kxy in unique(table['kxy']).tolist():
    relevant_rows = nptable[nptable[:,1] == kxy,:]
    x = array([ map(float,relevant_rows[:,0]) ])
    y = array([ map(float,relevant_rows[:,4]) ])
    z = array([ map(float,relevant_rows[:,5]) ])
    axes = pyplot.figure().add_subplot(111)
    axes.contour(x,y,z)
pyplot.show()
"""

#Plotting not-so-surfs
for kratio in unique(table['kz_n']).tolist():
    #print kratio
    relevant_rows = nptable[nptable[:,4] == kratio,:]
    pyplot.plot(map(float,relevant_rows[:,0]),
               map(float,relevant_rows[:,5]), '*-', label=kratio)
pyplot.legend(loc=5)
pyplot.show()
