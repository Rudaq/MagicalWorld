import pygame
import os

from game.artifacts.AttackClass import AttackClass
from game.hero.Character import Character
from game.settings import ELF_SPELLS

'''
Class for a hero of race Elf, inherits from Character class
'''

# Class for a hero of race Elf, inherits from Character class
class Elf(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.earth_spell = AttackClass(ELF_SPELLS['earth'], 25, 20, 'earth_spell')
        self.heal_spell = AttackClass(ELF_SPELLS['healing'], -15, 30, 'heal_spell')
        self.shoot_arrow = AttackClass(ELF_SPELLS['arrow'], 20, 10, 'shoot_arrow')
        self.race = "Elf"
        self.collision_sprites = collision_sprites
        self.pos = pos

    # load images
    # create class to manage spell objects
    # create object of class spell
    # delete some mana
    # move the spell
    # check collision with npcs or other objects
    def heal_spell_attack(self, npc):
        npc.life += self.attack_type.strength
        if npc.life > 100:
            npc.life = 100 - int(npc.life % 100)

    def fight(self, screen, option, npcs):
        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.earth_spell
            elif option == 2:
                self.attack_type = self.heal_spell
            else:
                self.attack_type = self.shoot_arrow

            if self.direction == 'U':
                self.attack_type.rect.x = self.rect.x
                if not option == 3:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_up
            elif self.direction == 'D':
                self.attack_type.rect.x = self.rect.x
                if not option == 3:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_down
            elif self.direction == 'L':
                if not option == 3:
                    self.attack_type.rect.x = self.rect.x + 30
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                if not option == 3:
                    self.attack_type.rect.x = self.rect.x + 120
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_right

            self.attack_type.size = 50
            self.attack_type.acceleration = 0.1
            self.attack_type.start_x = self.attack_type.rect.x
            self.attack_type.start_y = self.attack_type.rect.y

        if option == 1 or option == 2:
            self.attack(screen, npcs)
        else:
            self.use_weapon(screen, npcs)
