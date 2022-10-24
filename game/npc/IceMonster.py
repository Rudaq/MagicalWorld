from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent
# Class for a npc of type Ice Monster, inherits from Npc class inheriting from Character class
class IceMonster(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation, collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Ice Monster"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "yeti_blood.PNG"))
        tusk_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "yeti_tusk.PNG"))
        skin_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "ice_monster_skin.PNG"))
        self.blood = Artifact(blood_image, 10, 'Ice Monster Blood', None)
        self.skin = Artifact(skin_image, 15, 'Ice Monster Skin', None)
        self.tusk = Artifact(tusk_image, 15, 'Ice Monster Tusk', None)
        self.artifacts.add(self.tusk, self.blood, self.skin)
        ice_image = pygame.image.load(os.path.join(path, "resources/graphics/particles", "small_cube.PNG"))
        self.npc_attack = AttackClass(ice_image, 20, 10, 'ice monster attack')





