import math

def exp(x, terms=10):
    sine = 0
    for n in range(terms):
        sign = (-1) ** n
        sine += (sign * (x ** (2 * n + 1))) / math.factorial(2 * n + 1)
    return sine

def degtorad(degrees):
    return degrees * (math.pi / 180)

degrees = float(input("Enter the angle in degrees: "))
radians = degtorad(degrees)
sine_value = exp(radians)
print(f"sin({degrees} degrees) = {sine_value}")