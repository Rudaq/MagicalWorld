from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Leprechaun(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Leprechaun"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Leprechaun Blood', None)
        self.artifacts.add(self.blood)
        gold_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "gold.PNG"))
        self.gold_bar = Artifact(gold_image, 10, 'Gold Bar', None)
        self.gifts.add(self.gold_bar)
        leprechaun_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "coin.PNG"))
        self.npc_attack = AttackClass(leprechaun_attack, 20, 10, 'leprechaun attack')
