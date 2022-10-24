import os
from pathlib import Path

import pygame

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent
print("Current Directory", current)
print(path)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super(CameraGroup, self).__init__()
        self.display_surf = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surf.get_size()[0] / 2
        self.half_h = self.display_surf.get_size()[1] / 2

        # ground
        self.ground_surf = pygame.image.load(os.path.join(path, 'resources/graphics/tilemap/map.png')).convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))
        self.ground_offset = 0

    def custom_draw(self, hero, npcs, screen):
        # ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surf.blit(self.ground_surf, ground_offset)

        # active elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            if hasattr(sprite, 'sprite_type') and sprite.sprite_type != 'hero':
                self.display_surf.blit(sprite.image, sprite.rect.topleft)

        self.display_surf.blit(hero.image, hero.rect.topleft)