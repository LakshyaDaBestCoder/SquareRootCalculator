import math as m

def calculateSquareRoot():
    number=float(input("Of which number do you want to find Square Root?").strip())
    sq=m.sqrt(number)
    print("The Square root of",number,"is",sq)
calculateSquareRoot()