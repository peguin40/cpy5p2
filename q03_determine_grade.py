#q03_determine_grade.py
#determines grade

#input mark
mark = int(input("Enter score between 0 and 100:"))

#functions

def display_grade(a):
    if 70<=a<=100:
        print("Congratulations! You got an A!")
    elif 60<=a<=69:
        print("You got a B")
    elif 55<=a<=59:
        print("You got a C")
    elif 50<=a<=54:
        print("You got a D")
    elif 45<=a<=49:
        print("You got an E")
    elif 35<=a<=44:
        print("You got a F")
    elif 0<=a<=34:
        print("You got a U")

#process validity of input

if 0<=mark<=100:
    display_grade(mark)
else:
    print("Invalid score! Score must be between 0-100")
