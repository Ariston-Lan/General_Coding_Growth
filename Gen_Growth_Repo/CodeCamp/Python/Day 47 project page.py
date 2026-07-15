class Habit:
    def __init__(self, habit_name, frequency):
        self.habit_name = habit_name
        self.frequency = frequency
    
    
class Habitat:
    def __init__(self, name, description):
        self._name = name
        self.description = description
        self.members = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        invalid_characters = ['/',',',']','.',':',';','<','>','?','!','|']
        if len(self.name) < 3:
            raise ValueError('Name must be more than 3 characters long')
        for character in invalid_characters:
            if character in self.name:
                raise ValueError('Name must have no special characters')
        self.name = name
    def add_user(self, user):
        self.members.append(user)
        return f'{user.username} has joined {self.name} successfully!'

    def __str__(self):
        return f'{self.name} | {self.description} | {self.display_members()}'
    
    def remove_user(self, user):
        for memb in self.members:
            if memb.username == user.username:
                final = f'{memb.username} has been removed from {self.name}'
                self.members.remove(memb)
                return final
        raise ValueError('Member not found')

    def display_members(self):
        final = ''
        for memb in self.members:
            final += f'{memb.username}, '
        return final

class User:
    def __init__(self, username):
        self._username = username
        self.habits = []
        self.habitats = []
    
    def add_habitat(self, habitat):
        self.habitats.append(habitat)
    
    def add_habit(self, habit):
        self.habits.append(habit)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        invalid_characters = ['-', '.', ',', ' ', '/', ';', ':', '"', "'"]
        if len(username) < 3:
            raise ValueError ('Username must have more than 3 characters')
        for character in invalid_characters:
            if character in self.username:
                raise ValueError ('Username must have no special characters')
        self.username = username
    
    
    def dispaly_habits(self):
        final = ''
        for animal in self.habits:
            final += f'[{animal.name},{animal.habit_name}]'
        return final
    def display_habitats(self):
        final = ''
        for habitat in self.habitats:
            final += f'{habitat.name}'
        return final
    def __str__(self):
        return f'Username: {self.username} | Habits: {self.dispaly_habits()} | Habitats: {self.display_habitats()}'

    def remove_habitat(self, habitat):
        for hab in self.habitats:
            if hab.name == habitat.name:
                self.habitats.remove(hab)
            else:
                raise ValueError('Habitat not found')
        
    def remove_habit(self, habitat):
        try:
            index = self.get_habit(habitat)
        except ValueError as e:
            raise ValueError (e)
        habit = self.habits.pop(index)
        return habit
   
    def get_habit(self, habitat):
        for index, habit in enumerate(self.habits):
            if habit.habitat.name == habitat.name:
                return index
        raise ValueError(f'No habit found from {habitat.name}')
class Animal(Habit):
    def __init__(self, habit_name, frequency, name, habitat, owner):
        super().__init__(habit_name, frequency)
        
        self.name = name
        self.habitat = habitat
        self.happiness=100
        self.state = 'ACTIVE'
        self.owner = owner
    
    def animal_activity(self):
        raise ValueError('Error, Animal Class should override this method')

class Owl(Animal):
    def __init__(self, habit_name, frequency, name, habitat, state):
        super().__init__(habit_name, frequency, name, habitat, state)
    
    def animal_activity(self):
        if self.happiness == 100:
            return f'{self.name} LOVES you!'
        elif self.happiness>80:
            return f'{self.name} flies around cuz he happy and shi'
        elif self.happiness>50:
            return f'{self.name} seems a little sad, you should give him a worm or sumthn'
        elif self.happiness >= 1:
            return f'{self.name} is on the verge of crashing out'
        elif self.happiness == 0:
            return f'{self.name} HATES you. Good job'
    
    def __str__(self):
        return f'{self.name} | Owl | {self.happiness} | {self.frequency} | {self.habitat} | {self.habit_name}'

class Wolf(Animal):
    def __init__(self, habit_name, frequency, name, habitat, state):
        super().__init__(habit_name, frequency, name, habitat, state)
    
    def animal_activity(self):
        return f'{self.name} is a wolf who does wolf things'

class Fox(Animal):
    def __init__(self, habit_name, frequency, name, habitat, state):
        super().__init__(habit_name, frequency, name, habitat, state)
    
    def animal_activity(self):
        return f'{self.name} is a fox who does fox things'


class HabitHabitatSystem:
    def __init__(self):
        self._global_habitats = []
        self._users = []
    
    def run(self):
        running = True
        while running:
            print('Join\nCreate\nQuit\nNew User\nLeave Habitat\nWilderness')
            choice = input().lower()
            if choice == 'join':
                self.join_habitat()
            elif choice =='create':
                self.create_habitat()
            elif choice == 'quit':
                running = False
                print('Program terminated')
            elif choice == 'check':
                self.check()
            elif choice =='new user':
                self.create_user()
            elif choice =='leave' or choice =='leave habitat':
                self.leave_habitat()
            elif choice == 'wilderness':
                self.display_wild_animals()
            else:
                print('Choice not found')

    wilderness = []

    animals = {
        'wolf':Wolf,
        'owl':Owl,
        'fox':Fox
    }

    @property
    def global_habitats(self):
        return self._global_habitats
    
    @property
    def users(self):
        return self._users

    def create_user(self):
        username = input("Enter your username:\n")
        try:
            new_user = User(username)
        except ValueError as e:
            print(e)
            return
        for user in self.users:
            if user.username == new_user.username:
                raise ValueError('Username cannot already exist')
        self.users.append(new_user)

    def create_habitat(self):
        name = input("Enter your Habitat's name:\n")
        description = input(f"Enter {name}'s description\n")

        try:
            habitat = Habitat(name, description)
        except ValueError as e:
            print(e)
            return
        self.global_habitats.append(habitat)
        for hab in self.global_habitats:
            print(f'{hab.name} | {hab.description}')
    
    def get_user(self):
        username = input("Enter Username:\n")
        for user in self.users:
            if user.username == username:
                return user
        raise ValueError (f"No user with the username '{username}' found")
    def display_habitats(self):
        for habitat in self.global_habitats:
            print(habitat)

    def display_wild_animals(self):
        for animal in HabitHabitatSystem.wilderness:
            print(f'{animal} | Previous owner: {animal.owner.username}')

    def get_habitat(self, prompt=''):
        if prompt:
            habitat_name_choice = input(f'{prompt}\n')
        else:
            habitat_name_choice = input("What Habitat do you wish to join?\n").lower()
        for habitat in self.global_habitats:
            if habitat.name.lower() == habitat_name_choice:
                return habitat
        raise ValueError(f'No habitat the name "{habitat_name_choice}" found')


    def create_habit(self, habitat, user):
        habit_name = input("What's the name of your habit?:\n")
        try:
            frequency = int(input("How many days per week are you dedicating to this habit?\n"))
        except ValueError:
            print("Frequency must be an integer")
            return
        habit = self.create_animal(habitat, habit_name, frequency, user)
        return habit
    
    def create_animal(self, habitat, habit_name, frequency, user):
        valid_species = ['owl','wolf','fox']
        for animal in valid_species:
            print(animal)
        species = input("Choose an animal to represent your habit!\n").lower()
        if species not in valid_species:
            raise ValueError('Invalid Species')
        name = input("Name your animal companion:\n")
        user_animal = HabitHabitatSystem.animals[species](habit_name, frequency, name, habitat, user)
        return user_animal





    def join_habitat(self):
        try:
            user = self.get_user()
            self.display_habitats()
            habitat = self.get_habitat()
            habit = self.create_habit(habitat, user)
        except ValueError as e:
            print(e)
            return
        
        habitat.add_user(user)
        user.add_habitat(habitat)
        user.add_habit(habit)

    def check(self):
        for user in self.users:
            print(user)
        for habitat in self.global_habitats:
            print(habitat)
    
    def leave_habitat(self):
        try:
            user = self.get_user()
            print(user.display_habitats())
            habitat = self.get_habitat('Enter the Habitat you wish to leave')
            habit = user.remove_habit(habitat)
            HabitHabitatSystem.wilderness.append(habit)
            user.remove_habitat(habitat)
            habitat.remove_user(user)
        except ValueError as e:
            print(e)

        
            

system = HabitHabitatSystem()
system.run()