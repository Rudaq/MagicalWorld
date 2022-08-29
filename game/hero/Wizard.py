from artifacts.AttackClass import AttackClass
from hero.Character import Character
from settings import WIZARD_SPELLS


# Class for a hero of race Wizard, inherits from Character class
class Wizard(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Wizard"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.wind_spell = AttackClass(WIZARD_SPELLS['wind'], 10, 10, 'wind_spell')
        self.healing_spell = AttackClass(WIZARD_SPELLS['healing'], 0, 25, 'healing_spell')
        self.magic_ball_spell = AttackClass(WIZARD_SPELLS['magic_ball'], 20, 30, 'magic_ball_spell')
        self.powerful_sparks = AttackClass(WIZARD_SPELLS['sparks'], 35, 20, 'powerful_sparks')

    def perform_action(self, screen):
        if self.in_attack:
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

        else:
            if self.mana - self.attack_type.mana >= 0:
                self.mana -= self.attack_type.mana
                self.attack_type.size = 5
                self.in_attack = True
                self.attack_direction = self.direction

    def fight(self, screen, option, npcs):

        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.wind_spell

            elif option == 2:
                self.attack_type = self.healing_spell

            elif option == 3:
                self.attack_type = self.powerful_sparks

            else:
                self.attack_type = self.magic_ball_spell


            if self.direction == 'U':
                self.attack_direction = 0
                self.attack_type.rect.x = self.rect.x
                if not option > 4:
                    self.attack_type.rect.y = self.rect.y - 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_up
            elif self.direction == 'D':
                self.attack_direction = 1
                self.attack_type.rect.x = self.rect.x
                if not option > 4:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_down
            elif self.direction == 'L':
                self.attack_direction = 2
                if not option > 4:
                    self.attack_type.rect.x = self.rect.x - 30
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                self.attack_direction = 3

                if not option > 4:
                    self.attack_type.rect.x = self.rect.x + 30
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_right

            self.attack_type.size = 50
            self.attack_type.acceleration = 0.1
            self.attack_type.start_x = self.attack_type.rect.x
            self.attack_type.start_y = self.attack_type.rect.y

        if option == 1 or option == 2:
            self.attack(screen, npcs)
        else:
            self.perform_action(screen)
