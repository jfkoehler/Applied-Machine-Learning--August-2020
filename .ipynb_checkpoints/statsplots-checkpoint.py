
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from ipywidgets import interact
import ipywidgets as widgets
from scipy import stats

def one_d_plotter(pop_mean, sample_mean, i, j):  
    c = '#fcba03'
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    y1 = np.random.normal(loc = pop_mean, scale = 1, size = 10_000)
    y2 = np.random.normal(loc = sample_mean, scale = 1, size = 10_000)

    hist1, bins1 = np.histogram(y1, bins = 30)
    hist2, bins2 = np.histogram(y2, bins = 30)

    x1 = (bins1[:-1] + bins1[1:])/2
    x2 = (bins2[:-1] + bins2[1:])/2

    ax.bar(x1, hist1, zs=0, zdir='y', color=c, ec=c, alpha=0.8)
    ax.bar(x2, hist2, zs = 1, zdir = 'y')
    ax.plot(np.zeros(len(x1)), np.ones(len(x1))*np.mean(x1), np.zeros(len(x2)), color = 'red')
    ax.set_ylim(-1, 1)
    ax._axis3don = False
    ax.view_init(i, j)
    ax.set_title('Difference in Means')
    

def two_d_plotter(vmean, i, j, c = '#fcba03'):  
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    y1 = np.random.normal(loc = vmean, scale = 1, size = 10_000)
    y2 = np.random.normal(loc = vmean+1, scale = 1, size = 10_000)
    y3 = np.random.normal(loc = vmean+2, scale = 1, size = 10_000)

    hist1, bins1 = np.histogram(y1, bins = 30)
    hist2, bins2 = np.histogram(y2, bins = 30)
    hist3, bins3 = np.histogram(y3, bins = 30)

    x1 = (bins1[:-1] + bins1[1:])/2
    x2 = (bins2[:-1] + bins2[1:])/2
    x3 = (bins3[:-1] + bins3[1:])/2
    
    ax.bar(x1, hist1, zs=0, zdir='y', color=c, ec=c, alpha=0.8)
    ax.bar(x2, hist2, zs = 1, zdir = 'y', color = c, ec = c, alpha = 0.8)
    ax.bar(x3, hist3, zs=2, zdir='y', color=c, ec=c, alpha=0.8)
    ax.set_ylim(-1, 1)
    ax._axis3don = False
    ax.view_init(i, j)
    #ax.set_title('Linear Regression Setting')
    plt.title('$\mu_y = b_0 + b_1 * x$')