from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Faerie(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Faerie"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG")).convert_alpha()
        self.blood = Artifact(blood_image, 10, 'Faerie Blood', None)
        self.artifacts.add(self.blood)
        magical_crystal_image = pygame.image.load(
            os.path.join(path, "resources/graphics/artifacts", "magical_crystal.PNG")).convert_alpha()
        self.magical_crystal = Artifact(magical_crystal_image, 15, 'Magical Crystal', None)
        magic_dust_image = pygame.image.load(
            os.path.join(path, "resources/graphics/artifacts", "magic_dust.PNG")).convert_alpha()
        self.magic_dust = Artifact(magic_dust_image, 20, 'Magic Dust', None)
        self.gifts.add(self.magical_crystal, self.magic_dust)
        faerie_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "spell.PNG")).convert_alpha()
        self.npc_attack = AttackClass(faerie_attack, 20, 10, 'faerie attack')
        self.context = Path("../NLP/context/FairiesContext.txt").read_text()
