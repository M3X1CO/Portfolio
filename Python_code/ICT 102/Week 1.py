def welcome():
    print("Hello RSU")

def greeting(n1, n2, n3, age, weight):
    print("Hey!!!.....", n1)
    print("Hey!!!.....", n2)
    print("Hey!!!.....", n3)
    print(age*weight*100/5)
    print("person name")

def main():
    print("Welcome to ICT")
    print("-------------")
    for i in range(20):
        welcome()
        greeting("David", "Peter", "Anna", 34, 45.6)

main()
