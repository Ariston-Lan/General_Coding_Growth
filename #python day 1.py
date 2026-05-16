#python day 19
valid_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
valid_categories = ['school', 'fitness', 'personal']
def validate_date(date):
    if not date in valid_days:
        print(f'{date} is not a day Monday-Sunday')
        return
    else:
        pass
def create_input(integer=False,text=False):
    if integer:
        try:
            user_input = int(input())
        except ValueError:
            print('Input only accepts numbers')
            return
        return user_input
    elif text:
            user_input = input().lower()
            return user_input
def filter_by_date(tasks):
    found = False
    if not tasks:
        print('No tasks avaliable')
        return
    print('Enter due date')
    due_date_filter = create_input(text=True)
    if not due_date_filter in valid_days:
        print('Due date must be day Monday-Sunday')
        return
    print(f'Tasks due {due_date_filter.upper()}:')
    for item in tasks:
        if item['due_date'] == due_date_filter:
            found = True
            print(display_task(item))
    if not found:
        print(f'No tasks due {due_date_filter.upper()}')
def filter_by_category(tasks):
    if not tasks:
        print('No tasks avaliable')
        return
    print('====\nChoose category to filter tasks by')
    for category in valid_categories:
        print(category)
    try:
        category_filter = input().lower()
    except ValueError:
        print('Category must be one of the valid categories')
    if not category_filter in valid_categories:
        print('Category must be one of the valid categories')
    print(f'{category_filter.upper()}:')
    for item in tasks:
        if item['category'] == category_filter:
            print(display_task(item))
def display_task(item, index=False, include_category=False):
    task = item['name']
    difficulty = item['difficulty']
    priority = item['priority']
    category = item['category']
    if include_category:
        if index:
            return (f'{index}. {category.upper()} : [ {task} - {difficulty.upper()} *Priority Level: {priority} ]')
        else:
            return (f'{category.upper()} : [ {task} - {difficulty.upper()} *Priority Level: {priority} ]')
    else:
        if index: 
            return (f'{index}. {task} - {difficulty.upper()} *Priority Level: {priority}')
        else:
            return (f'{task} - {difficulty.upper()} *Priority Level: {priority}')
def task_statistics(tasks, completed_tasks):
    if not tasks and not completed_tasks:
        print('No tasks avaliable')
        return
    print('Enter current day of week')
    current_date = input().lower()
    if not current_date in valid_days:
        print('Current day must be day of week monday-sunday')
        return
    tasks_due_today = 0
    tasks_amount = len(tasks)
    completed_tasks_amount = len(completed_tasks)
    priority_tasks_amount = 0
    total_tasks = tasks_amount + completed_tasks_amount
    completion_rate = round((completed_tasks_amount/total_tasks)*100, 2)
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
          \nTasks due today({current_date}): {tasks_due_today}
          \nTasks completion rate: {(completion_rate)}%
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
            if item['difficulty'] == difficulty_filter and item['priority'] >= priority_filter:
                print(display_task(item))
def show_due_soon(tasks):
    if not tasks:
        print('No tasks currently avaliable')
        return
    print('Choose date')
    try:
        date = input().lower()
    except ValueError:
        print('Date must be a weekday Monday-Sunday')
    if date in valid_days:
        for item in tasks:
            if item['due_date'] == date:
                print(display_task(item))
    else:
        print('Date must be a weekday Monday-Sunday')
def sort_tasks(tasks):
    if not tasks:
        print('No tasks currently avaliable')
        return
    print('EASY:')
    for item in tasks:
        if item['difficulty'] == 'easy':
          print(display_task(item))
    print('\nMEDIUM:')
    for item in tasks:
        if item['difficulty'] == 'medium':
            print(display_task(item))
    print('\nHARD:')
    for item in tasks:
        if item['difficulty'] == 'hard':
            print(display_task(item))
def edit_task(tasks):
    if not tasks:
        print('No task currently avaliable')
        return
    view_tasks(tasks)
    print('What task do you want to edit? (type index NOT task name)')
    task_index = create_input(integer=True)
    if not task_index:
        return
    for index, item in enumerate(tasks):
        if index == task_index-1:
            print(f'{display_task(item, include_category=True)}  - Due {item['due_date']}')
            print('Choose:\nname | difficulty | priority | due date | category')
            choice = input().lower()
            if choice == 'name':
                print('Type new task name')
                try:
                    item['name'] = input().lower()
                except ValueError:
                    print('Invalid input')
                    return
            elif choice == 'difficulty':
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
            elif choice == 'priority':
                print('Choose new priority:\n1\n2\n3\n4\n5')
                try:
                    priority_choice = int(input())
                except ValueError:
                    print('Input must be number 1-5')
                    return
                if priority_choice < 6 and priority_choice > 0:
                    item['priority'] = priority_choice
                else:
                    print('Input must be number 1-5')
                    return
            elif choice == 'due date':
                print('Enter new due date')
                try:
                    new_date = input().lower()
                except ValueError:
                    print('Invalid input')
                    return
                if not new_date in valid_days:
                    print('Invalid date entered, must be day Monday-Sunday')
                    return
                item['due_date'] = new_date
            elif choice == 'category':
                print(f'Assign new category:\n{valid_categories}')
                try:
                    new_category = input().lower()
                except ValueError:
                    print('Invalid input')
                    return
                if not new_category in valid_categories:
                    print(f'New category must be apart of already existing categories\n{valid_categories}')
                    return
                item['category'] = new_category     
            else:
                print(f'{choice} is not an option')
                return  
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
        if item['difficulty'] == difficulty_filter:
            print(display_task(item))
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
        if search_term in task:
            print(display_task(item))
            found = True
    if not found:
        print('No tasks found matching search')
def view_completed_tasks(completed_tasks):
    if not completed_tasks:
        print('No tasks completed')
    for index, item in enumerate(completed_tasks):
        print(display_task(item, index))
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
    print('Enter a category for the task')
    try:
        category = input().lower()
    except ValueError:
        print('Category must be one of the following:')
        for category in valid_categories:
            print(category)
        return
    if not category in valid_categories:
        print('Category must be one of the following:')
        for category in valid_categories:
            print(category)
        return
    tasks.append({
        "name":task,
        "difficulty":difficulty,
        "priority":priority,
        "due_date":date,
        "category":category
                })
    print(f'Task {task} added successfully!')
    return tasks
def remove_task(tasks):
    if not tasks:
        print('No tasks to remove')
        return
    print('What task do you wish to remove?')
    view_tasks(tasks)
    task_index = create_input(integer=True)
    if not task_index:
        return
    task_index = task_index-1
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
        print(display_task(item, index+1))
    return
def sort_important(tasks):
    if not tasks:
        print('No tasks currently avaliable')
        return
    tasks.sort(key = lambda item: item['priority'], reverse=True)
    final = ''
    for item in tasks:
        final += display_task(item) + '\n'
    print(final)
def run():
    should_quit = False
    print('What is your name?')
    name = get_name()
    tasks = []
    completed_tasks = []
    while not should_quit:
        print('=====\nnew name\nadd task\nremove task\nedit task\nmark task\nclear tasks\nview tasks\nsearch\nshow due soon\nfilters\nsort tasks\nstats\nquit')
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
            print('====\nincomplete\ncompleted')
            choice2 = create_input(text=True)
            if choice2 == 'incomplete':
                view_tasks(tasks)
            elif choice2 == 'completed':
                view_completed_tasks(completed_tasks)
            else:
                print(f'{choice2} is not an option')
        elif choice == 'clear tasks':
            clear_tasks(tasks)
        elif choice == 'mark task':
            complete_task(tasks, completed_tasks)
        elif choice == 'search':
            search_task(tasks)
        elif choice == 'filters':
            print('====\ndifficulty\npriority\ndue date\ncategory')
            choice2 = create_input(text=True)
            if choice2 == 'difficulty':
                filter_tasks(tasks)
            elif choice2 == 'priority':
                advanced_filter(tasks)
            elif choice2 == 'category':
                filter_by_category(tasks)
            elif choice2 == 'due date':
                filter_by_date(tasks)
            else:
                print(f'{choice2} is not an option')
        elif choice == 'edit task':
            edit_task(tasks)
        elif choice == 'sort tasks':
            print('====\ndifficulty\npriority\n')
            choice2 = create_input(text=True)
            if choice2 == 'difficulty':
                sort_tasks(tasks)
            elif choice2 == 'priority':
                sort_important(tasks)
            else:
                print(f'{choice2} is not an option')
        elif choice == 'show due soon':
            show_due_soon(tasks)
        elif choice == 'stats':
            task_statistics(tasks, completed_tasks)
        else:
            print(f'\n{choice} is not a valid option\n')
run()