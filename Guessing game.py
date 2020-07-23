import random
print("Play Guessing Game ")
# print("\t\t\t\t\t\t\t\t Guessing Game\t\t\t")

# print(pc_choice)
pc_choice = random.randrange(0, 21)
while (1):


    my_choice = int(input("Enter your guess till 0- 20 "))
    if my_choice == pc_choice:
        print("Correct \n The number is ",pc_choice)
        break


    if my_choice>pc_choice:
        print("Try a smaller number")

    if my_choice<pc_choice:
        print("Try greater number")

    

    continue

print("Game Over")
