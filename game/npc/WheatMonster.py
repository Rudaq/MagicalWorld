from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Wheat Monster, inherits from Npc class inheriting from Character class
class WheatMonster(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Wheat Monster"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        wheat_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "wheat.PNG"))
        self.wheat = Artifact(wheat_image, 10, 'Wheat', None)
        self.artifacts.add(self.wheat)
        wheat_monster_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "wheat_monster_attack.PNG"))
        self.npc_attack = AttackClass(wheat_monster_attack, 20, 10, 'wheat monster attack')
