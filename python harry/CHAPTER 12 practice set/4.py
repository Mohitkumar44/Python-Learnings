try:
    a= int(input("enter value of a : "))
    b= int(input("enter value of b : "))
    print(a/b)
except ZeroDivisionError as e:
    print("infinite")