from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass
current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent

# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class DarkWizard(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation, collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Dark Wizard"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Dark Wizard Blood', None)
        necklace_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "mermaid_necklace.PNG"))
        self.necklace = Artifact(necklace_image, 15, 'Mermaid Necklace', None)
        self.artifacts.add(self.blood, self.necklace)
        potion_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "magic_potion.PNG"))
        self.potion = Artifact(potion_image, 15, 'Magic Potion', None)
        healing_potion_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "healing_potion.PNG"))
        self.healing_potion = Artifact(healing_potion_image, 15, 'Healing Potion', None)
        snake_skin_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "snake_skin.PNG"))
        self.snake_skin = Artifact(snake_skin_image, 20, 'Snake Skin', None)
        scroll_image = pygame.image.load(os.path.join(path, "resources/GUI", "scroll_small.PNG"))
        self.scroll = Artifact(scroll_image, 10, 'Incantation Scroll', None)
        self.gifts.add(self.potion, self.snake_skin, self.healing_potion, self.scroll)

        dark_wizard_attack = pygame.image.load(os.path.join(path, "resources/graphics/particles", "dark_wizard_attack.PNG"))
        self.npc_attack = AttackClass(dark_wizard_attack, 20, 10, 'dark wizard attack')