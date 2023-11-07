import random

class DiceRoller:
    def __init__(self):
        self = self
        self.comp_rolls = []
    
    def Roll(self, num_of_dice: int, num_of_sides: int):
        current_rolls = []

        for current_rolls in range(num_of_dice):
            self.comp_rolls.append(random.randint(1, self.num_of_sides))
            return self.comp_rolls

class DRApp:
    def __init__(self):
        self.dice_roller = DiceRoller

    def help(self):
        print("Greetings!")
        print("Commands:")
        print("0 exit")
        print("1 roll")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("Command:")
            if command == "0":
                break
            elif command == "1":
                num_of_dice = int(input("Okay, how many dice do we need?: "))
                num_of_sides = int(input("Gotcha, and how many sides do the dice have?: "))
                self.dice_roller.Roll(num_of_dice, num_of_sides)
                print(self.comp_rolls)

