from random import randint

#Import the stuffs
#Take in dice type from user vs options given
#Return random result in that given range

#Add ability to roll multiple times? Combination of types of dice?
#Add ability to 

dice_type = int(input("What kind of dice are we rolling?: (2, 3, 4, 6, 8, 10, 12, 20, or 100) "))
options = [2, 3, 4, 6, 10, 12, 20, 100]

if dice_type in options:
    if dice_type == 2:
        print("The result of the throw:", randint(1, 2))
    elif dice_type == 3:
        print("The result of the throw:", randint(1, 3))
    elif dice_type == 4:
        print("The result of the throw:", randint(1, 4))
    elif dice_type == 6:
        print("The result of the throw:", randint(1, 6))
    elif dice_type == 8:
        print("The result of the throw:", randint(1, 8))
    elif dice_type == 10:
        print("The result of the throw:", randint(1, 10))
    elif dice_type == 12:
        print("The result of the throw:", randint(1, 12))
    elif dice_type == 20:
        print("The result of the throw:", randint(1, 20))
    elif dice_type == 100:
        print("The result of the throw:", randint(1, 100))
else:
    print("I'm sorry, that is not a supported option.")

