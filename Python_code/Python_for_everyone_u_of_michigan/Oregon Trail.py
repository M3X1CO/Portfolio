import random

# Define the initial game state
player_name = input("What's your name? ")
party_members = [player_name, "Jane", "John"]
miles_traveled = 0
food_remaining = 500
health = 100
weather_conditions = ["sunny", "rainy", "snowy"]
current_weather = random.choice(weather_conditions)

# Define the game loop
while True:
    print(f"\nYou have traveled {miles_traveled} miles.")
    print(f"You have {food_remaining} pounds of food left.")
    print(f"Your health is {health}.")
    print(f"The weather is {current_weather}.\n")

    # Determine how far the player can travel based on the weather conditions
    max_distance = random.randint(50, 100)
    if current_weather == "rainy":
        max_distance = max_distance // 2
    elif current_weather == "snowy":
        max_distance = max_distance // 10

    # Determine if the player gets sick
    if random.random() < 0.1:
        print("Oh no, you got sick!")
        health -= random.randint(10, 20)

    # Ask the player what they want to do
    action = input("What do you want to do? Type 'travel' to keep moving, 'hunt' to search for food, 'rest' to recover your health, or 'quit' to exit the game. ")

    # Handle the player's choice
    if action == "travel":
        # Update the game state
        distance_traveled = random.randint(1, max_distance)
        miles_traveled += distance_traveled
        food_remaining -= random.randint(5, 25)
        health -= random.randint(5, 15)

        # Check if the player is sick
        if random.random() < 0.1:
            print("Oh no, you're still sick!")
            health -= random.randint(10, 20)

        # Check if the game is over
        if food_remaining <= 0 or health <= 0:
            print("Game over! You ran out of food or your health dropped to 0.")
            break

        # Update the weather
        current_weather = random.choice(weather_conditions)

    elif action == "hunt":
        # Update the game state
        food_found = random.randint(50, 100)
        food_remaining += food_found
        health -= random.randint(5, 15)

        # Check if the player is sick
        if random.random() < 0.1:
            print("Oh no, you're still sick!")
            health -= random.randint(10, 20)

        # Check if the game is over
        if health <= 0:
            print("Game over! Your health dropped to 0.")
            break

        # Update the weather
        current_weather = random.choice(weather_conditions)

    elif action == "rest":
        # Update the game state
        health += random.randint(10, 20)
        food_remaining -= random.randint(5, 10)

        # Check if the player is sick
        if random.random() < 0.1:
            print("Oh no, you're still sick!")
            health -= random.randint(10, 20)

        # Check if the game is over
        if food_remaining <= 0 or health <= 0:
            print("Game over! You ran out of food or your health dropped to 0.")
            break

        # Update the weather
        current_weather = random.choice(weather_conditions)

    else:
        print("Invalid input. Please try again.")

    # Check if the player has reached the end of the game
    if miles_traveled >= 1000:
        print("Congratulations! You made it to Oregon.")
        break
