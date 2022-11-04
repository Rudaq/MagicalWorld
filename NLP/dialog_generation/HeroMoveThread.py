# Thread supporting the npc side of the dialog
import threading

import pygame


class HeroMoveThread(threading.Thread):
    def __init__(self, hero, screen, npcs, all_sprites_group, sprites_to_move_opposite):
        super().__init__()
        self.hero = hero
        self.screen = screen
        self.npcs = npcs
        self.all_sprites = all_sprites_group
        self.sprites_to_move_opposite = sprites_to_move_opposite

    def run(self):
        clock = pygame.time.Clock()
        while True:
            if self.hero.moving:
                self.hero.move(self.hero.movement, self.hero.dir_opposite, self.hero.mov_x, self.hero.mov_y, self.hero.sign, self.all_sprites,
                          self.sprites_to_move_opposite)
            clock.tick(30)
