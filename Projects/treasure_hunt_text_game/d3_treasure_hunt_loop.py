import d3_treasure_hunt_player_stats as stats
import d3_treasure_hunt_choices as choices
import d3_treasure_hunt_building as bldg
import os
import time


def call_q():
    choices.main()
    return input("Enter the number of your choice: ")  # Return the user input


def main():
    stats.update()
    print("\nNight is approaching...")

    while stats.health > 0 and stats.sanity > 0:
        choice = call_q()

        if choice == "1":
            while bldg.bed < 100 or bldg.shelter < 100:
                os.system('cls' if os.name == 'nt' else 'clear')
                bldg.main()
                call_q()
                '''
                stats.update()
                stats.update_and_save_stats()
                print("Bed is made, get some rest?")
        elif choice == "2":
            # Implement logic for moving into the jungle
            pass
        elif choice == "3":
            # Implement logic for looking for food
            pass
        elif choice == "4":
            print("Thanks for playing! Goodbye.")
            break  # Exit the loop when the user chooses to quit
            '''
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
