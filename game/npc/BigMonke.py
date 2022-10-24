from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class BigMonke(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Big Monke"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        gem_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "dwarven_gem.PNG"))
        self.gem = Artifact(gem_image, 10, 'Dwarven Gem', None)
        self.gifts.add(self.gem)
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Monke Blood', None)
        heart_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "monke_heart.PNG"))
        self.heart = Artifact(heart_image, 10, 'Monke Heart', None)
        self.artifacts.add(self.blood, self.heart, self.gem)

        big_monke_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "banana.PNG"))
        self.npc_attack = AttackClass(big_monke_attack, 20, 10, 'big monke attack')
