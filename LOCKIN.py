#Daily Python day 28, this represents the last time I have touched this project
import json
import os
import time
def display_time(final_duration):
    visual_time = {
        'seconds':final_duration%60,
        'minutes':int(final_duration/60)%60,
    }
    if visual_time['seconds'] and visual_time['minutes']:
        return f'{visual_time['minutes']} mins and {visual_time['seconds']} sec'
    else:
        return f'{visual_time['seconds']} sec'
def create_date():
    valid_months = ['january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    thirty_day_months = ['april','june','september','november']
    thirtyone_day_months = ['january','march','may','july','august','october','december']
    print('Enter month')
    month = create_input(text=True)
    if not month in valid_months:
        print('Not a valid month')
        return
    print('Enter day')
    day = create_input(integer=True)
    if day < 1:
        print('Invalid day')
        return
    if month in thirtyone_day_months:
        if day > 31:
            print('Invalid day, must be 1-31')
            return
    elif month in thirty_day_months:
        if day > 30:
            print('Invalid day, must be 1-30')
            return
    elif month == 'febuary':
        if day > 28:
            print('Invalid day, must be 1-28')
            return
    data = f'{month.title()} {day}'
    return data
def view_sessions(sessions):
    if not sessions:
        print('No sessions found')
        return
    for session in sessions:
        date = session['date']
        rating = session['rating']
        duration = session['duration']
        print(f'{date} - {duration} *{rating.upper()}')
def create_input(integer=False,text=False,prompt=''):
    if integer:
        try:
            choice = input()
            if not choice:
                print('No input detected')
                return
            choice = int(choice)
        except ValueError:
            print('Invalid input, must be a number')
            return
        return choice
    elif text:
        choice = input(prompt).lower()
        if not choice:
            print('No input detected')
            return
        return choice
def choose_duration():
    valid_durations = [15,30,60]
    print('Choose duration:\n15\n30\n60')
    duration = create_input(integer=True)
    if not duration in valid_durations:
        print('Must choose from given duration')
        return
    print(f'Starting time for {duration} minutes')
    return duration
def create_session(sessions):
    chosen_duration = choose_duration()
    timer_time = chosen_duration*60
    user_ended_duration = timer(timer_time)
    if user_ended_duration:
        duration = user_ended_duration
    else:
        duration = chosen_duration
    overtime = overtime_stopwatch()
    if type(overtime) == str:
        final_duration = duration
    elif type(overtime) == int:
        final_duration = duration + overtime
    print('LOCKIN SESH DONE!!!')
    valid_ratings = ['red','yellow','green']
    print("Date:\n")
    date = create_date()
    if not date:
        return
    print('Rate LOCKIN session')
    rating = create_input(text=True)
    if not rating in valid_ratings:
        print('Rating must be red, yellow, or green')
        return
    displayed_time = display_time(final_duration)
    print(displayed_time)
    session = {
        'date':date,
        'rating':rating,
        'duration':displayed_time
    }
    sessions.append(session)
    return session
def run():
    data = 'user_data.json'
    should_run = True
    if not os.path.isfile(data):
        SESSIONS = []
    else:
        f = open('user_data.json')
        data = json.load(f)
        f.close()
        SESSIONS = data
    while should_run:
        print('====\nStart\nSessions\nQuit')
        choice = create_input(text=True)
        if choice == 'start':
            create_session(SESSIONS)
        elif choice == 'quit':
            should_run = False
            with open('user_data.json', 'w') as f:
                json.dump(SESSIONS,f)
            print('Program terminated')
        elif choice == 'test':
            print('Loop check!')
        elif choice == 'sessions':
            view_sessions(SESSIONS)
def timer(duration):
    print('Enter Ctrl+C to stop early')
    start_time = time.time()
    try:
        for x in range(duration, 0, -1):
            seconds = x%60
            minutes = int(x/60)%60
            hours = int(x/3600)%60
            print(f'{hours:02}:{minutes:02}:{seconds:02}')
            time.sleep(1)
    except KeyboardInterrupt:
        print('Ending session early')
        final_time = int(time.time() - start_time)
        return int(final_time)
def overtime_stopwatch():
    choice = create_input(text=True,prompt="Want to continue your session? Type yes or no\n")
    if choice == 'yes':
        start_time = time.time()
        print('press Ctrl + C to stop!')
        try:
            while True:
                current_time = time.time() - start_time
                seconds = int(current_time)%60
                minutes = int(current_time/60)%60
                hours = int(current_time/3600)%60
                print(f'{hours:02}:{minutes:02}:{seconds:02}')
                time.sleep(1)
        except KeyboardInterrupt:
            end_time = time.time()
            final_time = int(end_time - start_time)
            return int(final_time)
    elif choice == 'no':
        return 'Finishing session...'
    else:
        return f'{choice} not a valid option, finishing session...'   
run()
