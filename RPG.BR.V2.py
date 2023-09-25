import random

print("Greetings,")
dice_num = int(input("How many dice are we rolling? "))
side_num = int(input("How many sides do the dice have? "))
current_rolls = []
comp_rolls = []

for current_rolls in range(dice_num):
    comp_rolls.append(random.randint(1, side_num))        
    comp_rolls.sort()

print(f'Okay! You rolled: {comp_rolls}')


