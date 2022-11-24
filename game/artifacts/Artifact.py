import pygame

import pygame.sprite


class Artifact(pygame.sprite.Sprite):
    def __init__(self, image, points, name, small_image):
        super().__init__()
        self.points = points
        self.name = name
        self.image = image
        self.small_image = small_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.clicked = False

    def show(self, x, y, all_artifacts, screen):
        self.rect.x = x
        self.rect.y = y
        all_artifacts.add(self)
        # all_artifacts.update()
        # all_artifacts.draw(screen)

