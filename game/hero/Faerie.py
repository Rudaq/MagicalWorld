import pygame
import os

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
        self.thrown_spell = SpellClass(FAERIE_SPELLS['thrown'], 20, "thrown_spell")
        self.tree_spell = SpellClass(FAERIE_SPELLS['leaf'], 20, "tree_spell")
        self.frozen_spell = SpellClass(FAERIE_SPELLS['ice'], 20, "frozen_spell")
        self.chosen_spell = None
        self.spell_direction = 0
        self.race = "Faerie"

    # load images
    # create class to manage spell objects
    # create object of class spell
    # delete some mana
    # move the spell
    # check collision with npcs or other objects

    def use_bow(self, screen, mana):
        if self.casting_spell:
            # self.chosen_spell.size = 5
            self.chosen_spell.move_spell()
            draw = False
            if self.chosen_spell.image == self.chosen_spell.image_up:
                self.chosen_spell.rect.y -= self.chosen_spell.size
                if self.chosen_spell.rect.bottom > self.chosen_spell.start_y - 150:
                    draw = True
            elif self.chosen_spell.image == self.chosen_spell.image_down:
                self.chosen_spell.rect.y += self.chosen_spell.size
                if self.chosen_spell.rect.top < self.chosen_spell.start_y + 150:
                    draw = True
            elif self.chosen_spell.image == self.chosen_spell.image_left:
                self.chosen_spell.rect.x -= self.chosen_spell.size
                if self.chosen_spell.rect.right > self.chosen_spell.start_x - 150:
                    draw = True
            else:
                self.chosen_spell.rect.x += self.chosen_spell.size
                if self.chosen_spell.rect.left < self.chosen_spell.start_x + 150:
                    draw = True

            if draw:
                screen.blit(self.chosen_spell.image, (self.chosen_spell.rect.x, self.chosen_spell.rect.y))

        else:
            if self.mana - mana >= 0:
                self.mana -= mana
                self.chosen_spell.size = 5
                self.casting_spell = True
                self.spell_direction = self.direction

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
                self.chosen_spell = self.tree_spell
                mana = 10
            else:
                self.tree_spell

            if self.direction == 'U':
                self.spell_direction = 0
                self.chosen_spell.rect.x = self.rect.x
                self.chosen_spell.rect.y = self.rect.y - 120
                self.chosen_spell.image = self.chosen_spell.image_up
            elif self.direction == 'D':
                self.spell_direction = 1
                self.chosen_spell.rect.x = self.rect.x
                self.chosen_spell.rect.y = self.rect.y + 30
                self.chosen_spell.image = self.chosen_spell.image_down
            elif self.direction == 'L':
                self.spell_direction = 2
                self.chosen_spell.rect.x = self.rect.x - 120
                self.chosen_spell.rect.y = self.rect.y
                self.chosen_spell.image = self.chosen_spell.image_left
            else:
                self.spell_direction = 3
                self.chosen_spell.rect.x = self.rect.x + 30
                self.chosen_spell.rect.y = self.rect.y
                self.chosen_spell.image = self.chosen_spell.image_right

            self.chosen_spell.size = 50
            self.chosen_spell.acceleration = 0.1
            self.chosen_spell.start_x = self.chosen_spell.rect.x
            self.chosen_spell.start_y = self.chosen_spell.rect.y

        self.use_magic(screen, mana, npcs)
