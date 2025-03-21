# If we wanted to create an object that represents a super hero we could do this:
# hero_1 = {"name": "Iron Man", "power": "Repulsor Beams", "health": 100, "speed": 80}
# What if we wanted to make another hero object with the same attributes but different values?
# We have to write out the whole thing from scratch again, but with the different values.
# hero_2= {"name": "Deadpool", "power": "Invulnerability", "health": 1000, "speed": 100}

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
        # Attributes are the properties that belong to an object.
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed


    def use_power(self, power: str):
        if self.health == 0:
            print(f"{self.name} is dead, he can't use powers")
            return
        if power in self.power:
            print(f"{self.name} used the {self.power[self.power.index(power)]} power")
        else:
            print(f"{self.name} doesn't have the {power} power")


    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} is now dead!")
        else:
            print(f"{self.name} takes {damage} damage. His health is {self.health}")

def main():
    iron_man = Hero("Iron Man", "Repulsor Beams", 100, 100)
    dead_pool = Hero("Deadpool", "Invulnerability", 100, 100)

    # To access an objects attributes we use dot notation.
    print(iron_man.name, iron_man.power)
    print(dead_pool.name, dead_pool.power)

    # We can also modify attributes
    iron_man.power = "Advanced Repulsor Beams"
    iron_man.speed = 100
    print(iron_man.name, iron_man.speed, iron_man.power)

    # We can change the type of an attribute, since python is not statically typed, but this is bad practice
    # iron_man.power = 43

if __name__ == '__main__':
    main()