from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Unicorn(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Unicorn"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG")).convert_alpha()
        self.blood = Artifact(blood_image, 10, 'Unicorn Blood', None)
        horn_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "horn.PNG")).convert_alpha()
        self.horn = Artifact(horn_image, 10, 'Unicorn Horn', None)
        heart_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "unicorn_heart.PNG")).convert_alpha()
        self.heart = Artifact(heart_image, 10, 'Unicorn Heart', None)
        self.artifacts.add(self.blood, self.horn, self.heart)
        unicorn_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "spell.PNG")).convert_alpha()
        self.npc_attack = AttackClass(unicorn_attack, 20, 10, 'unicorn attack')
