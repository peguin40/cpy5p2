#q04_determine_leap_year.py
#input year

year = int(input("Enter Year: "))

#process data

if year % 4 == 0 and year % 100 != 0:
    print("Leap Year!")
elif year % 400 == 0:
    print("Leap Year")
else:
    print("Non-Leap Year")
