'''
Finding the two highest scoresFinding the two highest scores item options
Write a program that prompts the user to enter the number of students, each student's name and score, and finally display the student with the highest score and the student with the second highest score.
Sample Run:
How many students would you like to add? 3
Enter the name for student 1: Jack
Enter the grade for student 1: 89
Enter the name for student 2: Jill
Enter the grade for student 2: 76
Enter the name for student 3: Peter
Enter the grade for student 3: 65
Jack has the highest score and Jill has the second highest score.
Naming Conventon: cst-150-highest-scores.py
You can ONLY use concepts covered in Chapter 3.
'''

highest_score = 0
second_highest_score = 0
highest_name = ""
second_highest_name = ""

students = int(input("How many students would you like to add? "))

for student in range(students):
    name = input('Enter the student name: ')
    grade = float(input('Enter in the grade? '))

    second_highest_score = highest_score
    second_highest_name = name

    if grade > highest_score:
        highest_score = grade
        name = highest_score
    elif grade > second_highest_score:
        second_highest_score = grade


