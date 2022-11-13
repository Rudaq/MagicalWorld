from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Snake(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Snake"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG")).convert_alpha()
        self.blood = Artifact(blood_image, 10, 'Snake Blood', None)
        skin_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "snake_skin.PNG")).convert_alpha()
        self.skin = Artifact(skin_image, 10, 'Snake Skin', None)
        self.artifacts.add(self.blood, self.skin)
        snake_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "dark_wizard_attack.PNG")).convert_alpha()
        self.npc_attack = AttackClass(snake_attack, 20, 10, 'snake attack')
