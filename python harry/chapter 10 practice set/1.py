class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("Harry",1200000,204101)
print(p.name,p.salary,p.pin,p.company)