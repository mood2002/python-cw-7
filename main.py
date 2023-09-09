# Part 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

first_person = Person("mariam", 16)
print(first_person.name, first_person.age)

# Part 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age > 18:
            print("You have too much responsibilities")
        else:
            print("Lucky you")

first_person = Person("mariam", 16)
first_person.is_adult()

# Part 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old"

first_person = Person("mariam", 16)
print(first_person)