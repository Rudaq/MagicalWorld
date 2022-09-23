from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass
current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Mermaid, inherits from Npc class inheriting from Character class
class Mermaid(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Mermaid"
        self.collision_sprites = collision_sprites
        self.can_talk = False
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "mermaid_blood.PNG"))
        necklace_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "mermaid_necklace.PNG"))
        horn_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "horn.PNG"))
        self.blood = Artifact(blood_image, 10, 'Mermaid Blood')
        self.necklace = Artifact(necklace_image, 15, 'Mermaid Necklace')
        self.horn = Artifact(horn_image, 10, 'Unicorn Horn')
        self.artifacts.add(self.necklace, self.blood, self.horn)
        mermaid_attack = pygame.image.load(os.path.join(path, "resources/graphics/particles", "mermaid_attack.PNG"))
        self.npc_attack = AttackClass(mermaid_attack, 20, 10, 'mermaid attack')


    # Method move to stop mermaid from moving (not moving; on the beach)
    def move(self, direction="R", dx=0, dy=0):
        pass

    def move_in_fight(self, hero):
        pass
