import random

pips = random.randint(1, 6)
print("You roll the die...it lands with...", pips, "pips showing.")


prizes = ["Tesla Model 3", "$10,000 ", "1 year Prime Subscription", "$100 "]
prizes_won = random.choice(prizes)
print("You've spun the wheel...and it lands on a prize of", prizes_won + "!!!")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print("You've shuffled the cards!!!")
print(cards)
