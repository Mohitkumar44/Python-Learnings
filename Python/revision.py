# a = int(input("enter no. 1 : "))
# b = int(input("enter no. 2 : "))
# print(a+b)


# side = int(input("enter side : "))
# print(side**2)


# a = float(input("enter no. 1 : "))
# b = float(input("enter no. 2 : "))
# print((a+b)/2)


# a = float(input("enter no. 1 : "))
# b = float(input("enter no. 2 : "))
# print(a>=b)


# name = input("Enter Name : ")
# print(len(name))


# name = input("Enter String : ")
# print(name.count("$"))


# marks = int(input("Enter Marks : "))
# if marks >= 90 and marks <= 100:
#     print("Grade : ")
# elif marks >= 80 and marks <= 90:
#     print("Grade : A")
# elif marks >= 70 and marks <= 80:
#     print("Grade : c")
# elif marks >= 0 and marks <= 70:
#     print("Grade : D")


# name = int(input("Enter Num : "))
# if  name % 2 == 0:
#     print("even")
# else:
#     print("odd")


# num1 = int(input("enter no.1 : "))
# num2 = int(input("enter no.2 : "))
# num3 = int(input("enter no.3 : "))

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2>num3:
#     print(num2)
# else:
#     print(num3)


# num1 = int(input("enter no. : "))
# if  num1 % 7 == 0:
#     print("Yes")
# else:
#     print("No")


# list = []

# mov1 = input("Enter Movie 1 : ")
# mov2 = input("Enter Movie 2 : ")
# mov3 = input("Enter Movie 3 : ")

# list.append(mov1)
# list.append(mov2)
# list.append(mov3)

# print(list)


# list = [ 4,5,7,8,5 ]
# list_ = list.reverse()
# print(list == list_)


# list = ["c","d","a","a","b","b","a"]
# print(list.count("a"))


# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)


# student = {
#     "name" : "shradha",
#     "score" : "90"
# }

# student.update({"kal":"bijli"})
# print(student)


# set = { 5,8,9 }
# set.pop()
# print(set)


# dict = {
#     "table":[ "a piece of furniture","listof facts & figures"],
#     "cat" : "a small animal"
# }
# print(dict)


# clas = {"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(clas))


# dict = {}

# fir = int(input("Enter Marks Of Phy. Subject : "))
# sec = int(input("Enter Marks Of chem. Subject : "))
# thi = int(input("Enter Marks Of Maths Subject : "))

# dict.update({"Physics" : fir,"Chemistry": sec , "Maths":thi })
# print(dict)


# set = {9,"9.0"}
# print(set)


# i=1
# while i<=100:
#     print(i)
#     i+=1


# i=100
# while i>0:
#     print(i)
#     i-=1


# t = int(input("Enter : "))
# i=1
# while i<=10:
#     print(t*i)
#     i+=1


# list = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx<len(list):
#     print(list[idx])
#     idx+=1


# list = [1,4,9,16,25,36,49,64,81,100]
# a=int(input("enter no. : "))
# idx = 0
# while idx<len(list):
#     if list[idx] == a:
#         print("Found at index ",idx)
#         break
#     else:
#         print("not found")
#     idx+=1


# i=1
# while i<=100:
#     if i % 3 == 0:
#         i+=1
#         continue
#     print(i)
#     i+=1


# list = [1,4,9,16,25,36,49,64,81,100]
# for el in list:
#     print(el)


# a = int(input("Enter No. : "))
# list = [1,4,9,16,25,36,49,64,81,100]
# for el in list:
#     if el == a:
#         print("found : ",el)
#     else:
#         print("finding...")


# for el in range(1,101):
#     print(el)


# for el in range(100,0,-1):
#     print(el)


# n = int(input("Enter Value of n : "))
# for el in range(1,11):
#     print(n*el)


# n = int(input("Enter No. : "))
# sum = 0
# i = 1
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)


# fact = 1
# n = int(input("Enter No. : "))
# for el in range(1,n+1):
#     fact*=el
# print(fact)


# def sum(a,b):
#     s=a+b
#     return s
# print(sum(2,3))


# a = [1,5,4,7]
# def print_length(list):
#     print(len(list))
# print_length(a)


# a = [1,5,4,7]
# def prt_line(list):
#     for el in list:
#         print(el,end = " ")

# prt_line(a)


# def fact(n):
#     mul = 1
#     for el in range(1,n+1):
#         mul*=el
#     print(mul)

# fact(5)


# def convert(usd):
#     inr=usd*83
#     print(inr,"INR")

# convert(82)


# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
    
# print(sum(15))


# a = [4,5,8,7,2,1,4,5,8,9,6,3,5,5]
# def prt(list,index):
#     while index<len(list):
#         print(list[index])
#         prt(list,index+1)
#         break
# prt(a,0)


# a = [4,5,8,7,2,1,4,5,8,9,6,3,5,5]
# def prt(list,index=0):
#     if index==len(list):
#         return
#     print(list[index])
#     prt(list,index+1)
# prt(a)


# f = open("pyq","r")
# print(f.read())


# f = open("practice.txt","x")
# f.write("Hi everyone \nwe are learning File I/O \nusing Java \nI like programming in Java")


# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java","Python")
# print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)


# with open("practice.txt","r") as f:
#     data = f.read()
#     if data.find("learning"):
#         print("yes")
#     else:
        # print("no")


def check_line():
    word = "learning"
    with open("practice.txt","r") as f:
        line = f.readline()
        
