a = int(input("enter no. : "))
b = int(input("enter no. : "))
c = int(input("enter no. : "))

def greatest_no(a,b,c):
    if a>b and a>c:
        print(a)
    if c>b and c>a:
        print(c)
    if b>a and b>c:
        print(b)

greatest_no(a,b,c)