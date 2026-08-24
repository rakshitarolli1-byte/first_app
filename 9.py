import sys

class Complex:
    # Constructor of the class
    def __init__(self, realpart=0.0, imagpart=0.0):
        self.realpart = realpart
        self.imagpart = imagpart

    def readComplex(self):
        self.realpart = float(input("Enter real part: "))
        self.imagpart = float(input("Enter imaginary part: "))

    def __str__(self):
        return f"{self.realpart}+i{self.imagpart}"

    def __add__(self, c2):
        return Complex(self.realpart + c2.realpart,
                       self.imagpart + c2.imagpart)


compList = []

N = int(input("Enter the value of N (N >= 2): "))

if N < 2:
    print("Invalid input for N (N >= 2)")
    sys.exit()

for i in range(N):
    print("Complex Number", i + 1)
    num = Complex()
    num.readComplex()
    compList.append(num)

print("Entered Complex numbers are:")

for num in compList:
    print(num)

total = Complex()

for num in compList:
    total += num

print("Sum of %d complex numbers is %s" % (N, total))

