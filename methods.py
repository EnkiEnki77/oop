# Methods are functions that belong to a class or object, they define it's behavior

class Hero:
    def __init__(self, name:str, power:list[str], speed:int, health:int):
        self.name  = name
        self.speed = speed
        self.power = power
        self.health = health

    def use_power(self, power:str):
        if self.health == 0:
            print(f"{self.name} is dead, he can't use powers")
            return
        if power in self.power:
            print(f"{self.name} used the {self.power[self.power.index(power)]} power")
        else:
            print(f"{self.name} doesn't have the {power} power")

    def take_damage(self, damage:int):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} is now dead!")
        else:
            print(f"{self.name} takes {damage} damage. His health is {self.health}")

superman = Hero("Superman", ["super strength", "laser vision", "flight", "super speed"], 100_000, 1_000_000)

superman.take_damage(20)
superman.use_power("laser vision")
superman.use_power("flight")

superman.take_damage(500_000)
superman.take_damage(500_000)
superman.use_power("teleportation")