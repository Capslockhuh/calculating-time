# calculating-time.py - loops through integers from 1 to 99,999 and calculates their product while also measuring the time it took

from math import prod
import time

def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd
endTime = time.time()
print('The result is %s digits long' % (len(str(prod))))
print('This took %s seconds to calculate' % (endTime - startTime))

