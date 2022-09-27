#Ai is a bit smarter

import random

print("~ Welcome! ~")
print("==========")
stones = -1
stones = random.randint(15, 35)
player = "PLY"
user = ""
historyDict = {}
history = 0
num = -1
comp = -1

while(True):
    if player == "PLY":
        print("There are "+str(stones)+" remainding.")
        while(True):
            user = input("Enter a number (1-3): ")
            if user.isnumeric():
                num = int(user)
                if num > 0 and num < 4:
                    break
                else:
                    print("Make sure your number is between 1 & 3.")
            else:
                print("Please type a number.")

        stones -= num
        historyDict[history] = (""+str(history)+"    "+str(player)+"   "+str(stones)+"   "+str(num)+" ")

        print()
        print()
        for i in range(len(historyDict)):
            print(historyDict[i])

        if stones == 0:
            print ("You Win! :)")
            break
        else:
            history += 1
            player = "COM"


    if player == "COM":
        if stones <= 3:
            ran = random.randint(1, 3)
            if ran == 1 or ran == 2:
                comp = stones
        else:
            comp = random.randrange(1, 3)

        print("There are "+str(stones)+" remainding.")
        input("The computer choose to removed "+str(comp)+" stone(s). [Enter to continue]")
        stones -= comp
        historyDict[history] = (""+str(history)+"    "+str(player)+"   "+str(stones)+"   "+str(num)+" ")
        
        print()
        print()
        for i in range(len(historyDict)):
            print(historyDict[i])
        
        if stones == 0:
            print("You lost :( ")
            break
        else:
            history += 1
            player = "PLY"


print("Game has ended. Come back soon")
