list = [ "donkey","you"]
def rem(lst):
    with open("donkey.txt") as f :
        content = f.read()
    for i in range(len(lst)):
        content = content.replace(lst[i],"#"*len(lst[i]))
    with open("donkey.txt","w") as f :
        f.write(content)
rem(list)