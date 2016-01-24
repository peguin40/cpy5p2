#q05_find_month_days.py
#Finds number of days from the month and year
import datetime

#get input
month = int(input("Input Month: "))
while month<0 or month>12:
    print("Error: Invalid month")
    month = int(input("Input Month: "))

year = int(input("Input Year: "))


#process values

if month == 2:
    if year % 4 == 0 and year % 100!=0:
        print("February {0} has 29 days".format(year))
    elif year % 400 == 0:
        print("February {0} has 29 days".format(year))
    else:
        print("February {0} has 28 days".format(year))
else:
    month_word = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"
                  , "November", "December"]
    month_word = str(month_word[month - 1])
    try:
        i=1
        for i in range(1,35):
            datetime.date(year,month,i)
    except ValueError:
        days = int(i-1)
        print("{0} {1} has {2} days".format(month_word,year,days))

