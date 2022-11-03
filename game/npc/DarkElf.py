from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class DarkElf(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Dark Elf"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Dark Elf Blood', None)
        self.artifacts.add(self.blood)
        magic_blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "magic_blood.PNG"))
        self.magic_blood = Artifact(magic_blood_image, 10, 'Magic Blood', None)
        self.gifts.add(self.magic_blood)
        stone_donkey_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "stoneDonkey.PNG"))
        self.stone_donkey = Artifact(stone_donkey_image, 10, 'Travel Companion', None)
        self.gifts.add(self.stone_donkey)
        dark_elf_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/weapon", "arrow.PNG"))
        self.npc_attack = AttackClass(dark_elf_attack, 20, 10, 'dark elf attack')
