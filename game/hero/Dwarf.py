from artifacts.AttackClass import AttackClass
from hero.Character import Character
from settings import DWARVES_ACTIONS


# Class for a hero of race Dwarf, inherits from Character class
# images = entries from HERO_ANIMATIONS['Dwarf'] dict
class Dwarf(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Dwarf"
        self.collision_sprites = collision_sprites
        self.pos = pos
        self.braids_attack = AttackClass(DWARVES_ACTIONS['braids'], 20, 10, 'braids_attacks')
        self.axe_throw_attack = AttackClass(DWARVES_ACTIONS['axe_throw'], 25, 20, 'axe_throw_attack')
        self.axe_attack = AttackClass(DWARVES_ACTIONS['axe'], 30, 15, 'axe_attack')
        self.sleep = AttackClass(DWARVES_ACTIONS['sleep'], 0, 20, 'sleep')

    def throw_axe(self, screen):
        if self.in_attack:
            self.attack_type.attack_acceleration()
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

            # TO DO add rotation of an axe
            if draw:
                screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y))
                # rotated_image1 = pygame.transform.rotate(self.chosen_attack.image, 70)
                # rotated_image2 = pygame.transform.rotate(self.chosen_attack.image, 130)
                # screen.blit(rotated_image1, (self.chosen_attack.rect.x * 0.3, self.chosen_attack.rect.y))
                # screen.blit(rotated_image2, (self.chosen_attack.rect.x * 0.7, self.chosen_attack.rect.y))
        else:
            self.attack_type.size = 5
            self.in_attack = True
            self.attack_direction = self.direction

    def attack(self, screen, npcs):
        if self.in_attack:
            self.attack_type.attack_acceleration()
            if self.attack_type.size < 150:
                if self.attack_type.image == self.attack_type.image_up or self.attack_type.image == self.attack_type.image_down:
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, 50, self.attack_type.size))
                else:
                    screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y),
                                (0, 0, self.attack_type.size, 50))
            self.attack_type.check_attack_npc_collision(self, npcs)

        else:
            self.in_attack = True
            self.attack_direction = self.direction


    def rest(self, screen):
        if self.in_attack:
            self.attack_type.attack_acceleration()
            if self.attack_type.size < 150:
                screen.blit(self.attack_type.image, (self.attack_type.rect.x, self.attack_type.rect.y - 5),
                            (0, 0, 50, self.attack_type.size))
        else:
            self.in_attack = True
            self.attack_direction = self.direction

    def fight(self, screen, option, npcs):

        if self.attack_type is None:
            if option == 1:
                self.attack_type = self.braids_attack
            elif option == 2:
                self.attack_type = self.axe_attack
            elif option == 3:
                self.attack_type = self.sleep
                self.add_life(5)
            else:
                self.attack_type = self.axe_throw_attack

            if self.direction == 'U' and option != 3:
                self.attack_direction = 0
                self.attack_type.rect.x = self.rect.x
                if not option == 4:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_up
            elif self.direction == 'D' and option != 3:
                self.attack_direction = 1
                self.attack_type.rect.x = self.rect.x
                if not option == 4:
                    self.attack_type.rect.y = self.rect.y + 30
                else:
                    self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_down
            elif self.direction == 'L' and option != 3:
                self.attack_direction = 2
                if not option == 4:
                    self.attack_type.rect.x = self.rect.x + 30
                else:
                    self.attack_type.rect.x = self.rect.x
                self.attack_type.rect.y = self.rect.y
                self.attack_type.image = self.attack_type.image_left
            else:
                self.attack_direction = 3
                if not option == 4:
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
        elif option == 3:
            self.rest(screen)
        else:
            self.throw_axe(screen)
