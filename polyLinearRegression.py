import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def error_poly(C,data):
    """
    C: numpy.poly1d object
    data: 2d array each row is a point (x,y)
    """
    err = np.sum((data[:, 1] - np.polyval(C,data[:,0])) ** 2)
    return err

def fit_poly(data,error_func,degree=3):
    #generate initial guess for line model
    Cguess = np.poly1d(np.ones(degree+1,dtype=np.float32))

    #plot initial guess
    x = np.linspace(-5,5,21)
    plt.plot(x,np.polyval(Cguess,x),'m--',linewidth=2.0,label="Initial guess")

    #call optimizer to minimize error fucntion
    result = spo.minimize(error_func,Cguess,args=(data,),method='SLSQP',options={'disp':True})
    return np.poly1d(result.x)

def test_run():
    #define original line
    l_origin = np.float32([1.5,-10,-5,60,50])
    x_origin = np.linspace(-5,5,21)
    y_origin = l_origin[0] * x_origin **4 + \
               l_origin[1] * x_origin **3 + \
               l_origin[2] * x_origin **2 + \
               l_origin[3] * x_origin  + \
               l_origin[4]
    plt.plot(x_origin,y_origin,'b--',linewidth=2.0,label="Original line")

    #generate data points
    data = np.asarray([x_origin,y_origin]).T
    plt.plot(data[:,0],data[:,1],'go',label="Data points")

    #fit a line
    l_fit = fit_poly(data,error_poly)
    plt.plot(data[:,0],np.polyval(l_fit,data[:,0]),'r--',linewidth=2.0,label="Fitted line")
    plt.legend(loc='upper left')
    plt.show()

if __name__ == "__main__":
    test_run()