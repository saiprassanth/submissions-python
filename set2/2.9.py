'''table containing newtons square root and math square root and their difference
saiprassanth.ramesh@accenture.com
5dec2017'''
import math
def newtonsqrt(a):
    a = float(a)  
    x = a / 2  
    y = (x + a / x) / 2 
    return y
def mathsqr(n):
    n = float(n)
    return math.sqrt(n)
def printout():
    print '|{:<6}\t|{:<12}\t|{:<12}\t|{}'.format('number','newtonsqrt', 'math.sqr','difference')
    print '--------------------------------------------------------------'
    for i in range(1, 10):
        n = newtonsqrt(i)
        m = mathsqr(i)
        ab = abs(n - m)
        print '|{:<6}\t|{:<12}\t|{:<12}\t|{}'.format(i,n, m, ab)
printout()