from artifacts.AttackClass import AttackClass
from hero.Character import Character
from settings import DWARVES_ACTIONS


# Class for a hero of race Dwarf, inherits from Character class
# images = entries from HERO_ANIMATIONS['Dwarf'] dict
class Dwarf(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Dwarf"
        self.attack_type = None
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.braids_attack = AttackClass(DWARVES_ACTIONS['braids'], 20, 10, 'braids_attacks')
        self.axe_attack = AttackClass(DWARVES_ACTIONS['axe'], 30, 15, 'axe_attack')
        self.sleep = AttackClass(DWARVES_ACTIONS['sleep'], 0, 20, 'sleep')

    def attack(self, screen, npcs):
        if self.in_attack:
            self.attack_type.move_attack()
            if self.attack_type.size < 150:
                if self.attack_type.image == self.attack_type.image_up or self.attack_type.image == self.attack_type.image_down:
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, 50, self.attack_type.size))
                else:
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, self.attack_type.size, 50))
            self.attack_type.check_attack_npc_collision(self, npcs)
        if self.mana - self.attack_type.mana >= 0:
            self.mana -= self.attack_type.mana

    def fight(self, screen, option, npcs):
        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.axe_attack
            elif option == 2:
                self.attack_type = self.braids_attack
            elif option == 3:
                self.attack_type = self.sleep

            if self.direction == 'U': ## aqui
                self.attack_direction = 0
                if option == 2:
                    self.attack_type.rect.x = self.rect.x - 20
                    self.attack_type.rect.y = self.rect.y - 70
                else:
                    self.attack_type.rect.x = self.rect.x - 10
                    self.attack_type.rect.y = self.rect.y - 5
                self.attack_type.image = self.attack_type.image_up
            elif self.direction == 'D':
                self.attack_direction = 1
                if option == 2:
                    self.attack_type.rect.x = self.rect.x + 20
                    self.attack_type.rect.y = self.rect.y + 45
                else:
                    self.attack_type.rect.x = self.rect.x + 10
                    self.attack_type.rect.y = self.rect.y + 35
                self.attack_type.image = self.attack_type.image_down
            elif self.direction == 'L': ## aqui
                self.attack_direction = 2
                if option == 2:
                    self.attack_type.rect.x = self.rect.x - 80
                else:
                    self.attack_type.rect.x = self.rect.x - 20
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                self.attack_direction = 3
                if option == 2:
                    self.attack_type.rect.x = self.rect.x + 30
                else:
                    self.attack_type.rect.x = self.rect.x + 20
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_right

            self.attack_type.size = 50
            self.attack_type.acceleration = 0.1
            self.attack_type.start_x = self.attack_type.rect.x
            self.attack_type.start_y = self.attack_type.rect.y

        self.attack(screen, npcs)
