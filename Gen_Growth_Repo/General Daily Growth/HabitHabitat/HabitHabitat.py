#HabitHabitat Prototype (Interacting Classes)
import json
import os
class User:
    def __init__(self, username, display_name, animal):
        self.username = username
        self.display_name = display_name
        self.animal = animal
        self.habits = []
        self.habitats = []
    
    def view_habitats(self):
        final = '=====\n'
        for habitat in self.habitats:
            final += f'{habitat.name}\n'
        return final

    def validate_frequency(self, frequnecy):
        if frequnecy < 1 or frequnecy > 7:
            return False
        else:
            return frequnecy
        
    def get_habit(self, habitat):
        name = input("Enter your habit's name:\n").upper()
        try:
            frequency = int(input(f"Enter {name}'s frequency:\n"))
        except ValueError:
            return "INVALID_FREQUENCY"
        frequency = self.validate_frequency(frequency)
        if frequency is False:
            return "INVALID FREQUENCY"
        hab = Habit(name, frequency, habitat.name)
        return hab        
    
    def join_habitat(self, glob_habitats):
        if not glob_habitats:
            return "No habitats currently :("
        print(view_habitats(glob_habitats))
        habitat_name = input("Enter habitat name you wish to join:\n").title()
        habitat = None
        for current_habitat in glob_habitats:
            if current_habitat.name == habitat_name:
                habitat = current_habitat
        if habitat is None:
            return "Habitat not found"
        elif habitat:
            hab = self.get_habit(habitat)
            if hab == "INVALID FREQUENCY":
                return "Frequency input must be a number 1 - 7"
            self.habitats.append(habitat)
            self.habits.append(hab) 
            habitat.members.append(self)
        return f"{habitat_name} joined successfully!"
    def leave_habitat(self, glob_habitats,habitat=None):
        if not glob_habitats:
            return "No habitats currently :("
        habitat_name = input("Enter habitat name you wish to remove:\n").title()
        habitat = None
        for current_habitat in self.habitats:
            if current_habitat.name == habitat_name:
                habitat = current_habitat
        if habitat is None:
            return "Habitat not found"
        else:
            self.habitats.remove(habitat)
            found_habit = False
            for hab in self.habits:
                if hab.habit_origin == habitat.name:
                    self.habits.remove(hab)
                    found_habit = True
            if found_habit is False:
                return f"Habit not found for {habitat.name}"
            found_member = False
            for memb in habitat.members:
                if memb.username == self.username:
                    habitat.members.remove(memb)
                    found_member = True
            if found_member is False:
                return f"Member not found in {habitat.name}"
        return f"{habitat_name} left successfully!"
    def __str__(self):
        return ""
class Habit:
    def __init__(self, name, frequency, habit_origin):
        self.name = name
        self.frequency = frequency
        self.habit_origin = habit_origin
    
    def extract(self):
        data = {
            'name':self.name,
            'frequency':self.frequency,
            'habit_origin':self.habit_origin
        }
        return data
class Habitat:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.members = []
    
    def view_members(self):
        final = 'MEMBERS:\n'
        for memb in self.members:
            final += (f'{memb.username}\n')
        return final
    def extract(self):
        data = {
            'name':self.name,
            'description':self.description
        }
        return data
def view_habitats(glob_habitats):
    if not glob_habitats:
        return('No habitats to show :(')
    final = '=====\n'
    for habitat in glob_habitats:
        final += f'{habitat.name}\n'
    return final
def add_habitat(glob_habitats):
    name = input('Enter habitat name:\n').title()
    if name in glob_habitats:
        return f"{name} is already an existing habitat name!"
    description = input('Enter habitat description:\n')
    habitat = Habitat(name, description)
    glob_habitats.append(habitat)
    return f"{name} created successfully!"
def remove_habitat(glob_habitats, user):
    print(view_habitats(glob_habitats))
    name = input("Enter habitat name:\n").title()
    found_habitat = False
    habitat = None
    for current_habitat in glob_habitats:
        if name == current_habitat.name:
            if current_habitat in user.habitats:
                print(user.leave_habitat(glob_habitats,current_habitat))
            found_habitat = True
            habitat = current_habitat
    if found_habitat:
        glob_habitats.remove(habitat)
        return f"{name} removed successfully!"
    elif found_habitat is False:
        return f"Habitat {name} not found"
def validate_animal(animal):
    valid_animals = ['dog','cat','pig','bird']
    if not animal in valid_animals:
        return False
    else:
        return animal
def get_animal():
    print('Dog | Cat | Bird | Pig')
    animal = validate_animal(input('Enter your animal avatar:\n').lower())
    while animal is False:
        animal = get_animal()
    return animal
def validate_username(username):
    invalid_characters = [' ', '-', '.','!']
    if len(username) < 5:
        return False
    for character in invalid_characters:
        if character in username:
            return False
    else:
        return username
def get_username():
    username = validate_username(input("Enter username:\n"))
    while username is False:
        print("Username must be at least 5 characters long, and may not include special characters (' ', '-', '.', '!')")
        username = get_username()
    return username
def get_display_name():
    display_name = validate_display_name(input("enter display name:\n").title())
    if display_name is False:
        display_name = get_display_name()
    return display_name
def validate_display_name(display_name):
    invalid_characters = ['-', '.','!']
    if len(display_name) < 5:
        return False
    for character in invalid_characters:
        if character in display_name:
            return False
    return display_name
def unpack_habitat_data(habitat_data):
    unpacked_habitats = []
    for habitat in habitat_data:
        unpacked_habitats.append(Habitat(habitat['name'],habitat['description']))
    return unpacked_habitats
def unpack_habit_data(habit_data):
    unpacked_habits = []
    for habit in habit_data:
        unpacked_habits.append(Habit(habit['name'],habit['frequency'],habit['habit_origin']))
    return unpacked_habits
def get_user_data(user):
    username = user.username
    display_name = user.display_name
    animal = user.animal
    habits = user.habits
    habitats = user.habitats
    habits_data = []
    habitats_data = []

    for habit in habits:
        habits_data.append(habit.extract())
    for habitat in habitats:
        habitats_data.append(habitat.extract())

    data = {
        'username':username,
        'display_name':display_name,
        'animal':animal,
        'habits_data':habits_data,
        'habitats_data':habitats_data
    }

    return data
def save_user_data(data):
    with open("user_data_HH.json", "w") as f:
        json.dump(data, f)
    return "Data saved successfully!"
def load_user_data():
    with open("user_data_HH.json", "r") as f:
        data = json.load(f)
    player = User(data['username'], data['display_name'], data['animal'])
    player.habitats = unpack_habitat_data(data['habitats_data'])
    player.habits = unpack_habit_data(data['habits_data'])
    
    return player
def save_glob_data(glob_habitats):
    habitat_data = []
    for habitat in glob_habitats:
        habitat_data.append(habitat.extract())
    with open("glob_data_HH.json", "w") as f:
        json.dump(habitat_data, f)
def load_glob_data():
    with open("glob_data_HH.json", "r") as f:
        glob_habitat_data = json.load(f)
    glob_habitats = []
    for habitat in glob_habitat_data:
        glob_habitats.append(Habitat(habitat['name'],habitat['description']))
    return glob_habitats
def run():
    glob_habitats = load_glob_data()
    is_running = True
    if not os.path.isfile("user_data_HH.json"):
        username = get_username()
        display_name = get_display_name()
        animal = get_animal()
        player = User(username, display_name, animal)
    else:
        player = load_user_data()
    while is_running:
        print('Join\nLeave\nView\nRemove\nCreate\nQuit')
        choice = input().lower()
        if choice == 'join':
            print(player.join_habitat(glob_habitats))
        elif choice ==  'leave':
            print(player.leave_habitat(glob_habitats))
        elif choice == "remove":
            print(remove_habitat(glob_habitats, player))
        elif choice == "create":
            print(add_habitat(glob_habitats))
        elif choice == "quit":
            is_running = False
            print('Program teriminated')
            data = get_user_data(player)
            save_user_data(data)
            save_glob_data(glob_habitats)
        elif choice == "view":
            print('View global habitats\nView personal habitats')
            choice2 = input().lower()
            if choice2 == 'global':
                print(view_habitats(glob_habitats))
            elif choice2 == 'personal':
                print(player.view_habitats())
            else:
                print("Choice must be either 'global' or 'personal' ")
        else:
            print(f'{choice} is not a valid option')
coding = Habitat('Coding', 'Coding everydayyy fooo')
run()
