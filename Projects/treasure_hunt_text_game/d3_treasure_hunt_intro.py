import time
import os


def space():
    for _ in range(3):
        print()


def processing():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in range(3):
        time.sleep(.5)
        print("                                       ...")
    time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print(r'''
                        ____...------------...____
                   _.-"` /o/__ ____ __ __  __ \o\_`"-._
                 .'     / /                    \ \     '.
                 |=====/o/======================\o\=====|
                 |____/_/________..____..________\_\____|
                 /   _/ \_     <_o#\__/#o_>     _/ \_   \
                 \_________\####/_________/
                  |===\!/========================\!/===|
                  |   |=|          .---.         |=|   |
                  |===|o|=========/     \========|o|===|
                  |   | |         \() ()/        | |   |
                  |===|o|======{'-.) A (.-'}=====|o|===|
                  | __/ \__     '-.\uuu/.-'    __/ \__ |
                  |==== .'.'^'.'.====|
                  |  _\o/   __  {.' __  '.} _   _\o/  _|
                  `""""-""""""""""""""""""""""""""-""""`
    ''')
    print("                        Welcome to Treasure Island")
    print("                   Your mission is to find the treasure")
    print("                   ------------------------------------")

    processing()
    space()

    print("                         The sensation of the coarse sand\n"
          "                          beneath you contrasts sharply\n"
          "                      with the hazy confusion in your mind.\n"
          "                      As you open your eyes to the vastness\n"
          "                      of the horizon, the rhythmic sound of\n"
          "                       the waves crashing against the shore\n"
          "                                  fills the air.")

    processing()
    space()

    print("                           The hunger echoes the confusion\n"
          "                       in your mind, a rhythmic plea matching\n"
          "                      the waves. Vaguely remembering a tattered\n"
          "                            map now clutched in your hand,\n"
          "                     its cryptic markings hint at the beginning\n"
          "                    of a mysterious hunt for the elusive treasure.\n"
          "                                          ___\n"
          "                                          ).x)\n"
          "                                          (:_(\n"
          "\n")


if __name__ == "__main__":
    main()
