import pygame

import pygame.sprite

#class for making ikons for NPC while choosing them to give a gift

class NpcRepresent(pygame.sprite.Sprite):
    def __init__(self, represent):
        super().__init__()
        self.represent = represent
        self.name = represent.name
        self.image = represent.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.clicked = False
        self.clicked_counter = 0

