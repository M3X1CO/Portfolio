def grading_system():
    score = eval(input("Guess your grade fool: "))
    if score >= 80:
        print("study harder or lose")
    elif score >= 70:
        print("maybe you should hual trash")
    elif score >= 60:
        print("you definitely partied tooo hard")
    elif score >= 50:
        print("you are probably addicted to sumthing")
    else:
        print("your the next bill gates or elon musk... coming soon")

def heat_warning(degree):
    if degree > 40:
        print("stay inside your gonna die")
    elif degree > 15:
        print("still sus will probably get too hot soon make emergency supply run now")
    elif degree >= 0:
        print("Optimal operating temperature for Hoomans")
    else:
        print("Blood thickening activated...")


def main():
    print("   ")
    celsius = eval(input("Input temperature in Celsius: "))
    heat_warning(celsius)


main()
