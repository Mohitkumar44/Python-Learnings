# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("12345","abcde")

# print(acc1.acc_no)
# acc1.reset_pass()


# class person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()
# p1 = person()

# p1.welcome()




# class circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2
    
#     def perimeter(self):
#         return 2*(22/7)*self.radius

# c1 = circle(21)
# print(c1.radius)
# print(c1.area())
# print(c1.perimeter())




# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
         
#     def showdetails(self):
#         print("Role : ",self.role)
#         print("dept : ",self.dept)
#         print("salary : ",self.salary)


# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","75,000")

# e1 = Employee("clean","safaikarmi","50,000")
# e1.showdetails()


# eng1 = Engineer("Elom Musk",40)
# eng1.showdetails()




# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price

#     def __gt__(sel,odr2):
#         return odr1.price > odr2.price 



# odr1 = Order("book",500)

# odr2 = Order("pen",10)

# print( odr1 > odr2)