from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Farmer(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Farmer"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Farmer Blood', None)
        self.artifacts.add(self.blood)
        hemmer_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "hammer.PNG"))
        self.hammer = Artifact(hemmer_image, 10, 'Hammer', None)
        self.gifts.add(self.hammer)
        farmer_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "grabie.PNG"))
        self.npc_attack = AttackClass(farmer_attack, 20, 10, 'farmer attack')
