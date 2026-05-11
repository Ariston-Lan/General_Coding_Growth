#python day 14
valid_days = ['monday','tuesday','wednesday','thursay','friday','saturday','sunday']
def task_statistics(tasks, completed_tasks):
    print('Enter current day of week')
    try:
        current_date = input().lower()
    except ValueError:
        print('Current date must be day of week monday-sunday')
        return
    if not current_date in valid_days:
        print('Current day must be day of week monday-sunday')
        return
    tasks_due_today = 0
    tasks_amount = len(tasks)
    completed_tasks_amount = len(completed_tasks)
    priority_tasks_amount = 0
    total_tasks = tasks_amount + completed_tasks_amount
    completion_rate = (completed_tasks_amount/total_tasks)*100
    for item in tasks:
        priority = item['priority']
        due_date = item['due_date']
        if priority >= 4:
            priority_tasks_amount += 1
        if current_date == due_date:
            tasks_due_today +=1
    print(f'''\nTotal tasks: {total_tasks}
          \nCompleted tasks: {completed_tasks_amount}
          \nHigh priority tasks: {priority_tasks_amount}
          \nTasks due {current_date}: {tasks_due_today}
          \nTasks completion rate: {completion_rate}%
        ''')
def auto_assign_priority(difficulty):
    if difficulty == 'easy':
        priority = 1
    elif difficulty == 'medium':
        priority = 3
    elif difficulty == 'hard':
        priority = 5
    else:
        print('Unable to assign priority: Difficulty must be easy, medium, or hard.')
        return
    return priority
def advanced_filter(tasks):
    if not tasks:
        print('No tasks avaliable')
        return
    print('Choose difficulty:\nEasy\nMedium\nHard')
    difficulty_filter = input().lower()
    if difficulty_filter == 'easy' or difficulty_filter == 'medium' or difficulty_filter == 'hard':
        print('Choose minimum priority (1-5)')
        try:
            priority_filter = int(input())
        except ValueError:
            print('minimum priority must be a number 1-5')
            return
        if priority_filter < 1 or priority_filter > 5:
            print('minimum priority must be a number 1-5')
            return
        for item in tasks:
            difficulty = item['difficulty']
            task = item['name']
            priority = item['priority']
            if item['difficulty'] == difficulty_filter and item['priority'] >= priority_filter:
                print(f'{task} - {difficulty.upper()} *Priority Level: {priority}')
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
    print('Assign a prority level to the task from 1-5 (Optional)')
    priority = input()
    if not priority:
        priority = auto_assign_priority(difficulty)
    elif priority:
        try:
            priority = int(priority)
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
    if not date in valid_days:
        print('Date must be weekday Monday-Sunday')
        return
    tasks.append({
        "name":task,
        "difficulty":difficulty,
        "priority":priority,
        "due_date":date
                })
    print(f'Task {task} added successfully!')
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
        print('''=====\nprint name\nnew name\nadd task\nremove task\nview tasksnclear tasks\nmark task\nview completed tasks\nsearch\nfilter\nedit task\nsort tasks\nsort improtant\nshow due soon\nadvanced filter\nstats\nquit
              \n''')
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
        elif choice == 'advanced filter':
            advanced_filter(tasks)
        elif choice == 'stats':
            task_statistics(tasks, completed_tasks)
        else:
            print(f'\n{choice} is not a valid option\n')
run()