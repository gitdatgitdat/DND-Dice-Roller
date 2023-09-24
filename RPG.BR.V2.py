import random

print("Greetings,")
dice_type = int(input("How many sides do the dice have? "))
dice_num = int(input("And how many of those are we rolling? "))
current_rolls = []

for i in range(dice_num):
    current_rolls.append(random.randint(1, dice_type))        

print(f'Okay! You rolled: {current_rolls}')
