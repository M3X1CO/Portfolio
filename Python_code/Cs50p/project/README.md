# Hogwarts House and Grade Assignment

#### Video Demo: https://youtu.be/EXY5Hdp3FsU

#### Description:

This Python script reads data from a CSV file containing information about individuals and assigns them to Hogwarts houses based on their characteristics and grades based on their birth year. The script is inspired by the Hogwarts houses from the Harry Potter series.

The script will import the data, assign individuals to Hogwarts houses, and calculate their grades.
CSV Name for import: new_students.csv
The results will be saved in the specified output CSV file.
CSV Name for output: after.csv

The input CSV file should have the following columns: "name," "characteristic," and "birthdate."
The output CSV file will include the columns: "name," "house," and "grade."
Characteristics and Houses:

Individuals are assigned to Hogwarts houses based on their characteristics.
Supported characteristics for each house:
Gryffindor: courage, loyalty, adventure
Hufflepuff: dedication, patience, honesty
Ravenclaw: wisdom, creativity, perfectionism
Slytherin: ambition, competitive, leadership
Grades:

Individuals' grades are determined based on their birth year.
The script calculates the grade as the current year minus the birth year, minus 6, and appends "Grade" to it.
Please ensure that you provide the input and output CSV files as command-line arguments when running the script. Make sure that both files have the ".csv" extension.


This test suite contains a series of pytest test functions for the Python script that assigns individuals to Hogwarts houses based on their characteristics and calculates their grades based on their birth year. The script is inspired by the Hogwarts houses from the Harry Potter series.

**Test_project.py:**

1. `test_check_correct_args()`: Ensures that the `check_correct_args` function raises a `SystemExit` exception when the command-line arguments are incorrect. This is a critical test to validate the command-line argument handling.

2. `test_select_house()`: Checks whether the `select_house` function correctly assigns individuals to Hogwarts houses based on their characteristics.

3. `test_select_grade()`: Verifies that the `select_grade` function accurately calculates the grade of individuals based on their birth year.

These test functions help ensure that the code functions as intended and provide a level of confidence in its correctness. They can be executed using pytest to validate the functionality of the script.

For detailed usage and setup instructions, please refer to the main project README.md file.

For a video demonstration of the project, please refer to the provided URL in the main README.md.


For a video demonstration of the project, please refer to the provided URL.

**Usage:**

- Ensure you have Python installed on your system.
- Provide a CSV file with the data to be processed.
- Run the script with the following command:

```bash
python script.py input.csv output.csv
