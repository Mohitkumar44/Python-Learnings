class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,nxt):
        return complex(self.r + nxt.r , self.i + nxt.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = complex(1,2)
c2 = complex(3,4)
print(c1+c2)