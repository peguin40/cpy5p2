#q11_find_gcd.py
#find greatest common divisor of 2 integers

#input variables
n1= int(input("First Integer: "))
n2 = int(input("Second Integer: "))

#find greatest common divisor

d = n1    
    

while n1 % d != 0 or n2 % d != 0:
    d-=1

print("Greatest Common Divisor of {0} and {1} is {2}! ".format(n1,n2,d))
    
