__auth__ = 'NguyenTTin'
'''
from pylab import plot,show

x_num = [1,3,4,5,6,7]
y_num = [1,9,16,25,36,49]
plot(x_num,y_num, '*')
show()
'''

import numpy as np
import matplotlib.pyplot as plt
from pylab import plot,show

x = np.linspace(0,10,100)
line = plt.plot(x,np.sin(x)*np.cos(2*x))
plt.show()