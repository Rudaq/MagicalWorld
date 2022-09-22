import pygame

import pygame.sprite


class Artifact(pygame.sprite.Sprite):
    def __init__(self, image, points, name):
        super().__init__()
        self.points = points
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.clicked = False

    def show(self, x, y, all_artifacts, screen):
        self.rect.x = x
        self.rect.y = y
        all_artifacts.add(self)
        all_artifacts.update()
        all_artifacts.draw(screen)

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
