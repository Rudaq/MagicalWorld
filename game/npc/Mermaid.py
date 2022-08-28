from npc.Npc import Npc
from artifacts.Artifact import Artifact
import pygame
import os
from pathlib import Path
current = os.path.dirname(os.path.realpath(__file__))

path = Path(__file__).resolve().parent.parent.parent



# Class for a npc of type Mermaid, inherits from Npc class inheriting from Character class
class Mermaid(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation, collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Mermaid"
        self.collision_sprites = collision_sprites
        self.can_talk = False
        image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        image2 = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "corn.PNG"))
        self.blood = Artifact(image, 10, 'Mermaid blood')
        self.corn = Artifact(image2, 15, 'corn')
        self.corn2 = Artifact(image2, 15, 'corn2')
        self.artifacts.add(self.corn, self.blood, self.corn2)



    # Method move to stop mermaid from moving (not moving; on the beach)
    def move(self, direction="R", dx=0, dy=0):
        pass


