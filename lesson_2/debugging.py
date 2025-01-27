# Steps for debugging
# 1. Reproduce the Error
# 2. Determine the boundaries of the Error
def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    print(grades)
    total = sum(grades)
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'},
    {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75}
]

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        if grade:
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))


def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
            new_words.append(word)
        else:
            new_words.append(word)
    
    return ' '.join(new_words)

title = 'hello world of programming'
titlize(title)

import pdb

counter = 1

while counter <= 5:
    print(counter)
    pdb.set_trace()
    counter += 1