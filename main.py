# Fundamentally, programs are a set of instructions for manipulating data in a meaningful way.
# There are 3 steps:
# 1. Taking an input of data
# 2. Manipulating input data
# 3. Outputting manipulated input data.

# OOP is a coding paradigm that allows us to think of software in terms of objects and how they interact
# with each other.
# Programs are made up of lots of objects, entities, or things. They are often the nouns of your projects:
# A person, house, car, etc.
# These objects will have properties such as name, age, address, etc. (represented by attributes), and
# behaviors such as walking, talking, breathing, etc (represented by methods)
# Objects are like bundles of data that get passed around throughout the life of your program.

# To create multiple objects with similar properties and methods, we define the structure of these objects
# with a class, and instantiate it to create an object, passing in the individualized data for that specific
# object.
# The process of creating an object from a class is called instantiation, and objects that come from classes
# are an instance of that class.

# Classes define a type. For example, if we define a variable initializing it with a string value, the variable
# is a refernece to an object. This is because all string values are instances of the builtin str class.

# Instantiation is taking a class, and creating an object from that class.

class Door:
    def __init__(self, height, color, is_locked=False):
        self.height = height
        self.color = color
        self.is_locked = is_locked

    def open(self):
        pass

    def close(self):
        pass

    def toggle_locked(self):
        self.is_locked = not self.is_locked

# Instantiated Door class, created object of type Door.
door1 = Door(85, "red")
# Another instantiation of the Door class, creating an object of type Door.
door2 = Door(95, "grey", True)

# Instances of a class are built off the same blueprint, but are independent from each other in memory.
# Changes to one instance wont affect other instances. 
door1.toggle_locked()
print(door1.is_locked)
print(door2.is_locked)
