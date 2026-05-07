#python day 12
def show_due_soon(tasks):
    if not tasks:
        print('No tasks currently avaliable')
        return
    print('Choose date')
    try:
        date = input().lower()
    except ValueError:
        print('Date must be a weekday Monday-Friday')
    if date == 'monday' or date == 'tuesday' or date == 'wednesday' or date == 'thursday' or date == 'friday' or date == 'saturday' or date == 'sunday':
        for item in tasks:
            task = item['name']
            difficulty = item['difficulty']
            priority = item['priority']
            if item['due_date'] == date:
                print(f'{task} - {difficulty.upper()} *Priority Level: {priority}')
    else:
        print('Date must be a weekday Monday-Friday')
def sort_tasks(tasks):
    if not tasks:
        print('No tasks currently avaliable')
        return
    print('EASY:')
    for item in tasks:
        task = item['name']
        difficulty = item['difficulty']
        if item['difficulty'] == 'easy':
          print(f'{task} - {difficulty.upper()}')
    print('\nMEDIUM:')
    for item in tasks:
        task = item['name']
        difficulty = item['difficulty']
        if item['difficulty'] == 'medium':
            print(f'{task} - {difficulty.upper()}')
    print('\nHARD:')
    for item in tasks:
        task = item['name']
        difficulty = item['difficulty']
        if item['difficulty'] == 'hard':
            print(f'{task} - {difficulty.upper()}')
def edit_task(tasks):
    if not tasks:
        print('No task currently avaliable')
        return
    view_tasks(tasks)
    print('What task do you want to edit? (type index NOT task name)')
    try:
        task_index = int(input())-1
    except ValueError:
        print('Index must be a number greater than 0')
        return
    for index, item in enumerate(tasks):
        if index == task_index:
            print(item)
            print('Do you wish to edit the task name or difficulty?')
            try:
                choice = input().lower()
            except ValueError:
                print('User must input either "name" or "difficulty".')
                return
            if choice == 'name':
                print('Type new task name')
                item['name'] = input().lower()
            if choice == 'difficulty':
                print('Choose new difficulty:\n1. Easy\n2. Medium\n3. Hard')
                difficulty_choice = input().lower()
                if difficulty_choice == '1' or difficulty_choice == 'easy':
                    item['difficulty'] = 'easy'
                elif difficulty_choice == '2' or difficulty_choice == 'medium':
                    item['difficulty'] = 'medium'
                elif difficulty_choice == '3' or difficulty_choice == 'hard':
                    item['difficulty'] = 'hard'
                else:
                    print('Invalid input, type either index or difficulty')
def filter_tasks(tasks):
    if not tasks:
        print('No task currently avaliable')
        return
    found = False
    print('Choose difficulty to filter\n1. Easy\n2. Medium\n3. Hard')
    difficulty_filter = input().lower()
    if not difficulty_filter:
        print('No input detected')
        return
    for item in tasks:
        task = item["name"]
        difficulty = item["difficulty"]
        if difficulty == difficulty_filter:
            print(f'{task} - {difficulty.upper()}')
            found = True
    if found == False:
        print('No tasks found for selected difficulty')
def search_task(tasks):
    if not tasks:
        print('No tasks currently avaliable')
        return
    print('Search...')
    search_term = input()
    found = False
    for item in tasks:
        task = item['name']
        difficulty = item['difficulty']
        priority = item['priority']
        if search_term in task:
            print(f'{task} - {difficulty.upper()} *Priority Level: {priority}')
            found = True
    if found == False:
        print('No tasks found matching search')
def view_completed_tasks(completed_tasks):
    if not completed_tasks:
        print('No tasks completed')
    for index, item in enumerate(completed_tasks):
        task = item["name"]
        difficulty = item["difficulty"]
        print(f'{index+1}. {task} - {difficulty.upper()}')
def complete_task(tasks, completed_tasks):
    if not tasks:
        print('No task currently avaliable')
        return
    print('What task do you wish to mark complete?')
    view_tasks(tasks)
    try:
        task_index = int(input())-1
    except ValueError:
        print('Please input a valid number')
        return
    if task_index >= len(tasks) or task_index < 0:
        print('Invalid task number')
    else:
        completed_tasks.append(tasks.pop(task_index))
def get_name():
    'What is your name?'
    name = input()
    return name
def clear_tasks(tasks):
    if not tasks:
        print('No tasks to clear')
    else:
        tasks.clear()
        print('All tasks cleared!')
    return tasks
def print_name(name):
    print('How many times do you wish to print your name?')
    amount = int(input())
    return (name + ' ')*amount
def add_task(tasks):
    print('What task do you wish to add?')
    task = input().lower()
    if not task:
        print('Task must have atleast one character')
        return
    print('What is the difficulty of the task?')
    print('\n1. Easy\n2. Medium\n3. Hard')
    choice = input().lower()
    if choice == 'easy':
        difficulty = choice
    elif choice == 'medium':
        difficulty = choice
    elif choice == 'hard':
        difficulty = choice
    else:
        print('Invalid choice')
        return
    print('Assign a prority level to the task from 1-5 (1 being low priority and 5 being high priority)')
    try:
        priority = int(input())
    except ValueError:
        print('User must input a number from 1-5')
        return
    if priority < 1 or priority > 5:
        print('Prority level must be a number from 1-5')
        return
    print('Assign a due date for specified task')
    try:
        date = input().lower()
        print(date)
    except ValueError:
        print('Date must be a weekday Monday-Sunday')
        return
    if date == 'monday' or date == 'tuesday' or date == 'wednesday' or date == 'thursday' or date == 'friday' or date == 'saturday' or date == 'sunday':
        tasks.append({
            "name":task,
            "difficulty":difficulty,
            "priority":priority,
            "due_date":date
                    })
        print(f'Task {task} added successfully!')
    else:
        print('Date must be a weekday Monday-Sunday')
    return tasks
def remove_task(tasks):
    if not tasks:
        print('No tasks to remove')
        return
    print('What task do you wish to remove?')
    view_tasks(tasks)
    try:
        task_index = int(input())-1
    except ValueError:
        print('Please input a valid number')
        return
    if task_index >= len(tasks) or task_index < 0:
        print('Invalid task number')
    else:
        tasks.remove(tasks[task_index])
        print(f'Task removed successfully!')
    return tasks
def view_tasks(tasks):
    if not tasks:
        print('No tasks available')
    for index, item in enumerate(tasks):
        task = item['name']
        difficulty = item['difficulty']
        priority = item['priority']
        print(f'{index+1}. {task} - {difficulty.upper()} *Priority level: {priority}')
    return
def sort_important(tasks):
    if not tasks:
        print('No tasks currently avaliable')
        return
    tasks.sort(key = lambda item: item['priority'], reverse=True)
    final = ''
    for item in tasks:
        task = item['name']
        difficulty = item['difficulty']
        priority = item['priority']
        final += f'{task} - {difficulty.upper()} *Priority Level: {priority}\n'
    print(final)
def run():
    should_quit = False
    print('What is your name?')
    name = get_name()
    tasks = []
    completed_tasks = []
    while not should_quit:
        print('=====\nprint name\nnew name\nadd task\nremove task\nview tasks\nclear tasks\nmark task\nview completed tasks\nsearch\nfilter\nedit task\nsort tasks\nsort improtant\nshow due soon\nquit\n')
        choice = input().lower()
        if choice == 'print name':
            print(print_name(name))
        elif choice == 'quit':
            should_quit = True
            print ('Session Terminated')
        elif choice == 'new name':
            print('What is your new name?')
            name = get_name()
        elif choice == 'add task':
            add_task(tasks)
        elif choice =='remove task':
            remove_task(tasks)
        elif choice == 'view tasks':
            view_tasks(tasks)
        elif choice == 'clear tasks':
            clear_tasks(tasks)
        elif choice == 'mark task':
            complete_task(tasks, completed_tasks)
        elif choice == 'view completed tasks':
            view_completed_tasks(completed_tasks)
        elif choice == 'search':
            search_task(tasks)
        elif choice == 'filter':
            filter_tasks(tasks)
        elif choice == 'edit task':
            edit_task(tasks)
        elif choice == 'sort tasks':
            sort_tasks(tasks)
        elif choice == 'sort important':
            sort_important(tasks)
        elif choice == 'show due soon':
            show_due_soon(tasks)
        else:
            print(f'\n{choice} is not a valid option\n')
run()