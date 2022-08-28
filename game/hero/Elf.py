import pygame
import os

from artifacts.AttackClass import AttackClass
from hero.Character import Character
from settings import ELF_SPELLS

'''
Class for a hero of race Elf, inherits from Character class
'''


class Elf(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.earth_spell = AttackClass(ELF_SPELLS['earth'], 25, 'earth_spell')
        self.heal_spell = AttackClass(ELF_SPELLS['healing'], -15, 'heal_spell')
        self.shoot_arrow = AttackClass(ELF_SPELLS['arrow'], 20, 'shoot_arrow')
        self.race = "Elf"
        self.collision_sprites = collision_sprites
        self.pos = pos

    # load images
    # create class to manage spell objects
    # create object of class spell
    # delete some mana
    # move the spell
    # check collision with npcs or other objects

    def use_bow(self, screen, mana, npcs):
        if self.performing_action:
            # self.chosen_spell.size = 5
            self.chosen_attack.move_attack()
            draw = False
            if self.chosen_attack.image == self.chosen_attack.image_up:
                self.chosen_attack.rect.y -= self.chosen_attack.size
                if self.chosen_attack.rect.bottom > self.chosen_attack.start_y - 150:
                    draw = True
            elif self.chosen_attack.image == self.chosen_attack.image_down:
                self.chosen_attack.rect.y += self.chosen_attack.size
                if self.chosen_attack.rect.top < self.chosen_attack.start_y + 150:
                    draw = True
            elif self.chosen_attack.image == self.chosen_attack.image_left:
                self.chosen_attack.rect.x -= self.chosen_attack.size
                if self.chosen_attack.rect.right > self.chosen_attack.start_x - 150:
                    draw = True
            else:
                self.chosen_attack.rect.x += self.chosen_attack.size
                if self.chosen_attack.rect.left < self.chosen_attack.start_x + 150:
                    draw = True

            if draw:
                screen.blit(self.chosen_attack.image, (self.chosen_attack.rect.x, self.chosen_attack.rect.y))
            self.chosen_attack.check_attack_npc_collision(npcs, False, self)

        else:
            if self.mana - mana >= 0:
                self.mana -= mana
                self.chosen_attack.size = 5
                self.performing_action = True
                self.attack_direction = self.direction

    def fight(self, screen, option, npcs):
        mana = 0

        if self.chosen_attack is None:
            if option == 1:
                self.chosen_attack = self.earth_spell
                mana = 20
            elif option == 2:
                self.chosen_attack = self.heal_spell
                mana = 30
            else:
                self.chosen_attack = self.shoot_arrow
                mana = 10

            if self.direction == 'U':
                self.attack_direction = 0
                self.chosen_attack.rect.x = self.rect.x
                if not option == 3:
                    self.chosen_attack.rect.y = self.rect.y+ 30
                else:
                    self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_up
            elif self.direction == 'D':
                self.attack_direction = 1
                self.chosen_attack.rect.x = self.rect.x
                if not option == 3:
                    self.chosen_attack.rect.y = self.rect.y + 30
                else:
                    self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_down
            elif self.direction == 'L':
                self.attack_direction = 2
                if not option == 3:
                    self.chosen_attack.rect.x = self.rect.x + 30
                else:
                    self.chosen_attack.rect.x = self.rect.x
                self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_left
            else:
                self.attack_direction = 3
                if not option == 3:
                    self.chosen_attack.rect.x = self.rect.x + 30
                else:
                    self.chosen_attack.rect.x = self.rect.x
                self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_right

            self.chosen_attack.size = 50
            self.chosen_attack.acceleration = 0.1
            self.chosen_attack.start_x = self.chosen_attack.rect.x
            self.chosen_attack.start_y = self.chosen_attack.rect.y

        if option == 1 or option == 2:
            self.attack(screen, mana, npcs, True)
        else:
            self.use_bow(screen, mana, npcs)
