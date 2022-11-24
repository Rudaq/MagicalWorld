from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Orc, inherits from Npc class inheriting from Character class
class Orc(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Orc"
        self.collision_sprites = collision_sprites
        self.can_talk = False
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "orc_blood.PNG")).convert_alpha()
        self.blood = Artifact(blood_image, 10, 'Orc Blood', None)
        mace_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "orc_mace.PNG")).convert_alpha()
        self.mace = Artifact(mace_image, 10, 'Orc Mace', None)
        self.artifacts.add(self.blood, self.mace)
        potion_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "magic_potion.PNG")).convert_alpha()
        self.potion = Artifact(potion_image, 10, 'Life Potion', None)
        self.gifts.add(self.potion)
        mud_image = pygame.image.load(os.path.join(path, "resources/graphics/particles", "mud.PNG")).convert_alpha()
        self.npc_attack = AttackClass(mud_image, 20, 10, 'orc attack')

