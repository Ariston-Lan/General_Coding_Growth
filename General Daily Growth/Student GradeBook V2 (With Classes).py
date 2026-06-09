class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f'{self.name} - {self.grade}\n'
    def has_passed(self):
        if self.grade < 70:
            return False
        else:
            return True
def validate_grade(grade):
    if grade < 0 or grade > 100:
        return
    else:
        return grade
def get_name(prompt=''):
    name = input(prompt).title()
    return name
def get_grade(prompt=''):
    try:
        grade = int(input(prompt))
    except ValueError:
        return
    grade = validate_grade(grade)
    return grade
def add_student(students):
    student = Student(get_name("Enter Student's name\n"), get_grade("Enter Student's grade\n"))
    if student.grade is None:
        return 'Invalid grade detected'
    students.append(student)
    return f'\n{student.name} added successfully!'
def view_students(students):
    if not students:
        return "No students currently"
    final = '=====\n'
    for student in students:
        final += student.__str__()
    return final
def calcualte_average(students):
    if not students:
        return "No students currently"
    total = len(students)
    grade_sum = 0
    for student in students:
        grade = student.grade
        grade_sum += grade
    avg = grade_sum/total
    return f'=====\n{avg}'
def check_student(students):
    if not students:
        return "No students currently"
    search_name = get_name("Enter student you are looking for\n")
    for student in students:
        if search_name == student.name:
            if student.has_passed():
                return f"=====\n{student.name} is passing!"
            else:
                return f'=====\n{student.name} is not passing.'
    return f'{search_name} not found'
def run():
    students = []
    is_running = True
    while is_running:
        print('Add\nView\nAverage\nCheck\nQuit')
        choice = input().lower()
        if choice == 'add':
            print(add_student(students))
        elif choice == 'view':
            print(view_students(students))
        elif choice == 'average':
            print(calcualte_average(students))
        elif choice =='check':
            print(check_student(students))
        elif choice == 'quit':
            is_running = False
            print('=====\nProgram Terminated')
        else:
            print('=====\nInvalid choice')
run()