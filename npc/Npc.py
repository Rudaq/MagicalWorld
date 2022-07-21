import random

from hero.Character import Character

SPRITE_SIZE = 50


class Npc(Character):
    def __init__(self, name, side, mana, life, image, image_left, image_right, race, artifacts, quests):
        super().__init__(name, side, mana, life, image, image_left, image_right, race, None)
        self.artifacts = artifacts
        self.is_talking = False
        self.is_fighting = False
        self.quests_to_give = quests
        self.movement = [0, 0, 0]
        self.text = ">> "

    def talk(self):
        print("I'm NPC")

    def move(self, direction="R", dx=0, dy=0):
        step = 2
        if self.movement[0] == 0 and self.movement[2] == 0:
            distance = random.randint(-100, 100)
            axis = random.randint(0, 1)
            wait = random.randint(0, 30)
            self.movement = [distance, axis, wait ]
        else:
            if self.movement[0] > 0:
                self.movement[0] -= 1
                if self.movement[1] == 0:
                    self.rect.x += step
                    self.direction = "R"
                else:
                    self.rect.y += step
                    self.direction = "D"
            elif self.movement[0] < 0:
                self.movement[0] += 1
                if self.movement[1] == 0:
                    self.rect.x -= step
                    self.direction = "L"
                else:
                    self.rect.y -= step
                    self.direction = "U"
            elif self.movement[0] == 0:
                self.movement[2] -= 1

