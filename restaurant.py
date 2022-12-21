class Player:
    def __init__(self, name, energy, money):
        self.name = name
        self.energy = energy
        self.money = money

class Restaurant:
    def __init__(self, menu, staff, seating, kitchen):
        self.menu = menu
        self.staff = staff
        self.seating = seating
        self.kitchen = kitchen

class FoodTruck:
    def __init__(self, menu, staff, location):
        self.menu = menu
        self.staff = staff
        self.location = location

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class Customer:
    def __init__(self, name, order):
        self.name = name
        self.order = order# Initialize player character
player = Player("Alice", 100, 1000)

# Initialize vegan restaurant
menu = ["Veggie Burger", "Falafel Wrap", "Tofu Stir Fry"]
staff = ["Bob", "Charlie", "Diane"]
restaurant = Restaurant(menu, staff, 20, "Basic")

# Initialize food truck (not yet owned by the player)
food_truck = FoodTruck(menu, staff, "Downtown")

# Initialize some vegan recipes
recipe1 = Recipe("Veggie Burger", ["Lettuce", "Tomato", "Veggie Patty"], "1. Preheat grill to medium heat. 2. Grill veggie patty for 5-7 minutes on each side. 3. Assemble burger with lettuce, tomato, and veggie patty on a bun.")
recipe2 = Recipe("Falafel Wrap", ["Falafel Balls", "Pita Bread", "Tahini Sauce"], "1. Warm pita bread in the oven or on a stovetop griddle. 2. Assemble wrap with falafel balls, tahini sauce, and desired vegetables.")
recipe3 = Recipe("Tofu Stir Fry", ["Tofu", "Vegetables", "Soy Sauce"], "1. Press tofu to remove excess moisture. 2. Cut tofu and vegetables into bite-sized pieces. 3. Heat oil in a pan over medium heat. 4. Add tofu and vegetables to the pan and stir fry until cooked through. 5. Add soy sauce and desired seasonings to taste.")

# Initialize some customers
customer1 = Customer("Eve", "Veggie Burger")
customer2 = Customer("Frank", "Falafel Wrap")
customer3 = Customer("Greta", "Tofu Stir Fry")

while True:
    # Ask player if they have completed their daily habit
    daily_habit_completed = input("Have you completed your daily habit? (y/n) ")
    if daily_habit_completed == "y":
        player.energy += 10
    
    # Ask player if they have completed any one-off tasks
    one_off_tasks_completed = input("Have you completed any one-off tasks? (y/n) ")
    if one_off_tasks_completed == "y":
        one_off_task_reward = int(input("How much money did you earn from one-off tasks? "))
        player.money += one_off_task_reward
    
    # Display game actions
    print("Game actions:")
    print("1. Hire staff")
    print("2. Cook recipe")
    print("3. Buy ingredients")
    print("4. Exit game")
    
    # Ask player to choose a game action
    action = int(input("Choose a game action: "))
    
    if action == 1:
        # Hire staff
        name = input("Enter the name of the staff member you want to hire: ")
        restaurant.staff.append(name)
    elif action == 2:
        # Cook recipe
        if player.energy < 10:
            print("You do not have enough energy to cook a recipe.")
        else:
            # Display available recipes
            print("Available recipes:")
            for i, recipe in enumerate(menu):
                print(f"{i+1}. {recipe}")
            # Ask player to choose a recipe
            recipe_choice = int(input("Choose a recipe: ")) - 1
            recipe = menu[recipe_choice]
            # Cook recipe and serve to a customer
            player.energy -= 10
            customer = customers.pop(0)
            print(f"You cooked a {recipe} and served it to {customer.name}.")
    elif action == 3:
        # Buy ingredients
        ingredient = input("Enter the name of the ingredient you want to buy: ")
        cost = int(input("Enter the cost of the ingredient: "))
        if player.money < cost:
            print("You do not have enough money to buy this ingredient.")
        else:
            # Add ingredient to menu and subtract cost from player's money
            menu.append(ingredient)
            player.money -= cost
    elif action == 4:
        # Exit game
        break
    
    # Summarize state of restaurant
    num_customers_served = len(menu) - len(customers)
    num_customers_left_hungry = len(customers)
    print(f"Customers served: {num_customers_served}")
    print(f"Customers left hungry: {num_customers_left_hungry}")

        
