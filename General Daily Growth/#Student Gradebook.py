#Student Gradebook
def validate_grade(grade):
    if grade < 0 or grade > 100:
        return
    else:
        return grade
def create_input(name=False,grade=False,prompt=''):
    if name:
        student_name = input(prompt).title()
        return student_name
    if grade:
        try:
            student_grade = int(input(prompt))
        except ValueError:
            return
        student_grade = validate_grade(student_grade)
        return student_grade
def add_student(students):
    student_name = create_input(name=True,prompt="Enter student's name\n")
    student_grade = create_input(grade=True,prompt="Enter student's grade\n")
    if student_grade is None:
        return 'Invalid student grade detected'
    students.append(
    {
        "name":student_name,
        "grade":student_grade
    })
    return 'Student added successfully!'
def view_students(students):
    final = '====\n'
    if not students:
        return 'No students currently'
    for student in students:
        name = student['name']
        grade = student['grade']
        final += (f'{name} - {grade}\n')
    return final
def calculate_average(students):
    if not students:
        return "No students currently"
    total = len(students)
    grade_sum = 0
    for student in students:
        grade = student['grade']
        grade_sum += grade
    avg = grade_sum/total
    return avg
def run():
    students = []
    is_running = True
    while is_running:
        print('=====\nAdd\nView\nAverage\nQuit')
        choice = input().lower()
        if choice == 'add':
            print(add_student(students))
        elif choice == 'view':
            print(view_students(students))
        elif choice == 'average':
            print(calculate_average(students))
        elif choice =='quit':
            is_running = False
            print('Program terminated')
        else:
            print(f'{choice} is not a valid option')
run()