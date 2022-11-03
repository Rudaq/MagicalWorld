import os
from pathlib import Path

from game.artifacts.AttackClass import AttackClass
from game.hero.Character import Character
from game.settings import WIZARD_SPELLS
import pygame
current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent



# Class for a hero of race Wizard, inherits from Character class
class Wizard(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, collision_sprites)
        self.race = "Wizard"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.wind_spell = AttackClass(WIZARD_SPELLS['wind'], 10, 10, 'wind_spell')
        self.magic_ball_spell = AttackClass(WIZARD_SPELLS['magic_ball'], 20, 30, 'magic_ball_spell')
        self.powerful_sparks = AttackClass(WIZARD_SPELLS['sparks'], 35, 20, 'powerful_sparks')
        self.sound3_path = os.path.join(path, "resources/music/fairy_heal.wav")
        self.sound2_path = os.path.join(path, "resources/music/fire-magic.wav")
        self.sound1_path = os.path.join(path, "resources/music/healing_spell.wav")


    def attack(self, screen, npcs):
        if self.in_attack:
            self.attack_type.move_attack()
            if self.attack_type.size < 150:
                if self.attack_type.image == self.attack_type.image_up or self.attack_type.image == self.attack_type.image_down:
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, 50, self.attack_type.size))
                else:
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, self.attack_type.size, 50))
            self.attack_type.check_attack_npc_collision(self, npcs)
        if self.mana - self.attack_type.mana >= 0:
            self.mana -= self.attack_type.mana
            self.in_attack = False

    def fight(self, screen, option, npcs):
        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.wind_spell
                pygame.mixer.Sound.play(self.sound1)
            elif option == 2:
                self.attack_type = self.magic_ball_spell
                pygame.mixer.Sound.play(self.sound2)
            elif option == 3:
                self.attack_type = self.powerful_sparks
                pygame.mixer.Sound.play(self.sound3)

            if self.direction == 'U':
                self.attack_direction = 0
                self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y - 80
                self.attack_type.image = self.attack_type.image_up
            elif self.direction == 'D':
                self.attack_direction = 1
                self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y + 40
                self.attack_type.image = self.attack_type.image_down
            elif self.direction == 'L':
                self.attack_direction = 2
                self.attack_type.rect.x = self.rect.x - 80
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                self.attack_direction = 3
                self.attack_type.rect.x = self.rect.x + 35
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_right

            self.attack_type.size = 50
            self.attack_type.acceleration = 0.1
            self.attack_type.start_x = self.attack_type.rect.x
            self.attack_type.start_y = self.attack_type.rect.y

        self.attack(screen, npcs)

    # Placeholder. Method to add the found or obtained weapon to the equipment.
    def collect_artifact(self, artifact, npcs):
        if len(self.equipment) == 6:
            print("You can't collect more equipment! Your backpack is full!")
            return False
        else:
            if artifact.small_image is not None:
                artifact.image = artifact.small_image
                artifact.small_image = None

            self.equipment.append(artifact)
            self.points += artifact.points

            if self.active_quest.active_task is not None \
                    and self.active_quest.active_task.npc_take_artifact is None \
                    and self.active_quest.active_task.artifact.name == artifact:

                self.active_quest.task_completed(self, npcs)

            return True
