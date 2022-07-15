import pygame
from hero.Character import Character

SPRITE_SIZE = 50


class Dwarf(Character):
    def __init__(self, name, side, mana, life, image, image_left, image_right, race, active_quest):
        super().__init__(name, side, mana, life, image, image_left, image_right, race, active_quest)
