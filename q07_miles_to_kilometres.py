#q07_miles_to_kilometres.py
#variables

miles1 = int(1)
kilometres1 = float(miles1 * 1.609)

kilometres2 = int(20)
miles2 = float(kilometres2 / 1.609)

#print headers
print("{1:^7}{0:^11}{0:^11}{1:^7}".format("Kilometres","Miles"))

#print values
for miles1 in range(1,11):
    print("{0:^7}{1:^11.3f}{2:^11}{3:^7.3f}".format(miles1,kilometres1,kilometres2,miles2))
    kilometres2+=5
    kilometres1 = float(miles1 * 1.609)
    miles2 = float(kilometres2 / 1.609)
