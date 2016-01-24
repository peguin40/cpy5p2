#q06_kilograms_to_pounds.py
#variables

kilograms = 1
pounds = int(2.2*kilograms)

#print header
header1 = "Kilograms"
header2 = "Pounds"
print("{0:^11}{1:^8}".format(header1,header2))

#print table
for kilograms in range(1,10):
    print("{0:^11}{1:^8.1f}".format(kilograms,pounds))
    pounds = float(2.2 * (kilograms + 1))
