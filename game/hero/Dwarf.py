from game.artifacts.AttackClass import AttackClass
from game.hero.Character import Character
from game.settings import DWARVES_ACTIONS

# Class for a hero of race Dwarf, inherits from Character class
# images = entries from HERO_ANIMATIONS['Dwarf'] dict
class Dwarf(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Dwarf"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.braids_attack = AttackClass(DWARVES_ACTIONS['braids'], 20, 'braids_attacks')
        self.axe_throw_attack = AttackClass(DWARVES_ACTIONS['axe_throw'], 25, 'axe_throw_attack')
        self.axe_attack = AttackClass(DWARVES_ACTIONS['axe'], 30, 'axe_attack')
        self.sleep = AttackClass(DWARVES_ACTIONS['sleep'], 0, 'sleep')
        self.chosen_attack = None
        self.attack_direction = 0

    def throw_axe(self, screen):
        if self.performing_action:
            self.chosen_attack.attack_acceleration()
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

            # TO DO add rotation of an axe
            if draw:
                screen.blit(self.chosen_attack.image, (self.chosen_attack.rect.x, self.chosen_attack.rect.y))
                # rotated_image1 = pygame.transform.rotate(self.chosen_attack.image, 70)
                # rotated_image2 = pygame.transform.rotate(self.chosen_attack.image, 130)
                # screen.blit(rotated_image1, (self.chosen_attack.rect.x * 0.3, self.chosen_attack.rect.y))
                # screen.blit(rotated_image2, (self.chosen_attack.rect.x * 0.7, self.chosen_attack.rect.y))
        else:
            self.chosen_attack.size = 5
            self.performing_action = True
            self.attack_direction = self.direction

    def attack(self, screen, npcs):
        if self.performing_action:
            self.chosen_attack.attack_acceleration()
            if self.chosen_attack.size < 150:
                if self.chosen_attack.image == self.chosen_attack.image_up or self.chosen_attack.image == self.chosen_attack.image_down:
                    screen.blit(self.chosen_attack.image, (self.chosen_attack.rect.x, self.chosen_attack.rect.y),
                                (0, 0, 50, self.chosen_attack.size))
                else:
                    screen.blit(self.chosen_attack.image, (self.chosen_attack.rect.x, self.chosen_attack.rect.y),
                                (0, 0, self.chosen_attack.size, 50))

        else:
            self.performing_action = True
            self.attack_direction = self.direction

    def rest(self, screen):
        if self.performing_action:
            self.chosen_attack.attack_acceleration()
            if self.chosen_attack.size < 150:
                screen.blit(self.chosen_attack.image, (self.chosen_attack.rect.x, self.chosen_attack.rect.y - 5),
                            (0, 0, 50, self.chosen_attack.size))
        else:
            self.performing_action = True
            self.attack_direction = self.direction

    def fight(self, screen, option, npcs):

        if self.chosen_attack is None:
            if option == 1:
                self.chosen_attack = self.braids_attack
            elif option == 2:
                self.chosen_attack = self.axe_attack
            elif option == 3:
                self.chosen_attack = self.sleep
                self.add_life(5)
            else:
                self.chosen_attack = self.axe_throw_attack

            if self.direction == 'U' and option != 3:
                self.attack_direction = 0
                self.chosen_attack.rect.x = self.rect.x
                if not option == 4:
                    self.chosen_attack.rect.y = self.rect.y - 120
                else:
                    self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_up
            elif self.direction == 'D' and option != 3:
                self.attack_direction = 1
                self.chosen_attack.rect.x = self.rect.x
                if not option == 4:
                    self.chosen_attack.rect.y = self.rect.y + 30
                else:
                    self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_down
            elif self.direction == 'L' and option != 3:
                self.attack_direction = 2
                if not option == 4:
                    self.chosen_attack.rect.x = self.rect.x - 120
                else:
                    self.chosen_attack.rect.x = self.rect.x
                self.chosen_attack.rect.y = self.rect.y
                self.chosen_attack.image = self.chosen_attack.image_left
            else:
                self.attack_direction = 3
                if not option == 4:
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
            self.attack(screen, npcs)
        elif option == 3:
            self.rest(screen)
        else:
            self.throw_axe(screen)