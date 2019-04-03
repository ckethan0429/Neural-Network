import numpy as np
a = np.asarray([ [1,2,3], [4,5,6],[7,8,9] ])

a.tofile('foo.csv', sep = ',' , format='%10.5f')
#또는 np.savetxt('bar.csv', a, fmt='%10.5f', delimiter = ',')