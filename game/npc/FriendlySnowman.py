from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass
from NLP.dialog_generation.GenerateNpcDialog import wrap_text, draw_text
from game.settings import GUI_IMAGES, BLACK
import math
from datetime import datetime

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class FriendlySnowman(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Friendly Snowman"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Friendly Snowman Blood', None)
        self.artifacts.add(self.blood)
        self.npc_attack = None

    def take_gift(self, hero, artifact, npcs, screen):
        self.artifacts.add(artifact)
        if hero.active_quest is not None \
                and hero.active_quest.active_task is not None \
                and hero.active_quest.active_task.artifact == artifact.name \
                and hero.active_quest.active_task.npc_take_artifact == self.race:
            print(self.race + ": Your task is completed!")
            hero.active_quest.task_completed(hero, npcs)

        elif len(hero.active_quest.skipped_tasks) > 0:
            for task in hero.active_quest.skipped_tasks:
                if task.artifact == artifact.name \
                        and task.npc_take_artifact == self.race:
                    print(self.race + ": Thank you for your gift")

        if artifact.name == 'Snowman Nose':
            self.image = pygame.image.load(
                os.path.join(path, "resources/graphics/npc", "snowman_nose.PNG"))
