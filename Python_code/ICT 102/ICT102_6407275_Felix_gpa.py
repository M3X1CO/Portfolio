def gpa(grades):
    total_credits = 0
    total_grade_points = 0

    for credit, grade in grades:
        total_credits += credit
        total_grade_points += credit * grade

    if total_credits > 0:
        gpa = total_grade_points / total_credits
        return gpa

def main():
    classes = {"ICT 102": 3, "ICT 103": 3, "ICT 112": 3, "ICT 209": 3, "ITE 201": 3}
    grades = []

    for subject, credits in classes.items():
        grade = float(input(f"Enter a grade for {subject} (Credits: {credits}): "))
        grades.append((credits, grade))
        # print(subject, credits, grade)

    print("Subject     Credit/s   Grade")
    # print(grades) #list of tuples

    for subject, (credits, grade) in zip(classes.keys(), grades):
        print(f"{subject}:    {credits}          {grade}")

    zipped_result = list(zip(classes.keys(), grades))
    # print(zipped_result)

    calculated_gpa = gpa(grades)
    print(f"Calculated GPA: {calculated_gpa:.2f}")

    #print(grades)

if __name__ == "__main__":
    main()
