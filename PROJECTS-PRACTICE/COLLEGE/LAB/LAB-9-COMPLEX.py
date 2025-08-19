class Complex: 
    def inputComplex(self):
        self.realpart = int(input("Enter real part"))
        self.imgpart = int(input("Enter img part"))
    def display(self):
        print(f"the complex num is {self.realpart}+{self.imgpart}i")
    def sum(self,c1,c2):
        self.realpart = c1.realpart + c2.realpart
        self.imgpart = c1.imgpart + c2.imgpart
c1 = Complex()
c2 = Complex()
c3 = Complex()

c1.inputComplex()
c1.display()
c2.inputComplex()
c2.display()
c3.sum(c1,c2)
c3.display()