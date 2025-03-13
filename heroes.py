# If we wanted to create an object that represents a super hero we could do this:
hero_1 = {"name": "Iron Man", "power": "Repulsor Beams", "health": 100, "speed": 80}
# What if we wanted to make another hero object with the same attributes but different values?
# We have to write out the whole thing from scratch again, but with the different values.
hero_2= {"name": "Deadpool", "power": "Invulnerability", "health": 1000, "speed": 100}

# What if we then wanted to create 50 more super hero objects with the same attributes? Thisll get out of
# hand fast. Especially for objects with more attributes and method.

# This is where classes come in. They act as a blueprint for the structure of an object. You then just have
# to instantiate the class, passing it the data it needs, but the attributes and methods are already setup.
# This makes things much more DRY, less messy, and more scalable.

class Hero:
    # The __init__ method is what actually creates an object and initializes its attributes
    # The self param is what allows us to actually attach attributes to our object.
    # self represents the instance of the class, its used to access variables and methods associated with
    # the class.
    # When you instantiate a class, Python passes an empty object to the __init__ method as self.
    def __init__(self, name, power, health, speed):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

iron_man = Hero("Iron Man", "Repulsor Beams", 100, 100)
dead_pool = Hero("Deadpool", "Invulnerability", 100, 100)

print(iron_man.name, iron_man.power)
print(dead_pool.name, dead_pool.power)