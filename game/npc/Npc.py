import random
import pygame
from game.hero.Character import Character


# Class with characteristics common to all npcs, from which npc classes inherit
class Npc(Character):
    def __init__(self, name, side, mana, life, images, artifacts, quests):
        super().__init__(name, side, mana, life, images, None)
        self.artifacts = artifacts
        self.is_talking = False
        self.is_fighting = False
        self.quests_to_give = quests
        self.movement = [0, 0, 0]
        self.text = ">> "
        self.image = self.images['down']

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

    def moveByFaerie(self, direction, dx, dy):
        self.direction = direction
        self.rect.x += dx
        self.rect.y += dy

    def thrown(self, side):

        for i in range(1, 30):
            if side == "R" or side == "D":
                self.moveByFaerie("R", 15, -10)
            else:
                self.moveByFaerie("L", -15, -10)
            pygame.display.flip()


        for i in range(1, 100):
            self.moveByFaerie("D", 0, 3)
            pygame.display.flip()


