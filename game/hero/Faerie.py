import pygame
import os
import copy

from game.artifacts.SpellClass import SpellClass
from game.hero.Character import Character
from game.settings import FAERIE_SPELLS

'''
Class for a hero of race Elf, inherits from Character class
'''


class Faerie(Character):
    def __init__(self, name, side, mana, life, images, active_quest):
        super().__init__(name, side, mana, life, images, active_quest)
        self.fire_spell = SpellClass(FAERIE_SPELLS['fire'], 20, "fire_spell")
        self.thrown_spell = SpellClass(FAERIE_SPELLS['thrown'], 10, "thrown_spell")
        self.flower_spell = SpellClass(FAERIE_SPELLS['flower'], 0, "flower_spell")
        self.chosen_spell = None
        self.spell_direction = 0
        self.race = "Faerie"

    # load images
    # create class to manage spell objects
    # create object of class spell
    # delete some mana
    # move the spell
    # check collision with npcs or other objects

    def use_magic(self, screen, mana, npcs):
        if self.casting_spell:
            self.chosen_spell.move_spell()
            if self.chosen_spell.size < 150:
                if self.chosen_spell.image == self.chosen_spell.image_up or self.chosen_spell.image == self.chosen_spell.image_down:
                    screen.blit(self.chosen_spell.image, (self.chosen_spell.rect.x, self.chosen_spell.rect.y),
                                (0, 0, 50, self.chosen_spell.size))
                else:
                    screen.blit(self.chosen_spell.image, (self.chosen_spell.rect.x, self.chosen_spell.rect.y),
                                (0, 0, self.chosen_spell.size, 50))
            self.chosen_spell.check_spell_npc_collision(npcs, False, self)

        else:
            if self.mana - mana >= 0:
                self.mana -= mana
                self.casting_spell = True
                self.spell_direction = self.direction

    def fight(self, screen, option, npcs):
        mana = 0

        if self.chosen_spell is None:
            if option == 1:
                self.chosen_spell = self.fire_spell
                mana = 20
            elif option == 2:
                self.chosen_spell = self.thrown_spell
                mana = 10
            elif option == 3:
                self.chosen_spell = self.flower_spell
                mana = 20
                self.life += 10

            if self.direction == 'U' and not option == 3:
                self.spell_direction = 0
                self.chosen_spell.rect.x = self.rect.x
                self.chosen_spell.rect.y = self.rect.y - 120
                self.chosen_spell.image = self.chosen_spell.image_up
            elif self.direction == 'D' or option == 3:
                self.spell_direction = 1
                self.chosen_spell.rect.x = self.rect.x
                self.chosen_spell.rect.y = self.rect.y + 30
                self.chosen_spell.image = self.chosen_spell.image_down
            elif self.direction == 'L' and not option == 3:
                self.spell_direction = 2
                self.chosen_spell.rect.x = self.rect.x - 120
                self.chosen_spell.rect.y = self.rect.y
                self.chosen_spell.image = self.chosen_spell.image_left
            else:
                if not option == 3:
                    self.spell_direction = 3
                    self.chosen_spell.rect.x = self.rect.x + 30
                    self.chosen_spell.rect.y = self.rect.y
                    self.chosen_spell.image = self.chosen_spell.image_right

            self.chosen_spell.size = 50
            self.chosen_spell.acceleration = 0.1
            self.chosen_spell.start_x = self.chosen_spell.rect.x
            if not option == 3:
                self.chosen_spell.start_y = self.chosen_spell.rect.y
            else:
                self.chosen_spell.rect.y -= 30
                self.chosen_spell.start_y = self.chosen_spell.rect.y

        self.use_magic(screen, mana, npcs)
