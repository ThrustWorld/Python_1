from math import sqrt

width = float(input("Base rettangolo: "))
height = float(input("Altezza rettangolo: "))

area = width * height
perimeter = (width + height) * 2
diagonal = sqrt((width ** 2 + height ** 2))

print("Area: %.2f " %(area), "Perimeter: ", perimeter, "Diagonal: %.2f" %(diagonal))