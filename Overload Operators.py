class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if (self.a<other.a):
            return "Ob1 is gretater"
        else:
            return "Ob2 is greter"
    def __eq__(self,other):
        if (self.a==other.a):
            return "Both are equel"
        else:
            return "They are not equel"
ob1 = A(2)
ob2 = A(3)
print("Passed Value : ",ob1.a,ob2.a)
print(ob1<ob2)
ob3 = A(4)
ob4 = A(4)
print("Passed Valu:",ob3.a,ob4.a )
print(ob3==ob4)
        