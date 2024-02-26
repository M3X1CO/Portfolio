import random
import d3_treasure_hunt_player_stats as stats
bed = 0
shelter = 0


def bed_completion(global_bed):
    return "100%" if global_bed > 100 else "75%" if global_bed == 75 else "50%" if global_bed == 50 else "25%" if global_bed == 25 else "0%"


def shelter_completion(global_shelter):
    return "100%" if global_shelter > 100 else "75%" if global_shelter == 75 else "50%" if global_shelter == 50 else "25%" if global_shelter == 25 else "0%"


def eighty_twenty_odds():
    random_number = random.randint(0, 99)
    return random_number < 95


def main():
    global bed, shelter
    print("Exploring...")

    if eighty_twenty_odds():
        event = random.choice(["Sticks", "Grass", "Moss", "Rock"])
        if event == "Sticks" or event == "Rock":
            print(f"You discovered: {event}")
            bed += 25
            print(f"Bed completed: {bed_completion(bed)}")
            stats.action_taken()
        else:
            print(f"You discovered: {event}")
            shelter += 25
            print(f"Shelter completed: {shelter_completion(shelter)}")
            stats.action_taken()
    else:
        print("You didn't find anything!")


if __name__ == "__main__":
    main()
