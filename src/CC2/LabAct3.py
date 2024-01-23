import math

line = "-"*5

print(line,"SQUARE",line)
side = float(input("Enter the length of the side: "))
area_of_square = pow(side,2)
print(f"The area of a square with side length {side} is {round(area_of_square,2)}.")
print()

print(line,"RECTANGLE",line)
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area_of_rectangle = length*width
print(f"The area of a rectangle with length {length} and width {width} is {area_of_rectangle}.")
print()

print(line,"CIRCLE",line)
radius = float(input("Enter the radius: "))
area_of_circle = math.pi * pow(radius,2)
print(f"The area of a circle with radius {radius} is {round(area_of_circle,2)}.")
print()

print(line,"TRIANGLE",line)
side1 = float(input("Enter the length of the side A: "))
side2 = float(input("Enter the length of the side B: "))
side3 = float(input("Enter the length of the side C: "))
s = (side1+side2+side3)/2
area_of_triangle = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(f"The area of a triangle with side A {side1}, side B {side2}, and side C {side3} is {round(area_of_triangle,2)}.")
print()

print(line,"PARALLELOGRAM",line)
base = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))
area_of_parallelogram = height*base
print(f"The area of a parallelogram with base {base} and height {height} is {area_of_parallelogram}.")
print()

print(line,"TRAPEZOID",line)
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height: "))
area_of_trapezoid = ((base1+base2)/2)*height
print(f"The area of a trapezoid with first base {base1}, second base {base2}, and height {height} is {area_of_trapezoid}.")
print()

print(line,"ELLIPSE",line)
axis1 = float(input("Enter the length of the major axis: "))
axis2 = float(input("Enter the length of the minor axis: "))
area_of_ellipse = math.pi*axis1*axis2
print(f"The area of a ellipse with major axis {axis1} and minor axis {axis2} is {round(area_of_ellipse,2)}.")
