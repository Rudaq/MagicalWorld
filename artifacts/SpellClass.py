import math

import pygame.sprite


class SpellClass(pygame.sprite.Sprite):
    def __init__(self, image, strength):
        super().__init__()
        self.strength = strength
        self.image = image
        self.image_right = image
        self.image_left = pygame.transform.flip(self.image, True, False)
        self.image_down = pygame.transform.rotate(self.image, 270)
        self.image_up = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 50
        self.acceleration = 0.3
        self.size = 50
        self.start_x = 0
        self.start_y = 0

    def move_spell(self):
        self.size += (self.speed * self.acceleration)
        self.acceleration += 0.05
