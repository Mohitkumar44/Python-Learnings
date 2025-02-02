with open("log.txt") as f:
    for i in range(1,100):
        c = f.readline()
        if "python" in c:
            print(f"found in line {i}")
            break
    else:
        print("not found")
    