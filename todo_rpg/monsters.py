"""
how many days do you need to do things every day to form a habit?

a habit, but this can range from 18 to 254 days. Some research has even suggested that it can take up to 8 months to form a habit.
"""

import random


# Set up player stats
player_name = input("Enter your player name: ")
todo_items = []  # list to store to-do list items
health = 100
points = 0
location = 0  # start at the beginning of the map

# Set up store items and prices
store_items = {
    "health potion": 50,
    "energy drink": 75,
    "stealth gear": 100,
    "battle armor": 150,
}

# Set up enemies
enemies = [
    {
        "name": "Goblin",
        "health": 50,
        "attack": 10,
        "defense": 5,
        "reward": 25,
    },
    {
        "name": "Orc",
        "health": 75,
        "attack": 15,
        "defense": 10,
        "reward": 50,
    },
    {
        "name": "Dragon",
        "health": 100,
        "attack": 20,
        "defense": 15,
        "reward": 100,
    },
]

def add_todo_item():
    """Prompts the player to add a to-do list item"""
    item = input("Enter a to-do list item: ")
    todo_items.append(item)
    print(f"{item} has been added to your to-do list")

def check_todo_items():
    """Checks if all to-do list items have been completed and removes them if they have"""
    for item in todo_items:
        completed = input(f"Have you completed {item} (y/n)? ").lower()
        if completed == "y":
            todo_items.remove(item)
            print(f"{item} has been removed from your to-do list")

def advance():
    """Advances the player's location on the map and earns points and health"""
    global location, health, points
    location += 1
    health += 10
    points += 50
    print("You have advanced to the next location on the map!")
    print(f"Your health is now {health} and you have {points} points")

def visit_store():
    """Lets the player buy items from the store using their points"""
    global points
    print("Welcome to the store! Here are the items for sale:")
    for item, price in store_items.items():
        print(f"{item}: {price} points")
    purchase = input("What would you like to buy? ").lower()
    if purchase in store_items:
        cost = store_items[purchase]
        if points >= cost:
            points -= cost
            print(f"You have purchased {purchase} for {cost} points")
            print(f"You have {points} points remaining")
        else:
            print("You do not have enough points to make this purchase")
    else:
        print("That item is not available for purchase")

        
def fast_talk(enemy):
    """Attempts to defeat an enemy through fast talking, earning points if successful"""
    global points
    success = random.randint(0, 1)  # 50% chance of success
    if success:
        points += enemy["reward"]
        print(f"You have successfully fast talked the {enemy['name']} and earned {enemy['reward']} points")
    else:
        print(f"Your fast talking was unsuccessful and the {enemy['name']} attacked you")
        attack(enemy)

def stealth(enemy):
    """Attempts to defeat an enemy through stealth, earning points if successful"""
    global points
    success = random.randint(0, 1)  # 50% chance of success
    if success:
        points += enemy["reward"]
        print(f"You have successfully stealthily defeated the {enemy['name']} and earned {enemy['reward']} points")
    else:
        print(f"Your stealth attempt was unsuccessful and the {enemy['name']} attack you")
        attack(enemy)

def attack(enemy):
    """Calculates the player's attack and the enemy's defense to determine damage dealt"""
    global health
    enemy_health = enemy["health"]
    enemy_defense = enemy["defense"]
    player_attack = random.randint(10, 20)  # player's attack strength is between 10 and 20
    enemy_damage = player_attack - enemy_defense
    enemy_health -= enemy_damage
    if enemy_health <= 0:
        print(f"You have defeated the {enemy['name']} and earned {enemy['reward']} points")
        points += enemy["reward"]
    else:
        print(f"You have dealt {enemy_damage} damage to the {enemy['name']}")
        enemy_attack = enemy["attack"]
        player_defense = random.randint(5, 15)  # player's defense strength is between 5 and 15
        player_damage = enemy_attack - player_defense
        health -= player_damage
        if health <= 0:
            print("You have been defeated by the enemy")
            exit()
        else:
            print(f"The {enemy['name']} has dealt {player_damage} damage to you")

# Main game loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add to-do list item")
    print("2. Check to-do list items")
    print("3. Advance on the map")
    print("4. Visit the store")
    print("5. Fight an enemy")
    action = input("Enter the number of your choice: ")
    if action == "1":
        add_todo_item()
    elif action == "2":
        check_todo_items()
    elif action == "3":
        if not todo_items:  # only advance if all to-do list items are completed
            advance()
        else:
            print("You must complete all of your to-do list items before advancing on the map")
    elif action == "4":
        visit_store()
    elif action == "5":
        if not enemies:  # no enemies remaining
            print("You have defeated all of the enemies!")
        else:
            print("Which enemy would you like to fight?")
            for i, enemy in enumerate(enemies):
                print(f"{i+1}. {enemy['name']}")
            choice = int(input("Enter the number of your choice: "))
            if choice > 0 and choice <= len(enemies):
                selected_enemy = enemies[choice - 1]
                print(f"You have selected to fight the {selected_enemy['name']}")
                print("How would you like to defeat the enemy?")
                print("1. Fast talk")
                print("2. Stealth")
                print("3. Attack")
                defeat_method = input("Enter the number of your choice: ")
                if defeat_method == "1":
                    fast_talk(selected_enemy)
                elif defeat_method == "2":
                    stealth(selected_enemy)
                elif defeat_method == "3":
                    attack(selected_enemy)
                if selected_enemy["health"] <= 0:
                    enemies.remove(selected_enemy)  # enemy is defeated and removed from the list
            else:
                print("Invalid choice")
    else:
        print("Invalid choice")
