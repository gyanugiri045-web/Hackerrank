# numbers = [1,2,3]
# print(type[numbers])


# class person:
#     name = "john"


# person_one = person()
# person_two = person()
# person_three = person()
# person_four = person()

# print(person_one.name)

from datetime import date

class Person:

    species = "Human"
    person_created = 0


    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.person_created += 1

    @classmethod
    def get_created_person_number(cls):
        return f"There are {Person.person_created} are created."
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = date.today().year - year
        return cls(name, age)
    
    def greet(self):
        return f"hi mr.{self.name}"
    
    def likes(self, things):
        return f"{self.name} likes{things}"
    
    def welcome(self):
        message = self.greet()
        print(message, "welcome to our app.")

    def __repr__(self):
        return f"{self.name} is {self.age} year old."
        
    
person_one = Person("rajes", 20)
person_two = Person("rohan", 21)
person_three = Person.from_birth_year("sara", 2000)
print(person_three.__dict__)
print(Person.get_created_person_number())

# print(person_one.greet())
# print(person_two.greet())

# print(person_one.likes("ice ceam"))
# print(person_two.likes("candy"))

# person_one.welcome()
# person_two.welcome()