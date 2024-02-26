animals = {1: "Python"}
loops = 1

# Create a copy of the keys before iterating
keys = list(animals.keys())

for key in keys:
    del animals[key]
    animals[key + 1] = None
    print(f"{loops = }")
    loops += 1
