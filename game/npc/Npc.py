import os
import random
from pathlib import Path

import pandas as pd
import pygame
from hero.Character import Character

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent

# Class with characteristics common to all npcs, from which npc classes inherit
class Npc(Character):
    def __init__(self, name, side, mana, life, images, artifacts, quests, pos, groups, collision_sprites):
        super().__init__(name, side, mana, life, images, None, pos, groups, collision_sprites)
        self.sprite_type = 'npc'
        self.race = 'npc'
        self.movement = [0, 0, 0]
        self.text = '>> '
        self.image = self.images['down']
        self.collision_sprites = collision_sprites
        self.rect = self.image.get_rect(topleft=pos)
        # self.hitbox = self.rect.inflate(self.inflation[0], self.inflation[1])
        self.is_talking = False
        self.add_npc_to_hud = False
        self.can_talk = None
        self.groups = groups
        self.collision_sprites = collision_sprites
        self.collision_sprites_npc = None
        self.quests_to_give = quests
        self.gifts = pygame.sprite.Group()
        self.artifacts = pygame.sprite.Group()
        self.context = ''
        self.nice_greetings = []
        self.rude_greetings = []
        self.load_greetings()

        self.sound_path = os.path.join(path, "resources/music/npc_attack.wav")

    # # Placeholder. Method to talk? May be useful
    # def talk(self):
    #     print("I'm NPC")

    # Method for randomly moving the npc
    def move(self, all_sprites_group):
        is_collision, all_sprites_group = self.collision(all_sprites_group)

        step = 1
        #
        # # Randomly selecting length of the movement (self.movement[0]), the axis of movement (self.movement[1),
        # # and time to wait between next movements (self.movement[2])
        if self.movement[0] == 0 and self.movement[2] == 0:
            distance = random.randint(-100, 100)
            axis = random.randint(0, 1)
            wait = random.randint(0, 30)
            self.movement = [distance, axis, wait]

        # Increasing/Decreasing the value of x or y coordinates,
        # depending on the chosen axis of movement (up-down, left-right)
        if self.movement[0] > 0:
            self.movement[0] -= 1
            # Moving right
            if self.movement[1] == 0:
                if 'R' not in self.directions_of_collisions:
                    self.rect.x += step
                else:
                    self.movement[0] = 0
                self.direction = 'R'
                self.image = self.images['right']
            # Moving down
            else:
                if 'D' not in self.directions_of_collisions:
                    self.rect.y += step
                else:
                    self.movement[0] = 0
                self.direction = 'D'
                self.image = self.images['down']

        elif self.movement[0] < 0:
            self.movement[0] += 1
            # Moving left
            if self.movement[1] == 0:
                if 'L' not in self.directions_of_collisions:
                    self.rect.x -= step
                else:
                    self.movement[0] = 0
                self.direction = 'L'
                self.image = self.images['left']
            # Moving right
            else:
                if 'U' not in self.directions_of_collisions:
                    self.rect.y -= step
                else:
                    self.movement[0] = 0
                self.direction = 'U'
                self.image = self.images['up']
        # Waiting by a number of randomly selected iteration, before another random call
        elif self.movement[0] == 0:
            self.movement[2] -= 1

        if self.direction == 'R':
            self.image = self.images['right']
        elif self.direction == 'L':
            self.image = self.images['left']
        elif self.direction == 'U':
            self.image = self.images['up']
        else:
            self.image = self.images['down']

    def kill_npc(self, all_artifacts, screen):
        self.add_npc_to_hud = False
        x = self.rect.x - 100
        y = self.rect.y
        for artifact in self.artifacts:
            x += 50
            artifact.show(x, y, all_artifacts, screen)

    # One common function for throwing out particles for all NPC's
    def fight_npc(self, screen, hero, npcs):

        counter = random.randint(1, 50)
        if counter == 4 and self.npc_attack is not None:
            if self.attack_type is None:
                self.attack_type = self.npc_attack

                if hero.direction == 'D':
                    self.attack_type.rect.x = self.rect.x
                    self.attack_type.rect.y = self.rect.y - 30
                    self.attack_type.image = self.attack_type.image_up
                elif hero.direction == 'U':
                    self.attack_type.rect.x = self.rect.x
                    self.attack_type.rect.y = self.rect.y + 30
                    self.attack_type.image = self.attack_type.image_down
                elif hero.direction == 'R':
                    self.attack_type.rect.x = self.rect.x - 30
                    self.attack_type.rect.y = self.rect.y
                    self.attack_type.image = self.attack_type.image_left
                else:
                    self.attack_type.rect.x = self.rect.x + 30
                    self.attack_type.rect.y = self.rect.y
                    self.attack_type.image = self.attack_type.image_right
                self.attack_type.size = 50
                self.attack_type.acceleration = 0.1
                self.attack_type.start_x = self.attack_type.rect.x
                self.attack_type.start_y = self.attack_type.rect.y

            self.attack(screen, hero, counter, npcs)

    def attack(self, screen, hero, counter, npcs):
        if counter == 4 and self.life > 0:
            self.attack_type.move_attack()
            pygame.mixer.Sound.play(self.sound1)
            self.sound1.set_volume(1)

            if self.attack_type.size < 200:
                # move particles to the down
                if self.attack_type.image == self.attack_type.image_down:
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, 50, self.attack_type.size))
                    self.attack_type.rect.bottomleft = [self.attack_type.start_x,
                                                        self.attack_type.start_y + self.attack_type.size]
                # move particles to the up
                elif self.attack_type.image == self.attack_type.image_up:
                    self.attack_type.rect.topleft = [self.attack_type.start_x,
                                                     self.attack_type.start_y - self.attack_type.size]
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, 50, self.attack_type.size))

                # move particles to the left
                elif self.attack_type.image == self.attack_type.image_left:
                    self.attack_type.rect.topleft = [self.attack_type.start_x - self.attack_type.size,
                                                     self.attack_type.start_y]
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, self.attack_type.size, 50))

                # move particles to the right
                else:
                    self.attack_type.rect.topright = [self.attack_type.start_x + self.attack_type.size,
                                                      self.attack_type.start_y]
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, self.attack_type.size, 50))

            # check if hero had collision with attack
            self.attack_type.check_attack_hero_collision(self, hero, npcs)

        else:
            # ?
            if self.life > 0:
                counter = 4

    # function for NPC' movement while fighting
    def move_in_fight(self, hero, all_sprites_group):
        step = random.randint(1, 4)
        is_collision, all_sprites_group = self.collision(all_sprites_group)

        if not is_collision:
            if hero.direction == 'L':
                if hero.mana > 0:
                    self.rect.x += step
                    self.direction = 'R'
                    self.image = self.images['right']
                else:
                    step *= 2
                    self.rect.x -= step
                    self.direction = 'L'
                    self.image = self.images['left']
            elif hero.direction == 'U':
                if hero.mana > 0:
                    self.rect.y += step
                    self.direction = 'D'
                    self.image = self.images['down']
                else:
                    step *= 2
                    self.rect.y -= step
                    self.direction = 'U'
                    self.image = self.images['up']
            elif hero.direction == 'R':
                if hero.mana > 0:
                    self.direction = 'L'
                    self.rect.x -= step
                    self.image = self.images['left']
                else:
                    step *= 2
                    self.direction = 'R'
                    self.rect.x += step
                    self.image = self.images['right']
            else:
                if hero.mana > 0:
                    self.direction = 'U'
                    self.rect.y -= step
                    self.image = self.images['up']
                else:
                    step *= 2
                    self.direction = 'D'
                    self.rect.y += step
                    self.image = self.images['down']

    # def run(self, hero, all_sprites_group):
    #     step = random.randint(1, 4)
    #     is_collision, all_sprites_group = self.collision(self, all_sprites_group)
    #
    #     if not is_collision:
    #         if hero.direction == 'L':
    #             if hero.mana > 0:
    #                 self.rect.x += step
    #                 self.direction = 'R'
    #             else:
    #                 step *= 2
    #                 self.rect.x -= step
    #                 self.direction = 'L'
    #         elif hero.direction == 'U':
    #             if hero.mana > 0:
    #                 self.rect.y += step
    #                 self.direction = 'D'
    #             else:
    #                 step *= 2
    #                 self.rect.y -= step
    #                 self.direction = 'U'
    #         elif hero.direction == 'R':
    #             if hero.mana > 0:
    #                 self.direction = 'L'
    #                 self.rect.x -= step
    #             else:
    #                 step *= 2
    #                 self.direction = 'R'
    #                 self.rect.x += step
    #         else:
    #             if hero.mana > 0:
    #                 self.direction = 'U'
    #                 self.rect.y -= step
    #             else:
    #                 step *= 2
    #                 self.direction = 'D'
    #                 self.rect.y += step

    def take_gift(self, hero, artifact, npcs, screen):
        self.gifts.add(artifact)
        if hero.active_quest is not None \
                and hero.active_quest.active_task is not None \
                and hero.active_quest.active_task.artifact == artifact.name \
                and hero.active_quest.active_task.npc_take_artifact == self.race:
            print(self.race + ": Your task is completed!")
            if hero.active_quest.task_completed(hero, npcs):
                return True

        elif len(hero.active_quest.skipped_tasks) > 0:
            for task in hero.active_quest.skipped_tasks:
                if task.artifact == artifact.name \
                        and task.npc_take_artifact == self.race:
                    print(self.race + ": Thank you for your gift")
        return False

    def give_quest(self, hero):
        if hero.active_quest.active_task is None \
                and hero.active_quest.tasks[0].npc_give_task == self.race:
            hero.active_quest.is_started = True
            hero.active_quest.set_active_task()
            return True
        elif hero.active_quest.active_task is not None \
                and hero.active_quest.active_task.next_npc == self.race:
            hero.active_quest.is_started = True
            hero.active_quest.set_next_active_task()
            return True  # idk
        return False

    # def collision(self, all_sprites_group):
    #     # print("No of collision sprites in  NPC: ", len(self.collision_sprites))
    #     for sprite in self.collision_sprites:
    #         if sprite.rect.colliderect(self.rect):
    #             return True

    def collision(self, all_sprites_group):
        is_collision = False
        collision_occurred = False

        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                collision_occurred = True

                if sprite not in self.sprite_colliding:

                    if len(self.sprite_colliding) > 0:
                        self.sprite_colliding.append(sprite)
                        if self.sprite_colliding[-2].rect.y != sprite.rect.y and self.sprite_colliding[
                            -2].rect.x == sprite.rect.x:
                            if self.rect.left > sprite.rect.left:
                                self.collisions_left.append(sprite)
                                self.directions_of_collisions.append('L')
                            elif self.rect.left < sprite.rect.left:
                                self.collisions_right.append(sprite)
                                self.directions_of_collisions.append('R')

                        elif self.sprite_colliding[-2].rect.x != sprite.rect.x and self.sprite_colliding[
                            -2].rect.y == sprite.rect.y:
                            if self.rect.top > sprite.rect.top:
                                self.collisions_up.append(sprite)
                                self.directions_of_collisions.append('U')
                            elif self.rect.top < sprite.rect.top:
                                self.collisions_down.append(sprite)
                                self.directions_of_collisions.append('D')
                    else:
                        self.sprite_colliding.append(sprite)
                        self.directions_of_collisions.append(self.direction)
                        if self.direction == 'L':
                            self.collisions_left.append(sprite)
                        elif self.direction == 'R':
                            self.collisions_right.append(sprite)
                        elif self.direction == 'U':
                            self.collisions_up.append(sprite)
                        elif self.direction == 'D':
                            self.collisions_down.append(sprite)

                if self.direction in self.directions_of_collisions:
                    if self.direction == 'D' or self.direction == 'U':
                        all_sprites_group.offset.y -= 0
                    else:
                        all_sprites_group.offset.x -= 0
                    is_collision = True
            else:
                if sprite in self.sprite_colliding:
                    if sprite in self.collisions_left:
                        self.collisions_left.remove(sprite)
                        self.directions_of_collisions.remove('L')
                    elif sprite in self.collisions_right:
                        self.collisions_right.remove(sprite)
                        self.directions_of_collisions.remove('R')
                    elif sprite in self.collisions_up:
                        self.collisions_up.remove(sprite)
                        self.directions_of_collisions.remove('U')
                    elif sprite in self.collisions_down:
                        self.collisions_down.remove(sprite)
                        self.directions_of_collisions.remove('D')
                    self.sprite_colliding.remove(sprite)

        self.had_collision = collision_occurred
        if not collision_occurred:
            self.sprite_colliding = []
            self.directions_of_collisions = []

        return is_collision, all_sprites_group


    def load_greetings(self):
        dataset_path = os.path.join(path, "NLP/sentiment_analysis/Greetings.csv")


        dataset = pd.read_csv(
                dataset_path,
                names=["greetings", "sentiment"], encoding="utf-8", header=None, sep='\t')

        for key, text in dataset.iterrows():
            if text["sentiment"] == 1:
                self.nice_greetings.append(str(text["greetings"]))
            else:
                self.rude_greetings.append(str(text["greetings"]))
