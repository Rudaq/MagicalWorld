from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Leprechaun(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Leprechaun"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        gold_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "gold.PNG")).convert_alpha()
        self.gold_bar = Artifact(gold_image, 10, 'Gold Bar', None)
        self.gifts.add(self.gold_bar)

        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG")).convert_alpha()
        self.blood = Artifact(blood_image, 10, 'Leprechaun Blood', None)
        pot_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "pot_of_gold.PNG")).convert_alpha()
        self.pot = Artifact(pot_image, 10, 'Pot of Gold', None)
        self.artifacts.add(self.blood, self.gold_bar, self.pot)
        leprechaun_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "coin.PNG")).convert_alpha()
        self.npc_attack = AttackClass(leprechaun_attack, 20, 10, 'leprechaun attack')
        self.context = Path("../NLP/context/LeprechaunContext.txt").read_text()
