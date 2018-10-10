
# functions by Python
import random

def scholarship(student_name, student_age, student_grade):
    if student_grade >= 90:
        if student_age >= 18:
            print("Congratulations", student_name, "your scholarship is of 4000 eurodollars")
        elif student_age <= 17:
            print("Congratulations", student_name, "your scholarship is of 3000 eurodollars")
    elif student_grade >= 85:
        if student_age >= 18:
            print("Congratulations", student_name, "your scholarship is of 3000 eurodollars")
        elif student_age <= 17:
            print("Congratulations", student_name, "your scholarship is of 2000 eurodollars")
    elif student_grade >= 70:
        if student_age >= 18:
            print("Congratulations", student_name, "your scholarship is of 2000 eurodollars")
        elif student_age <= 17:
            print("Congratulations", student_name, "your scholarship is of 1000 eurodollars")
    elif student_grade <= 70:
        print("Congratulations", student_name, "you get absolutely nothing at all")

student = {
    'name': 'Alex',
    'age': random.randint(15, 35),
    'grade': random.randint(60, 100)
}
scholarship(student['name'], student['age'], student['grade'])
