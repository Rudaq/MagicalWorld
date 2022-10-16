from npc.Npc import Npc
import pygame
from artifacts.Artifact import Artifact
import os
from pathlib import Path
from artifacts.AttackClass import AttackClass

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent


# Class for a npc of type Mermaid, inherits from Npc class inheriting from Character class
class Mermaid(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation,
                 collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Mermaid"
        self.collision_sprites = collision_sprites

        self.can_talk = False
        blood_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "mermaid_blood.PNG"))
        necklace_image = pygame.image.load(os.path.join(path, "resources/graphics/artifacts", "mermaid_necklace.PNG"))
        self.necklace = Artifact(necklace_image, 10, 'Mermaid Necklace', None)
        self.blood = Artifact(blood_image, 10, 'Mermaid Blood', None)
        self.artifacts.add(self.blood, self.necklace)
        mermaid_attack = pygame.image.load(os.path.join(path, "resources/graphics/particles", "mermaid_attack.PNG"))
        self.npc_attack = AttackClass(mermaid_attack, 20, 10, 'mermaid attack')

    # Method move to stop mermaid from moving (not moving; on the beach)
    def move(self, direction="R", dx=0, dy=0):
        pass

    def move_in_fight(self, hero, all_sprites_group):
        pass

    # make that mermaid can talk only if she has a mermaid necklace in her equipment
    def take_gift(self, hero, artifact, npcs):
        self.artifacts.add(artifact)
        if artifact.name.equals('Mermaid Necklace'):
            self.can_talk = True
        if hero.active_quest is not None \
                and hero.active_quest.active_task is not None \
                and hero.active_quest.active_task.artifact == artifact.name \
                and hero.active_quest.active_task.npc_take_artifact == self.race:
            print(self.race + ": Your quest is completed!")
            hero.active_quest.task_completed(hero, npcs)
        else:
            print(self.race + ": Thank you for your gift")

    # Mermaid can only give quest if she can talk
    def give_quest(self, hero):
        if self.can_talk:
            if hero.active_quest.active_task is None \
                    and hero.active_quest.tasks[0].npc_give_task == self.race:
                hero.active_quest.set_active_task()
            elif hero.active_quest.active_task is not None \
                    and hero.active_quest.active_task.next_npc == self.race:
                hero.active_quest.set_next_active_task()