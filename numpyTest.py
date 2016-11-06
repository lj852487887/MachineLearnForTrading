import numpy as np
import math

def test_run():
    print np.empty(5)
    print np.ones((4,5),dtype=int)
    print np.random.random

def compute():
    p1 = 0.666
    p2 = 0.333
    entropy = -p1*math.log(p1,2)-p2*math.log(p2,2)
    print entropy
    print 1-0.9184*3/4

if __name__ == "__main__":
    #test_run()
    compute()