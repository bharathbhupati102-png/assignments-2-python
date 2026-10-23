# 4) WAP to enter the coefficients of a quadratic equation and find its roots
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Not a quadratic equation")
else:
    d = b*b - 4*a*c

    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print("Two distinct real roots:", r1, r2)
    elif d == 0:
        r = -b / (2*a)
        print("Two equal roots:", r)
    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / abs(2*a)
        print("Complex roots:", complex(real, imag),
              complex(real, -imag))