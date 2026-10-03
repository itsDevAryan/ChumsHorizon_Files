from chums import starter_chums, inventory, numbers, encounter, legendary_encounter, boulderpug, blazepaw, mistfrog, Legendary_chums
import random

#Introduction to the game
print("=========CHUMS HORIZON========= Version 1.0")
print("Created by: Aryan, @2026 an indie python programmer. All copyrights reserved")
print("Welcome to Chums Horizon! In this game, you will be able to catch and battle with various creatures called Chums. Each Chum has its own unique abilities and stats. Choose your starter Chum wisely and embark on an adventure to become the ultimate Chum Master!")
print("Please select your starter Chum from the following options:")
print(f"1. 🌿 Mosshare (Grass Type) - Base HP: 100, Attack: 60")
print(f"2. 🔥 Blazepaw (Fire Type) - Base HP: 90, Attack: 70")
print(f"3. 🦆 Puddleduck (Water Type) - Base HP: 100, Attack: 55")
print()

choose = input("Enter the number of your choice (1, 2, or 3): ")
    
#choice validation
while choose not in ["1", "2", "3"]:
    print("Invalid choice. Please select a valid option.")
    choose = input("Enter the number of your choice (1, 2, or 3): ")
    print()
if choose == "1":
    selected_chum = starter_chums[0]
    print(f"You have selected {selected_chum.emoji} {selected_chum.name} as your starter Chum!")
    print()
elif choose == "2":
    selected_chum = starter_chums[1]
    print(f"You have selected {selected_chum.emoji} {selected_chum.name} as your starter Chum!")
    print()
elif choose == "3":
    selected_chum = starter_chums[2]
    print(f"You have selected {selected_chum.emoji} {selected_chum.name} as your starter Chum!")
    print()
else:
    print("Invalid choice. Please select a valid option.")
    print()
    exit()

print("Name the legend name history will record as:")

#player name input
name = input("Enter your name: ")
print()
print(f"Welcome, {name}! Your journey as a Chum Master begins now!")

print("Ready to embark on your adventure? Let's go! to hunt for some chums and battle other trainers! in the ShadowLeaf forest")
print()
print("Professor: Oh hello there! I am Professor Leaf, the leading expert on Chums. I have been studying these creatures for many years and have discovered their unique abilities and characteristics. I will be your guide on this journey to become a Chum Master. Good luck!")
print("Professor: Before you go, I have a special gift for you. Here is a Chum Ball, which will allow you to catch and store your Chums. Use it wisely and remember to take care of your Chums!")
print("Professor: Now, go forth and explore the world of Chums! There are many adventures waiting for you, and I am sure you will become a great Chum Master!")
print()

inventory = inventory()
inventory.items["Chum Ball"] += 10
inventory.add_chum(selected_chum)

#player choice
def menu():
    print("=========CHUMS HORIZON=========")
    print("1.Hunt for Chums")
    print("2. View Inventory")
    print("3. View Chums")
    print("4.Search for Gyms to battle...")
    print("5.ChumVision")
    print("6. Exit")
    print("7.About me!")
    print("8. Shop")
    choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7 or 8): ")    
    return choice

#GYM battle logics
def gym_battle():
    player_chum = inventory.chums[0]
    gym_chum = random.choice([boulderpug, blazepaw, mistfrog])
    player_hp = player_chum.basehp
    gym_hp = gym_chum.basehp

    print(f"You entered the gym! {gym_chum.emoji} {gym_chum.name} is ready to battle!")
    while player_hp > 0 and gym_hp > 0:
        print(f"{player_chum.emoji} {player_chum.name}: {player_hp} HP")
        print(f"{gym_chum.emoji} {gym_chum.name}: {gym_hp} HP")
        action = input("Press Enter to attack or type q to leave: ").lower()

        if action == "q":
            print("You left the gym.")
            return

        gym_hp -= player_chum.attk
        print(f"{player_chum.emoji} {player_chum.name} dealt {player_chum.attk} damage!")
        if gym_hp <= 0:
            break

        player_hp -= gym_chum.attk
        print(f"{gym_chum.emoji} {gym_chum.name} dealt {gym_chum.attk} damage!")

    if player_hp > 0:
        inventory.badges += 1
        inventory.money += 50
        print("You won the gym battle and earned a badge! 🏅")
        print("You received ₹50!")
    else:
        print("You lost the gym battle. Train more and try again!")

#Shop logics
def shop():
    potion_price = 20
    print(f"You have {inventory.money} coins.")
    print(f"Potion - {potion_price} coins")
    buy = input("Buy a Potion? (y/n): ").lower()

    if buy == "y":
        if inventory.money >= potion_price:
            inventory.money -= potion_price
            inventory.items["Potion"] += 1
            print("You bought a Potion!")
            print(f"Money left: {inventory.money} coins")
        else:
            print("You do not have enough money.")
    else:
        print("You left the shop.")

playing = True
while playing:
    choice = menu()

    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid choice. Please select a valid option.")
        choice = menu()

    if choice == "1":
        print("Walking through the forest")
        encounter_chum = random.choice(numbers)

        if encounter_chum >= 95:
            a = random.choice(legendary_encounter)
            print(f"A legendary Chum appeared! {a.emoji} {a.name} base hp {a.basehp}!")
            if inventory.items["Chum Ball"] <= 0:
                print("You have no Chum Balls left!")
            else:
                catch = input("Press Enter to catch continue...")
                if catch == "":
                    print(f"You have caught {a.emoji} {a.name}!")
                    inventory.add_chum(a)
                    inventory.items["Chum Ball"] -= 1
        elif encounter_chum > 31:
            a = random.choice(encounter)
            print(f"You have encountered {a.emoji} {a.name} base hp {a.basehp}!")
            if inventory.items["Chum Ball"] <= 0:
                print("You have no Chum Balls left!")
            else:
                catch = input("Press Enter to catch continue...")
                if catch == "":
                    print(f"You have caught {a.emoji} {a.name}!")
                    inventory.add_chum(a)
                    inventory.items["Chum Ball"] -= 1
                     
        else:
            print("You have not encounter any chums!")
        print()

    elif choice == "2":
        print("Your Inventory: ")
        for item, quantity in inventory.items.items():
            print(f"{item}: {quantity}")
        print()
        
    elif choice == "3":
            print("Your Chums:")
            for chum in inventory.chums:
                print(f"{chum.emoji} {chum.name} - Base HP: {chum.basehp}, Attack: {chum.attk}")
            print()

    elif choice == "4":
        gym_battle()
        print()

    elif choice == "5":
        print("ChumVision - Legendary Chums:")
        for chum in legendary_encounter:
            print(f"{chum.emoji} {chum.name} - Rarity: Legendary")
        print()

    elif choice == "6":
        print("Thank you for playing Chums Horizon! Goodbye!")
        playing = False

    elif choice == "7":
        print("About Me!")
        print()
        print("I am an indie python programmer, and I created this game as a fun project to showcase my programming skills. I hope you enjoy playing Chums Horizon and have a great time exploring the world of Chums!")

    elif choice == "8":
        shop()
        print()
        
       