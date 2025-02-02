import random
n= random.randint(1,100)
y=-1
guess = 1
while y!=n:
    y = int(input("Guess a Number : "))
    if y<n:
        print("Higher number please")
        guess +=1
    elif y>n:
        print("Lower number please")
        guess +=1
print(f"Your have Guessed the number {n} in {guess} attempts")