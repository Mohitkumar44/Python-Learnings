import random
n = random.randint(1,100)
y = -1
guess = 1
while n != y:
    y = int(input("Guess a Number : "))
    if n>y:
        print("Higher Number Please")
        guess +=1
    elif n<y:
        print("Lower Number Please")
        guess +=1
print(f"You have guessed the number {n} in {guess} attempts")