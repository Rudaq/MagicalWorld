from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class Tiger(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Tiger"
        self.collision_sprites = collision_sprites
        self.can_talk = True
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "blood.PNG"))
        self.blood = Artifact(blood_image, 10, 'Tiger Blood', None)
        fur_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "tigers_fur.PNG"))
        self.fur = Artifact(fur_image, 20, 'Tiger Fur', None)
        self.artifacts.add(self.blood, self.fur)
        necklace_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "tiger_necklace.PNG"))
        self.magic_necklace = Artifact(necklace_image, 20, 'Magic Necklace', None)
        self.gifts.add(self.magic_necklace)
        tiger_attack = pygame.image.load(
            os.path.join(path, "resources/graphics/particles", "tiger_attack.PNG"))
        self.npc_attack = AttackClass(tiger_attack, 20, 10, 'tiger attack')

    def take_gift(self, hero, artifact, npcs, screen):
        self.gifts.add(artifact)

        if hero.active_quest is not None \
                and hero.active_quest.active_task is not None \
                and hero.active_quest.active_task.artifact == artifact.name \
                and hero.active_quest.active_task.npc_take_artifact == self.race:
            if hero.active_quest.active_task == 'feed_wild_tiger' \
                    and artifact.name == 'Raven Meat':
                hero.add_life(20)
            print(self.race + ": Your task is completed!")
            if hero.active_quest.task_completed(hero, npcs):
                return True

        elif len(hero.active_quest.skipped_tasks) > 0:
            for task in hero.active_quest.skipped_tasks:
                if task.artifact == artifact.name \
                        and task.npc_take_artifact == self.race:
                    print(self.race + ": Thank you for your gift")

        return False
