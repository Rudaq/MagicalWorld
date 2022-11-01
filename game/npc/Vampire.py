from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


class Vampire(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Vampire"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Vampire Blood', None)
        fang_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "fang.PNG"))
        self.fang = Artifact(fang_image, 5, 'Vampire Fang', None)
        self.artifacts.add(self.blood, self.fang)
        potion_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "immortality_potion.PNG"))
        self.potion = Artifact(potion_image, 50, 'Immortality Potion', None)
        self.gifts.add(self.potion)
        vampire_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "vampire_attack.PNG"))
        self.npc_attack = AttackClass(vampire_attack, 20, 10, 'vampire attack')
        self.context = Path("../NLP/context/VampireContext.txt").read_text()
