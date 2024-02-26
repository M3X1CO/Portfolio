meaning = input("What is the answer to the great question of life, the universe, and everything? ")
meaning = meaning.lower().strip()
if meaning == "42" or meaning == "forty-two" or meaning == "forty two":
    print("Yes")
else:
    print("No")