from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Dragon(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Dragon"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 30, 'Dragon Blood', None)
        eyeball_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "dragon_eyeball.PNG"))
        self.eyeball = Artifact(eyeball_image, 10, 'Dragon Eyeball', None)
        self.artifacts.add(self.blood, self.eyeball)
        dragon_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "fire.png"))
        self.npc_attack = AttackClass(dragon_attack, 20, 10, 'dragon attack')
