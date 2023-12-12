import random

def dice_roller():
    while True:
        print("Preparing to roll dice...")
        numod = input("How many dice are we rolling? ")
        numos = input("How many sides do the dice have? ")
        
        
def main():
    while True:
        print("Welcome to the Table Top Companion!")
        print("Please select one of the following:")
        print("1. Dice Rolling")
        print("2. Character Modifier")
        print("3. Roll History") 
        print("4. Exit the application")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            dice_roller()
        elif choice == "2":
            modifiers()
        elif choice == "3":
            roll_hist()
        elif choice == "4":
            print("Exiting the Word Games app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter either 1, 2, 3, or 4.")
            print("Quinn - So help me God if you use recursion to crash another app")

if __name__ == "__main__":
    main()