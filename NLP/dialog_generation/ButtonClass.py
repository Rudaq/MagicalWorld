import pygame.sprite
WHITE = (255, 255, 255)


class ButtonClass(pygame.sprite.Sprite):
    def __init__(self, width, height, name):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.name = name