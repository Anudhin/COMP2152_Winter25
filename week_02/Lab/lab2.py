import random

def get_valid_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Error: Please enter a number between 1 and 6!")
        except ValueError:
            print("Error: Please enter a valid integer!")
            continue

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
print("Weapons: ", weapons)


weaponRoll = get_valid_int_input("Choose a number (1-6) for your weapon roll: ")
print(f"You chose {weaponRoll}")

hero_combat_strength = weaponRoll 

weapon_selected = weapons[weaponRoll - 1]  
print(f"Your weapon is: {weapon_selected}")

if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if weapon_selected != "Fist":
    print("Thank goodness you didn't roll the Fist...")
