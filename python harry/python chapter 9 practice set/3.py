def generate_table(n):
    with open(f"Tables/table_{n}.txt","a") as f:
        for i in range(1,11):
            f.write(f"{n} x {i} = {n*i}\n")

for i in range(2,21):
    generate_table(i)