class claculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the square of this no. is {self.n*self.n}")

    def cube(self):
        print(f"the cube of this no. is {self.n*self.n*self.n}")

    def square_root(self):
        print(f"the square root of this no. is {self.n**1/2}")

    @staticmethod
    def greet():
        print("Hello User")
a = claculator(4)
a.square()
a.cube()
a.square_root()
a.greet()