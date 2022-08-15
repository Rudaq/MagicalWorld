import pygame

from game.hero.Character import Character


# Class for a hero of race Barbarian, inherits from Character class
class Barbarian(Character):
    def __init__(self, name, side, mana, life, images, active_quest):
        super().__init__(name, side, mana, life, images, active_quest)
        self.race = "Barbarian"

