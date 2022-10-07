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
        dark_wizard_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "dark_wizard_attack.PNG"))
        self.npc_attack = AttackClass(dark_wizard_attack, 20, 10, 'dark wizard attack')

    def take_gift(self, hero, artifact, npcs, screen):
        self.artifacts.add(artifact)
        if hero.active_quest is not None \
                and hero.active_quest.active_task is not None \
                and hero.active_quest.active_task.artifact == artifact.name \
                and hero.active_quest.active_task.npc_take_artifact == self.race:
            print(self.race + ": Your quest is completed!")
            if hero.active_quest.active_task.name == 'snowman_nose' and artifact.name == 'Snowman Nose':
                self.give_hint(screen)
            hero.active_quest.task_completed(hero, npcs)
        else:
            print(self.race + ": Thank you for your gift")

        if artifact.name == 'Snowman Nose':
            self.image =  pygame.image.load(
            os.path.join(path, "resources/graphics/npc", "snowman_nose.PNG"))

    def give_hint(self, screen):
        screen_width = math.floor(screen.get_size()[0])
        quest_top_right = screen_width - 400
        restore = datetime.now()
        time_diff = datetime.now() - restore
        time_sec = time_diff.total_seconds()

        time_to_display = 30 - time_sec
        while time_to_display > 0:
            screen.blit(GUI_IMAGES['scroll'], (quest_top_right, 100))
            w = 200
            h = quest_top_right + 110
            text = "Pay attention, this information will be read only once...  The Immortality Flower was last seen in " \
                   "the Dreary Forest below the Great Tree.. "


            text_list = wrap_text(text, 25, False)
            for text in text_list:
                draw_text(text, h, w, 14, BLACK, screen)
                w += 20
                if h == 1170:
                     h += 5
                else:
                    h -= 5


