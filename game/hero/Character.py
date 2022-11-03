import pygame
from artifacts.Artifact import Artifact

SPRITE_SIZE = 50
import os
from pathlib import Path

current = os.path.dirname(os.path.realpath(__file__))
path = Path(__file__).resolve().parent.parent.parent

'''
For testing collisions uncomment these lines:
collision_block = pygame.image.load("../resources/graphics/tilemap/npc_blocker.png")
regular_block = pygame.image.load("../resources/graphics/tilemap/player_blocker.png")
'''


# Class with characteristics common to all races, from which race classes inherit
class Character(pygame.sprite.Sprite):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, collision_sprites):
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
        # self.speed = 5

        self.name = name
        self.side = side
        self.mana = mana
        self.life = life
        self.equipment = []
        self.points = 0

        self.direction = "U"
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
        self.attack_direction = 0

        self.start_centerx = 0
        self.start_centery = 0
        self.set_start_centerx = True
        self.set_start_centery = True

        self.sprite_type = 'hero'
        self.artifacts = pygame.sprite.Group()

        self.sprite_colliding = []
        self.directions_of_collisions = []
        self.collisions_right = []
        self.collisions_left = []
        self.collisions_up = []
        self.collisions_down = []

        self.quests = []
        self.active_quest = None
        self.skipped_quests = []

        self.restore_new_task = None
        self.new_task = None

    # method to return active quest
    def set_active_quest(self):
        if len(self.quests) > 0:
            self.active_quest = self.quests[0]
            self.active_quest.active_task = None

        else:
            print("Your mission is completed! Congratulations!")
            self.active_quest = None

    def take_next_quest(self):
        self.points += self.active_quest.points
        self.quests.remove(self.active_quest)
        self.set_active_quest()

    # Method to move - changes direction, adds or subtracts value on the x or y coordinates
    def move(self, direction, dir_opposite, mov_x, mov_y, sign, all_sprites_group, sprites_to_move_opposite):
        is_collision, all_sprites_group = self.collision(all_sprites_group)

        if self.direction == 'R':
            self.image = self.images['right']
        elif self.direction == 'L':
            self.image = self.images['left']
        elif self.direction == 'U':
            self.image = self.images['up']
        else:
            self.image = self.images['down']


        if not is_collision:
            if direction == 'horizontal':
                all_sprites_group.offset.x += mov_x * sign
            elif direction == 'vertical':
                all_sprites_group.offset.y += mov_y * sign

            for sprite in sprites_to_move_opposite:
                if direction == 'horizontal':
                    sprite.rect.centerx += mov_x * sign * (-1)
                elif direction == 'vertical':
                    sprite.rect.centery += mov_y * sign * (-1)
                sprite.direction = dir_opposite

    def collision(self, all_sprites_group):
        is_collision = False
        collision_occurred = False

        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                '''
                For testing collisions uncomment these lines:
                print(" Direction of collision: ", self.directions_of_collisions)
                sprite.image = collision_block
                '''

                collision_occurred = True

                if sprite not in self.sprite_colliding:
                    # if the list is not empty (already has collision with some rect)
                    if len(self.sprite_colliding) > 0:
                        self.sprite_colliding.append(sprite)

                        # case when: first collision is with x and then hero changes his y position,
                        # so he has a long block of collision on the one side
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

                        # case when the rectangles are in diagonal collision (e.g. trees)
                        else:
                            self.directions_of_collisions.append(self.direction)
                            if self.direction == 'D':
                                self.collisions_down.append(sprite)
                            elif self.direction == 'U':
                                self.collisions_up.append(sprite)
                            elif self.direction == 'R':
                                self.collisions_right.append(sprite)
                            else:
                                self.collisions_left.append(sprite)

                    # if this is the first collision
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
                '''
                For testing collisions uncomment this line:
                sprite.image = regular_block
                '''
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

    # One common function for throwing out particles for all heroes
    def attack(self, screen, npcs):
        if self.performing_action:
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
            # check if npc had collision with attack

            self.attack_type.check_attack_npc_collision(self, npcs)

        else:
            if self.mana - self.attack_type.mana >= 0:
                self.mana -= self.attack_type.mana
                self.performing_action = True

    # function for throwing a weapon for Barbarian, Elf and Dwarf
    def use_weapon(self, screen, npcs):
        if self.performing_action:
            # self.chosen_spell.size = 5
            self.attack_type.move_attack()
            draw = False
            if self.attack_type.image == self.attack_type.image_up:
                self.attack_type.rect.y -= self.attack_type.size
                if self.attack_type.rect.bottom > self.attack_type.start_y - 150:
                    draw = True
            elif self.attack_type.image == self.attack_type.image_down:
                self.attack_type.rect.y += self.attack_type.size
                if self.attack_type.rect.top < self.attack_type.start_y + 150:
                    draw = True
            elif self.attack_type.image == self.attack_type.image_left:
                self.attack_type.rect.x -= self.attack_type.size
                if self.attack_type.rect.right > self.attack_type.start_x - 150:
                    draw = True
            else:
                self.attack_type.rect.x += self.attack_type.size
                if self.attack_type.rect.left < self.attack_type.start_x + 150:
                    draw = True

            if draw:
                screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y))
            self.attack_type.check_attack_npc_collision(self, npcs)

        else:
            if self.mana - self.attack_type.mana >= 0:
                self.mana -= self.attack_type.mana
                self.attack_type.size = 5
                self.performing_action = True

    # Placeholder. Method to talk? May be useful
    def talk(self):
        print("HELLO")

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
            return True

    def collect_map_artifact(self, map_artifact, equipment_buttons):
        if len(self.equipment) == 6:
            print("You can't collect more equipment! Your backpack is full!")
            return False
        else:
            if map_artifact.small_image is not None:
                artifact = Artifact(map_artifact.small_image, map_artifact.points, map_artifact.name, None)
                self.equipment.append(artifact)
                self.points += artifact.points
                return True
            else:
                return False

    def take_gift_from_npc(self, npc, npcs, gift):
        for n in npcs:
            if n.race == npc:
                for g in n.gifts:
                    if g.name == gift:
                        n.gifts.remove(g)
                        self.collect_artifact(g, npcs)
                break

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
