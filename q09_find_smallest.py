#q09_find_smallest.py
#find smallest integer such that n^2 is greater than 12000
import math

n = 1

while math.pow(n,2) <= 12000:
    n+=1

print(n)
