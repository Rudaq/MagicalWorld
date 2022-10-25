import pygame

from game.settings import TILE_SIZE


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, arrays, groups, sprite_type, surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        super(Tile, self).__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface

        self.groups = groups

        self.rect = self.image.get_rect(topleft=pos)

        for array in arrays:
            array.append(self)
        for group in groups:
            group.add(self)