# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:07:41 2023

@author: Nisarg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    data = np.genfromtxt('data1-1.csv', delimiter=',')
    return data



###### Main Function ######

data = read_data()
print(np.count_nonzero(data))

ohist, oedge = np.histogram(data, bins=32)


# calculate bin centre locations and bin widths
xdst=0.5*(oedge[1:]+oedge[:-1])
wdst=oedge[1:]-oedge[:-1]

# normalise the distribution
#ydist is a discrete PDF
ydst = ohist/np.sum(ohist)

#cumulative distribution
cdst=np.cumsum(ydst)

plt.figure(0)

# Plot the PDF
plt.bar(xdst, ydst, width=0.8*wdst)

plt.xlabel('Salaries in some European country', fontsize=15)
plt.ylabel('Probability', fontsize=15)


#Mean value
xmean=np.sum(xdst*ydst)
#and plot it
plt.plot([xmean,xmean],[0.0,max(ydst)], c='red')
text = ''' Mean value: {}'''.format(xmean.astype(int))
plt.text(x=xmean, y=max(ydst), s=text, fontsize=12, c='red')


plt.show()