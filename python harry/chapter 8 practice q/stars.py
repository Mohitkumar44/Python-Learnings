n = int(input("enter no. : "))
def stars(n):
    if n==0:
        return 0
    print("*"*n)
    stars(n-1)
stars(n)