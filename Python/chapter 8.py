# class car:
#     color = "blue"
#     brand = "mercedees"
# car1 = car()
# print(car.color)
# print(car.brand)



# class student:

#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new student in database")

# s1 = student("karan")
# print(s1.name)

# s2  = student("arjun")
# print(s2.name)



# class student:

#     def __init__(self,name ,marks):
#         self.name = name
#         self.marks = marks
#         print("Adding Data to Database")
#     def avrg(self):
#         sum = 0 
#         for val in self.marks:
#             sum += val
#         print("hi",self.name,"your avrg score is : ",sum/3)

# s1 = student("karan",[98,96,98])
# print(s1.name)
# print(s1.marks)
# s1.avrg()




# class account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no
#     def debit(self,withdraw):
#         self.balance -= withdraw
#         print(withdraw , "was debited")
#         print("final balance : ",self.bal())
#     def credit(self,credit):
#         self.balance += credit
#         print(credit,"was credited")
#         print("final balance : ",self.bal())
#     def bal(self):
#         return self.balance

# per1 = account(7000,12345)
# per1.debit(1000)
# per1.credit(500)































