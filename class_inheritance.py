# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim1 = Bulldog("Jim", 12)
print(jim1.description())
print(isinstance(jim1, Bulldog))

# Child classes have specific attributes
# and behaviors as well
print(jim1.run("slowly"))

# Is jim an instance of Dog()?
print(isinstance(jim1, Dog))

# Is julie an instance of Dog()?
julie1 = Dog("Julie", 10)
print(isinstance(julie1, Dog))

# Is johnny walker an instance of Bulldog()
johnnywalker2 = RussellTerrier("Johnny Walker", 4)
print(johnnywalker2.description())

print(isinstance(johnnywalker2, Bulldog))

# Is julie and instance of jim?
# print(isinstance(julie, jim))