"""
1. Prompt the user to input either enter to pick a card, or Q plus enter to quit.
2. If the user input is "Q" then break out of the while loop.
3. Otherwise, think of a way to use a method from the random module such that a random card is selected from the diamonds list.
4. Use list methods to remove that card from the diamonds list, then add it to the hands list.
5. Print the contents of both decks. 
6. After the while loop ends, use an if statement to check the condition not diamonds like so:
    if not diamonds:
This statement will evaluate as True if the diamonds list is empty. 
Inside this if statement's body, print the string "There are no more cards to pick."
"""


import random


diamonds = [
    "AD",
    "2D",
    "3D",
    "4D",
    "5D",
    "6D",
    "7D",
    "8D",
    "9D",
    "10D",
    "JD",
    "QD",
    "KD",
]
hand = []


while diamonds:
    user_choice = input("Select 'Enter' to pick a card or 'Q' to quit.")

    if user_choice == "Q":
        break

    if user_choice == "":
        random_diamond = random.choice(diamonds)
        print(f"You have selected {random_diamond}")
        hand.append(random_diamond)
        diamonds.remove(random_diamond)
        print(f"You have {hand} in your hand")
        print("&")
        print(f"The remaining cards in your deck are {diamonds}")

    if not diamonds:
        print("There are no more cards to pick.")

    elif user_choice != "" and user_choice != "":
        print("Invalid Selection")
