from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class EscapingVegetable(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Escaping Vegetable"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        carrot_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "small_carrot.PNG")).convert_alpha()
        self.carrot = Artifact(carrot_image, 10, 'Vegetables', None)
        self.artifacts.add(self.carrot)
        self.npc_attack = None
