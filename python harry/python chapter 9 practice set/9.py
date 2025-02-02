with open("donkey.txt") as f:
    cont = f.read()
with open("this.txt") as f:
    cont1 = f.read()
if cont == cont1:
    print("both files are identical")
else:
    print("both files are different")