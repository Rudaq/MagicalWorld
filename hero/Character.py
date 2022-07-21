import random

import pygame

SPRITE_SIZE = 50


class Character(pygame.sprite.Sprite):
    def __init__(self, name, side, mana, life, image, image_left, image_right, active_quest, race):
        super().__init__()
        height = SPRITE_SIZE
        width = SPRITE_SIZE
        self.width = width
        self.height = height
        self.image = image
        self.rect = self.image.get_rect()

        self.name = name
        self.side = side
        self.race = race
        self.mana = mana
        self.life = life
        self.equipment = []
        self.points = 0

        self.direction = "U"
        self.right = image_right
        self.left = image_left

        self.active_quest = active_quest
        self.my_text = ''
        self.hero_turn = False
        self.in_dialog = False

    def move(self, direction, dx, dy):
        self.direction = direction
        self.rect.x += dx
        self.rect.y += dy

    def talk(self):
        print("HELLO")

    def collect_weapon(self, weapon):
        self.equipment.append(weapon)

    def fight(self):
        print("This is a fight!!")
        if self.mana > 0:
            self.mana -= random.randint(0, self.mana)