from game.artifacts.AttackClass import AttackClass
from game.hero.Character import Character
from game.settings import WIZARD_SPELLS


# Class for a hero of race Wizard, inherits from Character class
class Wizard(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Wizard"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.wind_spell = AttackClass(WIZARD_SPELLS['wind'], 10, 'wind_spell')
        self.heal_spell = AttackClass(WIZARD_SPELLS['healing'], 0, 'heal_spell')
        self.magic_ball_spell = AttackClass(WIZARD_SPELLS['magic_ball'], 20, 'magic_ball_spell')
        self.powerful_sparks = AttackClass(WIZARD_SPELLS['sparks'], 35, 'powerful_sparks')

    def perform_action(self, screen, mana):
        if self.performing_action:
            # self.chosen_spell.size = 5
            self.chosen_attack.move_attack()
            draw = False
            if self.chosen_attack.image == self.chosen_attack.image_up:
                self.chosen_attack.rect.y -= self.chosen_attack.size
                if self.chosen_attack.rect.bottom > self.chosen_attack.start_y - 150:
                    draw = True
            elif self.chosen_attack.image == self.chosen_attack.image_down:
                self.chosen_attack.rect.y += self.chosen_attack.size
                if self.chosen_attack.rect.top < self.chosen_attack.start_y + 150:
                    draw = True
            elif self.chosen_attack.image == self.chosen_attack.image_left:
                self.chosen_attack.rect.x -= self.chosen_attack.size
                if self.chosen_attack.rect.right > self.chosen_attack.start_x - 150:
                    draw = True
            else:
                self.chosen_attack.rect.x += self.chosen_attack.size
                if self.chosen_attack.rect.left < self.chosen_attack.start_x + 150:
                    draw = True

            if draw:
                screen.blit(self.chosen_attack.image, (self.chosen_attack.rect.x, self.chosen_attack.rect.y))

        else:
            if self.mana - mana >= 0:
                self.mana -= mana
                self.chosen_attack.size = 5
                self.performing_action = True
                self.attack_direction = self.direction

    def fight(self, screen, option, npcs):
        mana = 0

        if self.chosen_attack is None:
            if option == 1:
                self.chosen_attack = self.wind_spell
                mana = 10
            elif option == 2:
                self.chosen_attack = self.heal_spell
                mana = 25
            elif option == 3:
                self.chosen_attack = self.powerful_sparks
                mana = 30
            else:
                self.chosen_attack = self.magic_ball_spell
                mana = 20

            if self.direction == 'U':
                self.attack_direction = 0
                self.chosen_attack.rect.x = self.rect.x
                if not option > 4:
                    self.chosen_attack.rect.y = self.rect.y + 30
                else:
                    self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_up
            elif self.direction == 'D':
                self.attack_direction = 1
                self.chosen_attack.rect.x = self.rect.x
                if not option > 4:
                    self.chosen_attack.rect.y = self.rect.y + 30
                else:
                    self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_down
            elif self.direction == 'L':
                self.attack_direction = 2
                if not option > 4:
                    self.chosen_attack.rect.x = self.rect.x + 30
                else:
                    self.chosen_attack.rect.x = self.rect.x
                self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_left
            else:
                self.attack_direction = 3
                if not option > 4:
                    self.chosen_attack.rect.x = self.rect.x + 30
                else:
                    self.chosen_attack.rect.x = self.rect.x
                self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_right

            self.chosen_attack.size = 50
            self.chosen_attack.acceleration = 0.1
            self.chosen_attack.start_x = self.chosen_attack.rect.x
            self.chosen_attack.start_y = self.chosen_attack.rect.y

        if option == 1 or option == 2:
            self.attack(screen, mana, npcs)
        else:
            self.perform_action(screen, mana)
