import pygame
import os
import copy

from game.artifacts.AttackClass import AttackClass
from game.hero.Character import Character
from game.settings import FAERIE_SPELLS

'''
Class for a hero of race Elf, inherits from Character class
'''

class Faerie(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Faerie"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.fire_spell = AttackClass(FAERIE_SPELLS['fire'], 20, "fire_spell")
        self.thrown_spell = AttackClass(FAERIE_SPELLS['thrown'], 10, "thrown_spell")
        self.flower_spell = AttackClass(FAERIE_SPELLS['flower'], 0, "flower_spell")
        self.chosen_attack = None
        self.attack_direction = 0

    # load images
    # create class to manage spell objects
    # create object of class spell
    # delete some mana
    # move the spell
    # check collision with npcs or other objects

    def fight(self, screen, option, npcs):
        mana = 0
        if self.chosen_attack is None:
            if option == 1:
                self.chosen_attack = self.fire_spell
                mana = 20
            elif option == 2:
                self.chosen_attack = self.thrown_spell
                mana = 10
            elif option == 3:
                self.chosen_attack = self.flower_spell
                if self.life < 100:
                    self.life += 10
                    mana = 20

            if self.direction == 'U' and not option == 3:
                self.attack_direction = 0
                self.chosen_attack.rect.x = self.rect.x
                self.chosen_attack.rect.y = self.rect.y - 120
                self.chosen_attack.image = self.chosen_attack.image_up
            elif self.direction == 'D' or option == 3:
                self.attack_direction = 1
                self.chosen_attack.rect.x = self.rect.x
                self.chosen_attack.rect.y = self.rect.y + 30
                self.chosen_attack.image = self.chosen_attack.image_down
            elif self.direction == 'L' and not option == 3:
                self.attack_direction = 2
                self.chosen_attack.rect.x = self.rect.x - 120
                self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_left
            else:
                if not option == 3:
                    self.attack_direction = 3
                    self.chosen_attack.rect.x = self.rect.x + 30
                    self.chosen_attack.rect.y = self.rect.y
                    self.chosen_attack.image = self.chosen_attack.image_right

            self.chosen_attack.size = 50
            self.chosen_attack.acceleration = 0.1
            self.chosen_attack.start_x = self.chosen_attack.rect.x

            if not option == 3:
                self.chosen_attack.start_y = self.chosen_attack.rect.y
            else:
                self.chosen_attack.rect.y -= 30
                self.chosen_attack.start_y = self.chosen_attack.rect.y

        self.attack(screen, mana, npcs)
