import pygame
from artifacts.AttackClass import AttackClass
from hero.Character import Character
from settings import BARBARIAN_ACTIONS, HERO_ANIMATIONS


# Class for a hero of race Barbarian, inherits from Character class
class Barbarian(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Barbarian"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.sword_attack = AttackClass(BARBARIAN_ACTIONS['sword'], 50, 10, 'sword_attack')
        self.fury = AttackClass(BARBARIAN_ACTIONS['fury'], 15, 5, 'fury_attack')
        self.resistance = AttackClass(BARBARIAN_ACTIONS['resistance'], 0, 10, 'resistance_to_damage')

    def resistant_to_damage(self, screen):
        half_live = self.life / 2
        self.add_life(half_live)
        screen.blit(self.attack_type.image_right, (self.attack_type.rect.x, self.attack_type.rect.y))

    def fight(self, screen, option, npcs):
        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.sword_attack
            elif option == 2:
                self.attack_type = self.fury
            else:
                self.attack_type = self.resistance

            if self.direction == 'U':
                self.attack_type.rect.x = self.rect.x
                if option == 2:
                    self.attack_type.rect.y = self.rect.y + 10
                    for i in range(4):
                        screen.blit(BARBARIAN_ACTIONS['fury_flames'][i], (self.rect.x, self.rect.y))
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_up

            elif self.direction == 'D':
                self.attack_type.rect.x = self.rect.x
                if option == 2:
                    self.attack_type.rect.y = self.rect.y + 10
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_down
            elif self.direction == 'L':
                if option == 2:
                    self.attack_type.rect.x = self.rect.x + 10
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                if option == 2:
                    self.attack_type.rect.x = self.rect.x + 15
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_right

            if option == 3:
                self.resistant_to_damage(screen)

            self.attack_type.size = 50
            self.attack_type.acceleration = 0.1
            self.attack_type.start_x = self.attack_type.rect.x
            self.attack_type.start_y = self.attack_type.rect.y

        if option == 1:
            self.use_weapon(screen, npcs)

        elif option == 2:
            self.attack(screen, npcs)



    def collect_artifact(self, artifact):
        if len(self.equipment) == 6:
            print("You can't collect more equipment! Your backpack is full!")
            return False
        else:
            if artifact.small_image is not None:
                artifact.image = artifact.small_image
                artifact.small_image = None
            self.equipment.append(artifact)
            self.points += artifact.points
            if artifact.name == 'New Sword':
                self.sword_attack = AttackClass(artifact.image, 25, 10, 'sword_attack')
            return True




