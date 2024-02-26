'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindors"})

print(gryffindors)
'''


'''
# list comprehension list of dicts
students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)
'''


'''
# dictionary comprehension
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)
'''


'''
# prints the index of names
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i, students[i]) # or i + 1 to give ranking instead or index value
'''

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)



