import math

import pygame.sprite
from settings import FAERIE_SPELLS


def fire_spell(npc, hero):
    if hero.attack_direction == 'D':
        expected_y = npc.rect.y + 200
        while npc.rect.y < expected_y:
            npc.rect.y += 2
    elif hero.attack_direction == 'U':
        expected_y = npc.rect.y - 200
        while npc.rect.y > expected_y:
            npc.rect.y -= 2
    elif hero.attack_direction == 'L':
        expected_x = npc.rect.x - 200
        while npc.rect.x > expected_x:
            npc.rect.x -= 2
    else:
        expected_x = npc.rect.x + 200
        while npc.rect.x < expected_x:
            npc.rect.x += 2


class AttackClass(pygame.sprite.Sprite):
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

    def move_attack(self):
        self.size += (self.speed * self.acceleration)
        self.acceleration += 0.05

    def attack_acceleration(self):
        self.size += (self.speed * self.acceleration)
        self.acceleration += 0.01

    def fire_spell(npc, hero):
        if hero.attack_direction == 'D':
            expected_y = npc.rect.y + 200
            while npc.rect.y < expected_y:
                npc.rect.y += 2
        elif hero.attack_direction == 'U':
            expected_y = npc.rect.y - 200
            while npc.rect.y > expected_y:
                npc.rect.y -= 2
        elif hero.attack_direction == 'L':
            expected_x = npc.rect.x - 200
            while npc.rect.x > expected_x:
                npc.rect.x -= 2
        else:
            expected_x = npc.rect.x + 200
            while npc.rect.x < expected_x:
                npc.rect.x += 2
    def check_attack_npc_collision(self, npcs, option, hero):
        for npc in npcs:
            if npc.rect.colliderect(self.rect):
                if (self.start_x + self.size) >= npc.rect.x:
                    if option:
                        npc.life += self.strength
                        if npc.life > 100:
                            npc.life = 100 - int(npc.life % 100)
                    if self.spell_type == "fire_spell":
                        fire_spell(npc, hero)
                        npc.life -= self.strength
                    else:
                        npc.life -= self.strength
                    if npc.life < 0:
                        npc.life = 0
                hero.performing_action = False
                hero.in_attack = False
                break
