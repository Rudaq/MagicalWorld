import pygame
import os
import copy

from artifacts.AttackClass import AttackClass
from hero.Character import Character
from settings import FAERIE_SPELLS

'''
Class for a hero of race Elf, inherits from Character class
'''


class Faerie(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Faerie"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.fire_spell = AttackClass(FAERIE_SPELLS['fire'], 20, 20, "fire_spell")
        self.thrown_spell = AttackClass(FAERIE_SPELLS['thrown'], 40, 10, "thrown_spell")
        self.flower_spell = AttackClass(FAERIE_SPELLS['flower'], 0, 20, "flower_spell")

    # load images
    # create class to manage spell objects
    # create object of class spell
    # delete some mana
    # move the spell
    # check collision with npcs or other objects
    def fight(self, screen, option, npcs):
        mana = 0
        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.fire_spell

            elif option == 2:
                self.attack_type = self.thrown_spell

            elif option == 3:
                self.attack_type = self.flower_spell
                self.add_life(20)

            if self.direction == 'U' and not option == 3:
                self.attack_direction = 0
                self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y + 30
                self.attack_type.image = self.attack_type.image_up

            elif self.direction == 'D' or option == 3:
                self.attack_direction = 1
                self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y + 30
                self.attack_type.image = self.attack_type.image_down

            elif self.direction == 'L' and not option == 3:
                self.attack_direction = 2
                self.attack_type.rect.x = self.rect.x + 30
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                if not option == 3:
                    self.attack_direction = 3
                    self.attack_type.rect.x = self.rect.x + 30
                    self.attack_type.rect.y = self.rect.y
                    self.attack_type.image = self.attack_type.image_right

            self.attack_type.size = 50
            self.attack_type.acceleration = 0.1
            self.attack_type.start_x = self.attack_type.rect.x

            if not option == 3:
                self.attack_type.start_y = self.attack_type.rect.y
            else:
                self.attack_type.rect.y -= 30
                self.attack_type.start_y = self.attack_type.rect.y

        self.attack(screen, npcs)

    def fire_spell_attack(self, npc):
        if self.attack_direction == 'D':
            expected_y = npc.rect.y + 200
            while npc.rect.y < expected_y:
                npc.rect.y += 2

        elif self.attack_direction == 'U':
            expected_y = npc.rect.y - 200
            while npc.rect.y > expected_y:
                npc.rect.y -= 2

        elif self.attack_direction == 'L':
            expected_x = npc.rect.x - 200
            while npc.rect.x > expected_x:
                npc.rect.x -= 2
        else:
            expected_x = npc.rect.x + 200
            while npc.rect.x < expected_x:
                npc.rect.x += 2
        npc.life -= self.attack_type.strength




