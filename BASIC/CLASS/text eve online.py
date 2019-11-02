import random


class making_frigate:
    def __init__(self):
        self.shield = random.randrange(300, 600)
        self.armor = random.randrange(400, 700)
        self.hull = random.randrange(200, 400)
        self.dps = random.randrange(50,200)

    def dps(self):
        return self.dps
    def shield_damaged(self, damage):
        self.shield = self.shield - damage

    def armor_damage(self, damage):
        self.armor = self.armor - damage

    def hull_damage(self, damage):
        self.hull = self.hull - damage

    def explosion(self):
        print("Boom")


user = eve_text_online()
computer = eve_text_online()
print("your shield:", user.shield,"               enemy's shield:", computer.shield)
print("your armor:", user.armor,"               enemy's armor:", computer.armor)
print("your hull:", user.hull,"               enemy's hull:", computer.hull)
print("your dps:", user.dps,"               enemy's dps:", computer.dps)