print("\t\t\t\t\t\t\t\t\t\t Dice roller game  \t\t\t")


import random
DICE_OUTPUT = [1,2,3,4,5,6]

while(1):
    c = int(input("Game by pressing : \n 1.Play \n 2.Exit"))
    if c==1:

        print("Rolling a dice ")
        a = random.choice(DICE_OUTPUT)
        print(a)
        continue
    if c==2:
        print("GAME ENDS")
        break

    else:
        print("Invalid press")
        break
print("Over")




