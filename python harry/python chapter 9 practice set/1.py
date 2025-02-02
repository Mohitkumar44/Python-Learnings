f = open("poem.txt")
content = f.read()
if "twinkle" in content:
    print("the word twinkle is present in file")
else:
    print("the word twinle is not present in the file")