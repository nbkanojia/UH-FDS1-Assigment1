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

ohist, oedge = np.histogram(data, bins=32)


# calculate bin centre locations and bin widths
xdst= (oedge[1:]+oedge[:-1])/2
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


#The value of X should be such that 33% of people have a salary above X.
indx=np.argmin(np.abs(cdst-0.67))
xlow=oedge[indx]

plt.bar(xdst[indx:],ydst[indx:], width=0.9*wdst[indx:], color='green')

#find the fraction of claims £5k+
hdst=ydst*(xdst >= 56003)
#plt.bar(xdst, hdst, width=0.9*wdst, color='orange')



plt.plot([xlow,xlow],[0.0,max(ydst)], c='orange')
text = ''' 33% of people have a \nsalary above {}'''.format(xlow.astype(int))
plt.text(x=xlow+xlow*0.10, y=max(ydst)-0.012, s=text, fontsize=12, c='orange')

#plt.figure(1)
#plt.hist(data, bins=32, edgecolor='w',density=True)
#plt.xlabel('Claim value, £', fontsize=15)
#plt.ylabel('Probability', fontsize=15)

plt.show()