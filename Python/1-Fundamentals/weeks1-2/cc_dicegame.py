import random

high_score = 0


def dice_game():
    global high_score

    dice_roll = random.randint(1, 6)
    print(f"You rolled a {dice_roll}.")

    if dice_roll > high_score:
        high_score = dice_roll

    print(f"Current high score: {high_score}")


if __name__ == "__main__":
    while True:
        print("Current High Score:")
        print("1. Roll Dice")
        print("2. Leave Game")
        print("Enter your choice: ")

        choice = input()

        if choice == "1":
            dice_game()
        elif choice == "2":
            break
        else:
            print("Invalid choice.")
