import random

import pandas as pd
import pygame
from hero.Character import Character


# Class with characteristics common to all npcs, from which npc classes inherit
class Npc(Character):
    def __init__(self, name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites):
        super().__init__(name, side, mana, life, images, None, pos, groups, inflation, collision_sprites)
        self.artifacts = pygame.sprite.Group()
        self.is_talking = False
        self.is_fighting = False
        self.quests_to_give = quests
        self.movement = [0, 0, 0]
        self.text = ">> "
        self.image = self.images['down']
        self.collision_sprites = collision_sprites
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(self.inflation[0], self.inflation[1])
        self.add_npc_to_hud = False
        self.can_talk = None
        self.nice_greetings = []
        self.rude_greetings = []
        self.load_greetings()

    # Placeholder. Method to talk? May be useful
    def talk(self):
        print("I'm NPC")

    # Method for randomly moving the npc
    def move(self, direction="R", dx=0, dy=0):
        step = 2

        # Randomly selecting length of the movement (self.movement[0]), the axis of movement (self.movement[1),
        # and time to wait between next movements (self.movement[2])
        if self.movement[0] == 0 and self.movement[2] == 0:
            distance = random.randint(-100, 100)
            axis = random.randint(0, 1)
            wait = random.randint(0, 30)
            self.movement = [distance, axis, wait]

        # Increasing/Decreasing the value of x or y coordinates,
        # depending on the chosen axis of movement (up-down, left-right)
        else:
            if self.movement[0] > 0:
                self.movement[0] -= 1
                # Moving right
                if self.movement[1] == 0:
                    self.rect.x += step
                    self.direction = "R"
                # Moving down
                else:
                    self.rect.y += step
                    self.direction = "D"
            elif self.movement[0] < 0:
                self.movement[0] += 1
                # Moving left
                if self.movement[1] == 0:
                    self.rect.x -= step
                    self.direction = "L"
                # Moving right
                else:
                    self.rect.y -= step
                    self.direction = "U"
            # Waiting by a number of randomly selected iteration, before another random call
            elif self.movement[0] == 0:
                self.movement[2] -= 1

    # move npc to a given place
    def moveByFaerie(self, direction, dx, dy):
        self.direction = direction
        self.rect.x += dx
        self.rect.y += dy

    def throw(self, side, screen):
        for i in range(1, 8):
            if side == "R" or side == "D":
                self.moveByFaerie("R", 50, -20)
            else:
                self.moveByFaerie("L", -50, -20)
            screen.blit()
            pygame.display.flip()

        for i in range(1, 16):
            self.moveByFaerie("D", 0, 10)
            screen.blit()
            pygame.display.flip()

    def kill_npc(self, all_artifacts, screen):
        self.add_npc_to_hud = False
        x = self.rect.x - 100
        y = self.rect.y
        self.kill()
        for artifact in self.artifacts:
            x += 50
            artifact.show(x, y, all_artifacts, screen)
        print("dead")

    def load_greetings(self):
        dataset = pd.read_csv(
                "C:\\Inżynierka\\MagicalWorld\\NLP\\sentiment_analysis\\Greetings.csv",
                names=["greetings", "sentiment"], encoding="utf-8", header=None, sep='\t')

        for key, text in dataset.iterrows():
            if text["sentiment"] == '1':
                self.nice_greetings.append(str(text["greetings"]))
            else:
                self.rude_greetings.append(str(text["greetings"]))
