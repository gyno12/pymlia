from Ch05 import logRegres
from numpy import *

if __name__ == '__main__':
    a, b = logRegres.loadDataSet()
    w = logRegres.stocGradAscent1(array(a), b, 20)
    print w
    logRegres.plotBestFit(w)