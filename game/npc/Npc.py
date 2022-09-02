import random
import pygame
from hero.Character import Character


# Class with characteristics common to all npcs, from which npc classes inherit
class Npc(Character):
    def __init__(self, name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites):
        super().__init__(name, side, mana, life, images, None, pos, groups, inflation, collision_sprites)
        self.artifacts = pygame.sprite.Group()
        self.is_talking = False
        # self.is_fighting = False
        self.quests_to_give = quests
        self.movement = [0, 0, 0]
        self.text = ">> "
        self.image = self.images['down']
        self.collision_sprites = collision_sprites
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(self.inflation[0], self.inflation[1])
        self.add_npc_to_hud = False
        self.can_talk = None

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

    def kill_npc(self, all_artifacts, screen):
        self.add_npc_to_hud = False
        x = self.rect.x - 100
        y = self.rect.y
        for artifact in self.artifacts:
            x += 50
            artifact.show(x, y, all_artifacts, screen)

    # One common function for throwing out particles for all NPC's
    def fight_npc(self, screen, hero):
        counter = random.randint(1, 25)
        if counter == 4:
            if self.attack_type == None:
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

            self.attack(screen, hero, counter)

    def attack(self, screen, hero, counter):
        if counter == 4 and self.life > 0:
            self.attack_type.move_attack()
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
            self.attack_type.check_attack_hero_collision(self, hero)

        else:
            if self.life > 0:
                counter == 4

    # function for NPC' movement while fighting
    def move_in_fight(self, hero):
        step = random.randint(1, 4)
        if hero.direction == "L":
            if hero.mana > 0:
                self.rect.x += step
                self.direction = "R"
            else:
                step *= 2
                self.rect.x -= step
                self.direction = "L"
        elif hero.direction == "U":
            if hero.mana > 0:
                self.rect.y += step
                self.direction = "D"
            else:
                step *= 2
                self.rect.y -= step
                self.direction = "U"
        elif hero.direction == "R":
            if hero.mana > 0:
                self.direction = "L"
                self.rect.x -= step
            else:
                step *= 2
                self.direction = "R"
                self.rect.x += step
        else:
            if hero.mana > 0:
                self.direction = "U"
                self.rect.y -= step
            else:
                step *= 2
                self.direction = "D"
                self.rect.y += step
