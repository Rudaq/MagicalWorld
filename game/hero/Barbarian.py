import pygame

from game.Weapon import Weapon
from game.hero.Character import Character

sword = pygame.image.load(r'resources/graphics/weapon/sword.png')


# Class for a hero of race Barbarian, inherits from Character class
class Barbarian(Character):
    def __init__(self, name, side, mana, life, images, active_quest):
        super().__init__(name, side, mana, life, images, active_quest)
        self.race = "Barbarian"
        self.current_attack = None

    def create_attack(self):
        self.current_attack = Weapon(self)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def fight(self, screen, option):
        if option == 1:
            pass
        elif option == 2:
            pass
        else:
            pass

        if self.direction == 'R':
            self.rect = self.image.get_rect(midlef)
