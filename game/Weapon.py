import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, hero):
        super().__init__()
        self.sprite_type = 'weapon'
        direction = hero.direction

        # graphic
        self.image = pygame.image.load(r'resources/graphics/weapon/sword.png').convert_alpha()

        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=hero.rect.midright + pygame.math.Vector2(0, 16))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=hero.rect.midleft + pygame.math.Vector2(0, 16))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=hero.rect.midbottom + pygame.math.Vector2(-10, 0))
        else:
            self.rect = self.image.get_rect(midbottom=hero.rect.midtop + pygame.math.Vector2(-10, 0))