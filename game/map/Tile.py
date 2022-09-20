import pygame

from game.settings import TILE_SIZE


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, arrays, groups, sprite_type, inflation=(0, 0),
                 surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        super(Tile, self).__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.inflation = inflation
        # inflate - take the rect and change the size
        self.groups = groups
        if sprite_type == 'nature_object':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILE_SIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)

        for array in arrays:
            array.append(self)
        for group in groups:
            group.add(self)