n=int(input("enter a number : "))

table = [n*i for i in range(1,11)]
with open("file.txt","a") as f:
    f.write(f"Table of {n} is {str(table)} \n")