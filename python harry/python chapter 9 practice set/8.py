with open("donkey.txt") as f:
    cont = f.read()

with open("this.txt","w") as f:
    f.write(cont)