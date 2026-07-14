#HabitHabitat Prototype (Interacting Classes)
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
            if hab == "INVALID_FREQUENCY":
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
class Habit:
    def __init__(self, name, frequency, habit_origin):
        self.name = name
        self.frequency = frequency
        self.habit_origin = habit_origin
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
def run():
    glob_habitats = [coding]
    is_running = True
    username = input("Enter username:\n")
    display_name = input("Enter display name:\n").title()
    animal = input("Enter your animal avatar:\n").lower()
    player = User(username, display_name, animal)
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
