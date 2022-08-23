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
        self.in_fight = False
        self.casting_spell = False

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

    # Placeholder. Method to talk? May be useful
    def talk(self):
        print("HELLO")

    # Placeholder. Method to add the found or obtained weapon to the equipment.
    def collect_weapon(self, weapon):
        self.equipment.append(weapon)

    # Placeholder. Method supporting hero fighting - diminishing mana and life.
    def fight(self, screen, option, npcs):
        print("This is a fight!!")