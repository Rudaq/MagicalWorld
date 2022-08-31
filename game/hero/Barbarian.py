import pygame
from artifacts.AttackClass import AttackClass
from hero.Character import Character
from settings import BARBARIAN_ACTIONS, HERO_ANIMATIONS


# Class for a hero of race Barbarian, inherits from Character class
class Barbarian(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Barbarian"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.sword_attack = AttackClass(BARBARIAN_ACTIONS['sword'], 15, 10, 'sword_attack')
        self.furry = AttackClass(HERO_ANIMATIONS['Barbarian']['up'], 15, 5, 'furry_attack')

    def fight(self, screen, option, npcs):
        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.sword_attack
            elif option == 2:
                self.attack_type = self.furry
                print("option 2")
            else:
                print("option 2")

            if self.direction == 'U':
                self.attack_type.rect.x = self.rect.x
                if not option == 1:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_up
            elif self.direction == 'D':
                self.attack_type.rect.x = self.rect.x
                if not option == 1:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_down
            elif self.direction == 'L':
                if not option == 1:
                    self.attack_type.rect.x = self.rect.x + 30
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                if not option == 1:
                    self.attack_type.rect.x = self.rect.x + 120
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_right

            self.attack_type.size = 50
            self.attack_type.acceleration = 0.1
            self.attack_type.start_x = self.attack_type.rect.x
            self.attack_type.start_y = self.attack_type.rect.y

        if option == 2 or option == 3:
            self.attack(screen, npcs)
        if option == 1:
            self.use_weapon(screen, npcs)
