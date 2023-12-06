import random

def guess_random_number(tries, start, stop):
    global random_number
    random_number = random.randint(start, stop)
    while tries > 0:
        print(f"You have {tries} tries remaining.")
        try:
            guess = int(input(f"Guess a number between {start} and {stop}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        tries -= 1
        if guess == random_number:
            print("You guessed the correct number!")
            return guess
        elif guess < random_number:
            print("Guess Higher!")
        else:
            print("Guess Lower")
    return -1

def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print(f"The number to guess is: {random_number}")

    for i in range(start, stop + 1):
        print(f"Number of tries left: {tries}")
        print(f"Guess: {i}")

        if i == random_number:
            print("The program guessed correctly!")
            return

        tries -= 1

        if tries == 0:
            print("The program has failed to guess the correct number.")
            return

if __name__ == "__main__":
    tries = 5
    start = 0
    stop = 10



def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    print(f"Random number to find: {random_number}")
    low = start
    high = stop
    while tries > 0:
        midpoint = (low + high) // 2
        print(f"Guess: {midpoint}")
        tries -= 1
        if midpoint == random_number:
            print("The program guessed correctly!")
            return
        elif midpoint < random_number:
            print("Guessing Higher!")
            low = midpoint + 1
        else:
            print("Guessing Lower!")
            high = midpoint - 1
    if tries == 0:
        print(f"The program has failed to guess the number: {random_number}")
        return

if __name__ == "__main__":
    tries = 5
    start = 0
    stop = 100




"""     # User input.
    guess = guess_random_number(tries, start, stop)
    if guess != -1:
        print("")
    else:
        print(f"You have failed to guess the number: {random_number}") """

# Computer guess Linear.
#guess_random_num_linear(tries, start, stop)


# computer guess binary
guess_random_num_binary(tries, start, stop)

