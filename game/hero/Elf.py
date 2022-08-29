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

    def use_bow(self, screen, npcs):
        if self.in_attack:
            # self.chosen_spell.size = 5
            self.attack_type.move_attack()
            draw = False
            if self.attack_type.image == self.attack_type.image_up:
                self.attack_type.rect.y -= self.attack_type.size
                if self.attack_type.rect.bottom > self.attack_type.start_y - 150:
                    draw = True
            elif self.attack_type.image == self.attack_type.image_down:
                self.attack_type.rect.y += self.attack_type.size
                if self.attack_type.rect.top < self.attack_type.start_y + 150:
                    draw = True
            elif self.attack_type.image == self.attack_type.image_left:
                self.attack_type.rect.x -= self.attack_type.size
                if self.attack_type.rect.right > self.attack_type.start_x - 150:
                    draw = True
            else:
                self.attack_type.rect.x += self.attack_type.size
                if self.attack_type.rect.left < self.attack_type.start_x + 150:
                    draw = True

            if draw:
                screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y))
            self.attack_type.check_attack_npc_collision(self, npcs)

        else:
            if self.mana - self.attack_type.mana >= 0:
                self.mana -= self.attack_type.mana
                self.attack_type.size = 5
                self.in_attack = True
                self.attack_direction = self.direction


    def fight(self, screen, option, npcs):

        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.earth_spell
            elif option == 2:
                self.attack_type = self.heal_spell
            else:
                self.attack_type = self.shoot_arrow

            if self.direction == 'U':
                self.attack_direction = 0
                self.attack_type.rect.x = self.rect.x
                if not option == 3:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_up
            elif self.direction == 'D':
                self.attack_direction = 1
                self.attack_type.rect.x = self.rect.x
                if not option == 3:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_down
            elif self.direction == 'L':
                self.attack_direction = 2
                if not option == 3:
                    self.attack_type.rect.x = self.rect.x + 30
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                self.attack_direction = 3
                if not option == 3:
                    self.attack_type.rect.x = self.rect.x + 30
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
            self.use_bow(screen, npcs)
