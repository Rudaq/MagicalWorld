import random
import pygame

SPRITE_SIZE = 50


# Class with characteristics common to all races, from which race classes inherit
class Character(pygame.sprite.Sprite):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites):
        super().__init__()
        height = SPRITE_SIZE
        width = SPRITE_SIZE
        self.width = width
        self.height = height
        self.images = images
        self.image = self.images['down']
        self.rect = self.image.get_rect(topleft=pos)

        self.collision_sprites = collision_sprites
        self.groups = groups
        self.inflation = inflation
        self.hitbox = self.rect.inflate(self.inflation[0], self.inflation[1])
        self.speed = 5

        self.name = name
        self.side = side
        self.mana = mana
        self.life = life
        self.equipment = []
        self.points = 0

        self.direction = "U"

        self.active_quest = active_quest
        self.my_text = ''
        self.text_history = []
        self.last_position = 175

        # dialog variables
        self.hero_turn = False
        self.in_dialog = False
        self.in_fight_mode = False
        self.in_attack = False
        self.performing_action = False

        self.attack_type = None

    # Method to move - changes direction, adds or subtracts value on the x or y coordinates
    def move(self, direction, dx, dy):
        self.direction = direction

        self.hitbox.x += dx * 2
        self.collision('horizontal')
        self.hitbox.y += dy * 2
        self.collision('vertical')

        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.collision_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction == 'R':  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction == 'L':  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.collision_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction == 'D':  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction == 'U':  # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    # One common function for throwing out particles for all heroes

    # One common function for throwing out particles for all heroes
    # stara wersja
    #     def attack(self, screen, npcs):
    #         if self.performing_action:
    #             self.attack_type.move_attack()
    #             if self.attack_type.size < 150:
    #                 if self.attack_type.image == self.attack_type.image_up or self.attack_type.image == self.attack_type.image_down:
    #                     screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
    #                                 (0, 0, 50, self.attack_type.size))
    #                 else:
    #                     screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
    #                                 (0, 0, self.attack_type.size, 50))
    #             # check if npc was affected by the attack
    #             self.attack_type.check_attack_npc_collision(self, npcs)
    #
    #         else:
    #             if self.mana - self.attack_type.mana >= 0:
    #                 self.mana -= self.attack_type.mana
    #                 self.performing_action = True

    # nowa moja wersja
    # def attack(self, screen, npcs):
    #     if self.performing_action:
    #         # move attack to the NPC
    #         self.attack_type.move_attack()
    #         if self.attack_type.size < 150:
    #
    #             # move attack down
    #             if self.attack_type.image == self.attack_type.image_down:
    #                 self.attack_type.rect.topleft = [self.attack_type.start_x,
    #                                                  self.attack_type.start_y + self.attack_type.size]
    #                 screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
    #                             (0, 0, 50, self.attack_type.size))
    #
    #             # move attack up
    #             elif self.attack_type.image == self.attack_type.image_up:
    #                 self.attack_type.rect.topleft = [self.attack_type.start_x,
    #                                                  self.attack_type.start_y - self.attack_type.size]
    #                 screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
    #                             (0, 0, 50, self.attack_type.size))
    #
    #             # move attack to the left
    #             elif self.attack_type.image == self.attack_type.image_left:
    #                 self.attack_type.rect.topleft = [self.attack_type.start_x - self.attack_type.size,
    #                                                  self.attack_type.start_y]
    #                 screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
    #                             (0, 0, 50, self.attack_type.size))
    #
    #             # move attack to the right
    #             else:
    #                 self.attack_type.rect.topleft = [self.attack_type.start_x + self.attack_type.size,
    #                                                  self.attack_type.start_y]
    #                 screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
    #                             (0, 0, self.attack_type.size, 50))
    #
    #         # check if npc was affected by the attack
    #         self.attack_type.check_attack_npc_collision(self, npcs)
    #
    #     else:
    #         if self.mana - self.attack_type.mana >= 0:
    #             self.mana -= self.attack_type.mana
    #             self.performing_action = True

    def attack(self, screen, npcs):
        if self.performing_action:
            self.attack_type.move_attack()
            if self.attack_type.size < 200:
                if self.attack_type.image == self.attack_type.image_down:
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, 50, self.attack_type.size))
                    self.attack_type.rect.bottomleft = [self.attack_type.start_x,
                                                     self.attack_type.start_y + self.attack_type.size]
                elif self.attack_type.image == self.attack_type.image_up:
                    self.attack_type.rect.topleft = [self.attack_type.start_x,
                                                       self.attack_type.start_y - self.attack_type.size]
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, 50, self.attack_type.size))
                elif self.attack_type.image == self.attack_type.image_left:
                    self.attack_type.rect.topleft = [self.attack_type.start_x - self.attack_type.size,
                                                       self.attack_type.start_y]
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, self.attack_type.size, 50))
                else:
                    self.attack_type.rect.topright = [self.attack_type.start_x + self.attack_type.size,
                                                     self.attack_type.start_y]
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, self.attack_type.size, 50))
            self.attack_type.check_attack_npc_collision(self, npcs)

        else:
            if self.mana - self.attack_type.mana >= 0:
                self.mana -= self.attack_type.mana
                self.performing_action = True

    # Placeholder. Method to talk? May be useful
    def talk(self):
        print("HELLO")

    # Placeholder. Method to add the found or obtained weapon to the equipment.
    def collect_artifact(self, artifact):
        if len(self.equipment) == 5:
            print("You can't collect more equipment! Your backpack is full!")
        else:
            self.equipment.append(artifact)
            self.points += artifact.points

    # Placeholder. Method supporting hero fighting - diminishing mana and life.
    def fight(self, screen, option, npcs):
        print("This is a fight!!")

    def add_life(self, value):
        if self.life < 100:
            if self.life + value > 100:
                self.life = 100
            else:
                self.life += value

    def add_mana(self, value):
        if self.mana <= 100 - value:
            self.mana += value
