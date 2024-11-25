class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        # Private property. Can use within the class but not through objects
        self.__age = age
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    
    # Returns values by just calling the object
    def __str__(self):
        return f"{self.name}, {self.age}"

class Cat(Animal):
    # Class attribute (shared by all instances)
    species = "Felis catus"
    
    # Instance method
    def meow(self):
        return f"{self.name} says meow!"

class Dog(Animal):
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)
cat1 = Cat("Billo Rani", 2)
cat2 = Cat("Conditioner", 4)

# print(dog1.bark())
# print(dog2.get_age())
# print(dog1.species)
# print(dog1.age)
# print(dog1)

# print(cat1.meow())
# print(cat2.get_age())
# print(cat1.species)
# print(cat1.age)
# print(cat1)

print(isinstance(dog1, Animal))