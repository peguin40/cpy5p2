#q12_find_factors.py
#find smallest factors of integer

#input variable
integer = int(input("Enter Integer: "))
integer1 = integer

x = -1
factors = []

#find smallest factors
while integer != 1:
    i = 2
    
    while integer % i != 0: # finds a factor
        i+=1
    integer = integer / i
    
    x += 1 #index of factor found
    
    factors.insert(x,i) #insert factor found into list of factors


#display results
print("Smallest factors of {0} are {1}".format(integer1,factors))
