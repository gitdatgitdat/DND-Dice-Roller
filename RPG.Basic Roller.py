from random import randint

#Import the stuffs
#Take in dice type from user vs options given
#Return random result in that given range

#Add ability to roll multiple times? Combination of types of dice?

dice_type = int(input("What kind of dice are we rolling?: (4, 6, 8, 10, 12, or 20) "))
options = [4, 6, 10, 12, 20]

if dice_type in options:
    if dice_type == 4:
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
else:
    print("I'm sorry, that is not a supported option.")

