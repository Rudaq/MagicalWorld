import pygame
from hero.Character import Character

SPRITE_SIZE = 50


# Class for a hero of race Wizard, inherits from Character class
class Wizard(Character):
    def __init__(self, name, side, mana, life, images, race, active_quest):
        super().__init__(name, side, mana, life, images, race, active_quest)
