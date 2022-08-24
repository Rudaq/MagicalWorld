import pygame

from game.hero.Character import Character


# Class for a hero of race Barbarian, inherits from Character class
class Barbarian(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Barbarian"
        self.collision_sprites = collision_sprites
        self.pos = pos

