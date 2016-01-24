#q10_find_largest.py
#find largest integer n such that n^3 < 12000
import math

n = 1

while math.pow(n,3) < 12000:
    n+=1

print(n-1)
