def nameLess(n1, n2, n3, n4, n5, g1, g2, g3, g4, g5, p1, p2, p3, p4, p5):
    print(f"{n1}, {g1}, {p1}")
    print(f"{n2}, {g2}, {p2}")
    print(f"{n3}, {g3}, {p3}")
    print(f"{n4}, {g4}, {p4}")
    print(f"{n5}, {g5}, {p5}")
    #5 peoples information name email telephone 5 lines
    #use print and println


def drawEgg():
    print("  __________  ")
    print(" /          \ ")
    print("/            \\")
    print("\            /")
    print(" \          / ")
    print("  ----------  ")

def drawTeaCup():
    print(" \            /")
    print("  \          / ")
    print("  +----------+  ")

def drawStopSign():
    print("   __________  ")
    print("  /          \ ")
    print(" /            \\")
    print(" |    STOP    |")
    print(" \            /")
    print("  \          / ")
    print("   ----------  ")

def drawHat():
    print("   __________  ")
    print("  /          \ ")
    print(" /            \\")
    print(" +------------+  ")

def drawBunny():
    print("(\__/)")
    print("(='x'=)")
    print("c(\")_(\")")

def drawCat():
    print(" /\\___/\\")
    print("( =^.^= )")
    print(" (\")_(\")_/")

def drawBird():
    pass

def drawPig():
    pass


def main():
    nameLess("David", "Peter", "Anna", "Charlie", "Joe", "David@gmail.com", "Peter@gmail.com", "Anna@gmail.com", "Charlie@gmail.com", "Joe@gmail.com", "555-555-5123", "555-555-5124", "555-555-5125", "555-555-5126", "555-555-5127", )
    drawEgg()
    drawTeaCup()
    drawStopSign()
    drawHat()
    drawBunny()
    drawCat()
    drawBird()
    drawPig()


main()