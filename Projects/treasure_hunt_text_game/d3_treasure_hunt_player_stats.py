health = 3
sanity = 3
skill = 2
location = "Beach"


def update_and_save_stats():
    with open("player_stats.txt", "w") as file:
        file.write(f"Health:{health}\n")
        file.write(f"Sanity:{sanity}\n")
        file.write(f"Skill:{skill}\n")
        file.write(f"Location:{location}\n")


def update():
    print(f"\nCurrent Location: {location}")
    print(f"Health: {health:.2f}")
    print(f"Sanity: {sanity:.2f}")
    print(f"Skill: {skill:.2f}")



def action_taken():
    global health, sanity, skill
    health -= .01
    sanity -= .01
    skill += .01
