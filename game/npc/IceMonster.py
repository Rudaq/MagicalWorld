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
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "mermaid_blood.PNG"))
        self.mermaid_blood = Artifact(blood_image, 10, 'Mermaid Blood')
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "yeti_blood.PNG"))
        tusk_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "yeti_tusk.PNG"))
        ice_image = pygame.image.load(os.path.join(path, "resources/graphics/particles", "small_cube.PNG"))
        self.blood = Artifact(blood_image, 10, 'Ice Monster Blood')
        self.tusk = Artifact(tusk_image, 15, 'Ice Monster Tusk')
        self.artifacts.add(self.tusk, self.blood, self.mermaid_blood)
        self.npc_attack = AttackClass(ice_image, 20, 10, 'ice monster attack')

   # Method move to stop mermaid from moving (not moving; on the beach)
    def move(self, direction="R", dx=0, dy=0):
        pass



