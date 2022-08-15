import random
import pygame


# Class with characteristics common to all races, from which race classes inherit
class Character(pygame.sprite.Sprite):
    def __init__(self, name, side, mana, life, images, active_quest):
        super().__init__()
        height = SPRITE_SIZE
        width = SPRITE_SIZE
        self.width = width
        self.height = height
        self.images = images
        self.image = self.images['down']
        self.rect = self.image.get_rect()

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
        self.rect.x += dx
        self.rect.y += dy

    # Placeholder. Method to talk? May be useful
    def talk(self):
        print("HELLO")

    # Placeholder. Method to add the found or obtained weapon to the equipment.
    def collect_weapon(self, weapon):
        self.equipment.append(weapon)

    # Placeholder. Method supporting hero fighting - diminishing mana and life.
    def fight(self, screen, option):
        print("This is a fight!!")
