# q02_triangle.py
#validates triangle and compute perimeter

#input variables

side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

#compute perimeter

def compute_perimeter(a,b,c):
    print(a + b + c)

#validate triangle

if (side1 + side2) > side3 and (side2 + side3) > side1 and (side3 + side1) > side2:
    compute_perimeter(side1,side2,side3)
else:
    print("Invalid Triangle! ")
