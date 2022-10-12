from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Orc, inherits from Npc class inheriting from Character class
class Orc(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Orc"
        self.collision_sprites = collision_sprites
        self.can_talk = False
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "orc_blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Orc Blood', None)
        mace_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "orc_mace.PNG"))
        self.mace = Artifact(mace_image, 10, 'Orc Mace', None)
        self.artifacts.add(self.blood, self.mace)
        ice_image = pygame.image.load(os.path.join(path, "resources/graphics/particles", "small_cube.PNG"))
        self.npc_attack = AttackClass(ice_image, 20, 10, 'ice attack')
