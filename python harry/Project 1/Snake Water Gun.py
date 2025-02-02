import random
computer = random.choice([1,-1,0])
youstr = input("Enter Your Choice : ")
youDict = {"s":1,"w":-1,"g":0}
Dict = {1:"snake", -1:"water", 0:"gun"}
younum = youDict[youstr]
print(f"You choose {Dict[younum]}")
print(f"Computer choose {Dict[computer]}")
if younum-computer == 0:
    print("Its a Draw!")
if younum-computer == -1 or younum-computer ==2:
    print("You Win!")
if younum-computer ==-2 or younum-computer ==1:
    print("You Lose!")