# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:07:41 2023

@author: Nisarg
"""

import numpy as np
import matplotlib.pyplot as plt


def read_data():
    """
    Return the read csv file return salar.

    Returns
    -------
    data : numpy array
        return ther numby array list.

    """
    # read csv file
    data = np.genfromtxt('data1-1.csv', delimiter=',')
    return data


def calculate_bin_size(data):
    """
    Use the Freedman-Diaconis rule calcualte the bin size for givin data.

    Parameters
    ----------
    data : numpy array
        bin size calculate for data

    Returns
    -------
    bin_size : int
        calculated bin size.

    """
    # Calculate bin size using Freedman-Diaconis rule
    iqr = np.percentile(data, 75) - np.percentile(data, 25)
    bin_width = int(2 * iqr / (len(data) ** (1/3)))
    bin_size = np.ceil((max(data) - min(data))/bin_width).astype(int)
    print("bin_size", bin_size)
    return bin_size


def calculate_pdf(pdf_data):
    """
    Calculate the psd mean.

    Parameters
    ----------
    pdf_data : numpy array
        data for which pdf to be calculated.

    Returns
    -------
    xdst : int
        bin centre locations.
    ydst : int
        ydist is a discrete PDF.
    wdst : int
        width of bins.
    cdst : int
        cumulative distribution.
    oedge : int
        bin edges.
    xmean : int
        mean value.

    """
    # get the bin size
    bin_size = calculate_bin_size(pdf_data)
    ohist, oedge = np.histogram(data, bins=bin_size)

    # calculate bin centre locations and bin widths
    xdst = (oedge[1:]+oedge[:-1])/2
    wdst = oedge[1:]-oedge[:-1]

    # normalise the distribution
    # ydist is a discrete PDF
    ydst = ohist/np.sum(ohist)

    # cumulative distribution
    cdst = np.cumsum(ydst)

    # Mean value
    xmean = np.sum(xdst*ydst).round(2)
    print("Mean : ", data.mean())
    print("PDF Mean(W) : ", xmean)

    return xdst, ydst, wdst, cdst, oedge, xmean


def calculate_salary_below_33(cdst, oedge):
    """
    calculate the value of X should be such that 33% of\
people have a salary above X

    Parameters
    ----------
    cdst : int
        cumulative distribution..
    oedge : int
        bin edges.

    Returns
    -------
    xlow : float
        salary.
    indx : inr
        position of bar.

    """
    # The value of X should be such that 33% of people have a salary above X.
    indx = np.argmin(np.abs(cdst-0.67))
    xlow = oedge[indx].round(2)
    print("X:", xlow)
    return xlow, indx


def plot_graph(plot_data):
    """
    plot the graph and display values on it.

    Parameters
    ----------
    data : numpy array
        DESCRIPTION.

    Returns
    -------
    None.

    """
    xdst, ydst, wdst, cdst, oedge, xmean = calculate_pdf(plot_data)

    plt.figure(0, dpi=300)

    # Plot the PDF
    plt.bar(xdst, ydst, width=0.8*wdst)

    plt.xlabel('Salary', fontsize=15)
    plt.ylabel('Probability', fontsize=15)
    plt.title("Salaries distribution of European country")

    # and plot it
    text = ''' Mean value(W): {}'''.format(xmean.astype(float))
    plt.plot([xmean, xmean], [0.0, max(ydst)], c='red', label=text)

    xlow, indx = calculate_salary_below_33(cdst, oedge)

    plt.bar(xdst[indx:], ydst[indx:], width=0.9*wdst[indx:], color='green')

    text =  \
        ''' 33% of people have a \nsalary above(X) {}'''.format(
            xlow.astype(float))
    plt.plot([xlow, xlow], [0.0, max(ydst)], c='orange', label=text)

    plt.legend()
    plt.savefig("22085391.png", dpi=300)
    plt.show()


###### Main Function ######

# read the csv data
data = read_data()

# calculate the pdf and plot the graph
plot_graph(data)
