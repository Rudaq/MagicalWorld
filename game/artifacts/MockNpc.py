import pygame

import pygame.sprite


# class for making icons for NPC while choosing them to give a gift
class MockNpc(pygame.sprite.Sprite):
    def __init__(self, npc):
        super().__init__()
        self.npc = npc
        self.name = npc.name
        self.image = npc.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.clicked = False
        self.clicked_counter = 0
