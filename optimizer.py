import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def f(x):
    y = (x-1.5)**2 + 0.5
    print "x={},y={}".format(x,y)
    return y

def test_run():
    x_guess = 2.0
    min_result = spo.minimize(f,x_guess,method='SLSQP',options={'disp':True})
    print  "Min found at:"
    print "x={},y={}".format(min_result.x,min_result.fun)

    #plot
    xPlot = np.linspace(0.5,2.5,21)
    yPlot = f(xPlot)
    plt.plot(xPlot,yPlot)
    plt.plot(min_result.x,min_result.fun,'ro')
    plt.title("min of an objective function")
    plt.show()

if __name__ == "__main__":
    test_run()