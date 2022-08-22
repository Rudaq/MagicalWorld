import math

import pygame.sprite
from game.settings import FAERIE_SPELLS


class SpellClass(pygame.sprite.Sprite):
    def __init__(self, image, strength, spell_type):
        super().__init__()
        self.strength = strength
        self.spell_type = spell_type
        self.image = image
        self.image_right = image
        self.image_left = pygame.transform.flip(self.image, True, False)
        self.image_down = pygame.transform.rotate(self.image, 270)
        self.image_up = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 50
        self.acceleration = 0.1
        self.size = 0.1
        self.start_x = 0
        self.start_y = 0

    def move_spell(self):
        self.size += (self.speed * self.acceleration)
        self.acceleration += 0.05


    def fire_spell(self, npc, hero):
        if hero.spell_direction == 'D':
            expected_y = npc.rect.y + 200
            while npc.rect.y < expected_y:
                npc.rect.y += 2
        elif hero.spell_direction == 'U':
            expected_y = npc.rect.y - 200
            while npc.rect.y > expected_y:
                npc.rect.y -= 2
        elif hero.spell_direction == 'L':
            expected_x = npc.rect.x - 200
            while npc.rect.x > expected_x:
                npc.rect.x -= 2
        else:
            expected_x = npc.rect.x + 200
            while npc.rect.x < expected_x:
                npc.rect.x += 2

    def check_spell_npc_collision(self, npcs, option, hero, screen):
        for npc in npcs:
            if npc.rect.colliderect(self.rect):
                if (self.start_x + self.size) >= npc.rect.x:
                    if option:
                        npc.life += self.strength
                        npc.life = 100 - int(npc.life % 100)

                    else:
                        if self.spell_type == "fire_spell":
                            self.fire_spell(npc, hero)
                        elif self.spell_type == "thrown_spell":
                            npc.thrown(hero.spell_direction, screen)
                        elif self.spell_type == "tree_spell":
                            npc.image = FAERIE_SPELLS['tree']
                        elif self.spell_type == "frozen_spell":
                            npc.image = FAERIE_SPELLS['frozen']

                    npc.life -= self.strength
                    if npc.life < 0:
                        npc.life = 0
                hero.casting_spell = False
                hero.in_spell = False
                break

