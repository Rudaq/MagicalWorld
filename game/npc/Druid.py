from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass
import random

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Druid, inherits from Npc class inheriting from Character class
class Druid(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Druid"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG")).convert_alpha()
        self.blood = Artifact(blood_image, 10, 'Druid Blood', None)
        self.artifacts.add(self.blood)
        fire_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "sacred_fire.PNG")).convert_alpha()
        self.fire = Artifact(fire_image, 20, 'Sacred Fire', None)
        self.gifts.add(self.blood)
        druid_attack = pygame.image.load(os.path.join(path, "resources/graphics/particles", "druid_attack.PNG")).convert_alpha()
        self.npc_attack = AttackClass(druid_attack, 20, 10, 'druid attack')


