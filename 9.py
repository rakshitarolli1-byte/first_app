import sys
class complex:
    #constructor of the class
    def__init__(self, realpart=0.0, imagpart=0.0):
        self.realpart=realpart
        self.imagpart=imagpart
    def_str_(self):
        return f"{self.realpart}+i{self.imagpart}"
    def_add_(self, c2):
        return Complex(self.realpart+c2.realpart,self.imagpart+c2.imagpart)
compList=[]
N=int(input("Enter the value of N(N>=2):"))
if N<2:
    print("Invalid input for N(N>=2):")
    sys.exit()
for i in range(N):
    print("complex Number",i+1)
    num=Complex()
    num.readComplex()
    compList.append(num)
print("Entered Complex numbers are:")
for num in compList:
    print(num)
total=Complex()
for num in compList:
    total += num
print("sum of %d complex numbers is %s"%(N,total))
    
        
