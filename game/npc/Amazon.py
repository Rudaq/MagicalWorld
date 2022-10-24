from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Amazon(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Amazon"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Amazon Blood', None)
        spare_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "amazon_spare.PNG"))
        self.spare = Artifact(spare_image, 10, 'Amazon Spare', None)
        self.artifacts.add(self.blood, self.spare)
        sage_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "sage.PNG"))
        self.sage = Artifact(sage_image, 10, 'Sage', None)
        self.gifts.add(self.sage)
        amazon_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "spear.PNG"))
        self.npc_attack = AttackClass(amazon_attack, 20, 10, 'amazon attack')
        self.context = Path("../NLP/context/AmazonContext.txt").read_text()
