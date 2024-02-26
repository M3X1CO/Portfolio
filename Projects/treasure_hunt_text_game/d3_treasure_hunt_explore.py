def explore():
    print("Exploring...")

    event = random.choice(["Forest", "Cave", "Town Square"])
    print("You discovered: {}".format(event))

    # Simulate events and consequences
    if event == "Forest":
        print("You encounter a wild animal!")
        damage = random.randint(10, 20)
        print("The animal dealt {} damage to you.".format(damage))
        return player_stats.player_health - damage, player_stats.player_inventory
    elif event == "Cave":
        print("You found a hidden passage!")
        player_stats.player_inventory.append("Magic Crystal")
        print("You obtained a Magic Crystal!")
        return player_stats.player_health, player_stats.player_inventory
    # ... (other events)
    else:
        print("You continue your journey.")
        return player_stats.player_health, player_stats.player_inventory


if __name__ == "__explore__":
    explore()