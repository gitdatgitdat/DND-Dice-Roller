import random

class DiceRoller:
    def __init__(self):
        self.history = []

    def roll_dice(self, num_dice, num_sides, bonus, action_description):
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        rolls_with_bonus = [roll + bonus for roll in rolls]
        result = {
            'dice_type': f'D{num_sides}',
            'num_dice': num_dice,
            'rolls': rolls_with_bonus,
            'action_description': action_description
        }
        self.history.append(result)
        return result

    def view_history(self):
        if not self.history:
            print("No rolls in the history.")
            return

        print("\nRoll History:")
        for i, roll in enumerate(self.history, start=1):
            print(f"\nRoll #{i}")
            print(f"Action: {roll['action_description']}")
            print(f"Dice: {roll['dice_type']}, Num Dice: {roll['num_dice']}")
            print(f"Rolls with Bonus: {roll['rolls']}")
        print()

    def clear_history(self):
        self.history = []
        print("Roll history cleared.")

def main():
    dice_roller = DiceRoller()

    while True:
        print("\nWelcome! Please select one of the following:")
        print("1. Roll dice")
        print("2. Roll history")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            num_sides = int(input("Select die type (4, 6, 8, 10, 12, 20): "))
            num_dice = int(input("Select number of dice (1-10): "))
            add_bonus = input("Do you want to add a bonus value? (1 = yes, 2 = no): ")
            bonus = int(input("Enter the bonus value: ")) if add_bonus == '1' else 0
            action_description = input("Enter action description: ")

            result = dice_roller.roll_dice(num_dice, num_sides, bonus, action_description)
            print("\nRoll Results:")
            for i, roll_value in enumerate(result['rolls'], start=1):
                print(f"Roll {i}: {roll_value}")
            print()

            roll_again = input("Roll again? (1 = yes, 2 = no): ")
            if roll_again != '1':
                continue

        elif choice == '2':
            print("\nHistory Options:")
            print("1. View past rolls")
            print("2. Clear past rolls")
            print("3. Return to main")

            history_choice = input("Enter your choice (1-3): ")
            if history_choice == '1':
                dice_roller.view_history()
            elif history_choice == '2':
                dice_roller.clear_history()
            elif history_choice == '3':
                continue

        elif choice == '3':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()