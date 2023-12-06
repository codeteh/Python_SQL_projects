wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

# Create a list of options
print("1) Wizard")
print("2) Elf")
print("3) Human")

""" 
Set up for infinite while loop to handle player choice.
And a prompt for user to choose their character
"""
while True:
    character = input("Choose your own character: ")
    if character == "1":
        character = "Wizard"
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2":
        character = "Elf"
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3":
        character = "Human"
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown Character")
        continue

print("You have chosen the character:", character)
print("Health:", my_hp)
print("Damage:", my_damage)

# second infinite while loop for character battle with dragon
while True:
    dragon_hp = dragon_hp - my_damage
    my_hp = my_hp - dragon_damage
    if dragon_hp <= dragon_hp:
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon_hp)
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
    if my_hp <= my_hp:
        print("The Dragon strikes back!")
        print("The", character, "'s hitpoints are now:", my_hp)
        if my_hp <= 0:
            print("The", character, "has lost the battle!")
            break
