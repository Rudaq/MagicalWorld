from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Smith(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Smith"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG")).convert_alpha()
        self.blood = Artifact(blood_image, 10, 'Smith Blood', None)
        self.artifacts.add(self.blood)
        tools_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "tools.PNG")).convert_alpha()
        self.tools = Artifact(tools_image, 10, 'Tools', None)
        shovel_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "shovel.PNG")).convert_alpha()
        self.shovel = Artifact(shovel_image, 10, 'Shovel', None)
        sword_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "new_sword.PNG")).convert_alpha()
        self.new_sword = Artifact(sword_image, 10, 'New Sword', None)
        gem_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "purple_gem.PNG")).convert_alpha()
        self.gem = Artifact(gem_image, 10, 'Purple Gem', None)
        banana_image = pygame.image.load(os.path.join(path, "resources/graphics/particles", "banana.PNG")).convert_alpha()
        self.banana = Artifact(banana_image, 10, 'Banana', None)
        self.gifts.add(self.tools, self.shovel, self.new_sword, self.gem, self.banana)
        smith_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/weapon", "axe.png")).convert_alpha()
        self.npc_attack = AttackClass(smith_attack, 20, 10, 'weapon attack')
        self.context = Path("../NLP/context/SmithContext.txt").read_text()

