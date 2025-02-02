from random import randint

class train:
    def __init__(self,no):
        self.no = no
    def book(self,fro,to):
        print(f"your ticket for {fro} to {to} has been successfully booked in train {self.no}")
    def getstatus(self):
        print(f"your train {self.no} is on time")
    def getfare(self,fro,to):
        fare = randint(1000,5000)
        print(f"your train ticket price from {fro} to {to} is {fare}")
a = train(456456)
a.book("delhi","rampur")
a.getfare("delhi","rampur")
a.getstatus()