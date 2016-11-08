import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def error(line,data):
    """
    line: tuple/list/array (C0,C1) C0 is slope and C1 is y-intercept
    data: 2d array each row is a point (x,y)
    """
    err = np.sum((data[:, 1] - (line[0]*data[:, 0]+line[1])) ** 2)
    return err

def fit_line(data,error_func):
    #generate initial guess for line model
    l=np.float32([0,np.mean(data[:,1])])

    #plot initial guess
    x_ends = np.float32([-5,5])
    plt.plot(x_ends,l[0]*x_ends + l[1],'m--',linewidth=2.0,label="Initial guess")

    #call optimizer to minimize error fucntion
    result = spo.minimize(error_func,l,args=(data,),method='SLSQP',options={'disp':True})
    return result.x

def test_run():
    #define original line
    l_origin = np.float32([4,2])
    print "Original line: C0={},C1={}".format(l_origin[0],l_origin[1])
    x_origin = np.linspace(0,10,21)
    y_origin = l_origin[0] * x_origin + l_origin[1]
    plt.plot(x_origin,y_origin,'b--',linewidth=2.0,label="Original line")

    #generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0,noise_sigma,y_origin.shape)
    data = np.asarray([x_origin,y_origin+noise]).T
    plt.plot(data[:,0],data[:,1],'go',label="Data points")

    #fit a line
    l_fit = fit_line(data,error)
    print "Fitted line: C0={},C1={}".format(l_fit[0],l_fit[1])
    plt.plot(data[:,0],l_fit[0]*data[:,0]+l_fit[1],'r--',linewidth=2.0,label="Fitted line")
    plt.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()