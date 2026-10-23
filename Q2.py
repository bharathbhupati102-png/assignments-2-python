# 2) WAP to enter three sides of a triangle and find the area of the triangle.
import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("Area of triangle =", area)
else:
    print("Invalid triangle")