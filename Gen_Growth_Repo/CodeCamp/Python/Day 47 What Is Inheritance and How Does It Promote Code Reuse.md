# What Is Inheritance and How Does It Promote Code Reuse?\

## Inheritance
- Inheritance, a subclass (or child class) can use the attributes and methods of a base class (or parent class). This allows you to reuse code, create clear class hierarchies, and customize behavior without rewriting everything.

### Example
```python
class Parent:
    # Parent attributes and methods

class Child(Parent):
    # Child inherits, extends, and/or overrids where necessary
```

- For the Child class to inherit from the Parent class, you have to pass the Parent to the Child

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return f'{self.name} makes a sound

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

jack = Dog('Jack')
print(jack.sound()) # Jack makes a sound
print(jack.bark) # woof! woof!! woof!!!
```

- You can also override parent function methods to use class variables

```python
class Animal(self, name):
    self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    bark = 'woof woof'

    def sound(self):
        return f'{self.name} barks {self.bark}

jack = Dog('Jack')
print(jack.sound()) #Jack barks woof woof
```

### Super Function
- If you want to keep the return value of sound and add the bark class variable later, you can extend sound() by using the super() function.

#### Example
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'
    

class Dog(Animal):
    bark = woof woof woof

    def sound(self):
        base = super().sound()
        return f'{base}, then {self.name} barks {self.bark}'
    
jack = Dog('Jack')
print(jack.sound()) # Jack makes a sound, then Jack barks woof woof woof
```

### Multiple Inheritance
- Multiple inheritance is where a child class inherits from more than one parent class

```python
class Parent:
    # attributes and methods for Parent

class Child:
    # Attributes and method for Child

class Grandchild(Parent, Child):
    # Attributes and method for both Parent, Child and Grandchild
    # GrandChild can combine or override behavior from each
```

#### Example
```python
class Walker:
    def walk(self):
        return 'I can walk on land'
    
class Swimmer(self):
    def swim(self):
        return 'I can swim in water'

class Amphibian(Walker, Swimmer):
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."
    
frog = Amphibian('Freddy')
print(frog.introduce())
# Outpute: I'm Freddy the frog. I can walk on land and I can swim in water.
```

# What Is Polymorphism and How Does It Promote Code Reuse?

## Polymorphism
- Polymorphism allows methods in different clases to share the same name, but perform different tasks. You call the same method name on different objects and each responds in its own way.

```python
class A:
    def action(self):

class B:
    def action(self):

class C:
    def action(self):

Class().method() # Works for A, B, or C
```
### Example
```python
class Cat:
    def speak(self):
        return 'A cat meow'

class Bird:
    def speak(self):
        return 'A bird tweet'

class Monkey(self):
    def speak(self):
        return 'A monkey ooh ooh aah aah ooh ooh aah aah

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())
```

- When you pass in a cat, bird, or monkey, it calls the speak() method of the object and prints the result. Because each class defines speak() differently, youg et different outputs from the same function.

### Example 2
```python
class Twitter:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f" Tweet: '{self.content}'"

class Instagram:
    def __init__(self,content):
        self.content = content
    
    def post(self):
        return f' Instagram post: "{self.content}"'

class LinkedIn:
    def __init__(self, content):
        self.content = content
    
    def post(self):
        return f' LinkedIn post:"{self.content}"'

def start(social_media):
    print(social_media.post())


# Instances
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

# The polymorphic calls - same function, different outputs
start(tweet) # 🐦 Tweet: 'Just learned Python polymorphism!'
start(photo) # 📸 Instagram Post: 'Sunset vibes 🌅'
start(article) # 💼 LinkedIn Article: 'Why OOP matters in 2024'
```
## Inheritance-Based Polymorphism
- In inheritance-based polymorphism, a parent calss defines a method and multiple child classes override that method in their own way. You can then call the same method on any child object, and it behaves different depending on which class it is.

```python
class Animal:
    def speak(self):
        return 'Some generic sound'

class Cat(Animal):
    def speak(self):
        return 'A cat meow'

class Dog(Aniaml):
    def speak(self):
        return 'A dog barks woof woof'

class Monkey(Animal):
    def speak(self):
        return 'A monkey  ooh ooh aah aah ooh ooh'

print(Cat().speak()) # A cat meow
print(Dog().speak()) # A dog barks woof woof
print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh
print(Animal().speak()) # Some generic sound
```

# What is Name Mangling and How Does it Work?

## Name Mangling
- Before we get into name mangling, here's a reminder on the single underscore and double underscore notation

- The single underscore is for a convention that tells programmers that an attribute should only be used internally and should not be accessed outside of the class.

- The double underscore however, literally prevents any programmers from accessing that attribute from outside of the class

```python
class Example:
    def __init(self):
        self._internal = "I can be accessed from outside of the class, but shouldn't"
        self.__private = "You cannot access me directly from outside of the class

obj = Example()

print(obj._interal) # I can be accessed from outside the class, but should not
print(obj.__private) #AttributeError: 'Example' object has no attribute '__private'
```

- Prefixing an attribute with a double underscore triggers Python's name mangling process, in which Python internally renames the attribute by adding an underscore and the class name as a prefix, turning __attribute into _ClassName__attribute

- The purpose of name mangling is to precent accidental attribute and method overriding when you use inheritance.

### Example
```python
class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}
```
- Without name mangling, the original data attribute from parent.__data wouldve been erased.

```python
class Parent:
   def __init__(self):
       self.data = 'Parent data'

class Child(Parent):
   def __init__(self):
       super().__init__()
       self.data = 'Child data'

c = Child()
print(c.__dict__)  # {'data': 'Child data'}
```
