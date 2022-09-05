import pygame.sprite

class AttackClass(pygame.sprite.Sprite):
    def __init__(self, image, strength, mana, attack_type):
        super().__init__()
        self.strength = strength
        self.mana = mana
        self.attack_type = attack_type
        self.image = image
        self.image_right = image
        self.image_left = pygame.transform.flip(self.image, True, False)
        self.image_down = pygame.transform.rotate(self.image, 270)
        self.image_up = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 50
        self.acceleration = 0.1
        self.size = 0.1
        self.start_x = 0
        self.start_y = 0

    def move_attack(self):
        self.size += (self.speed * self.acceleration)
        self.acceleration += 0.05

    def check_if_correct_distance(self, hero, npc):
        # if hero.direction == "U":
        #     if self.start_y + self.size <= npc.rect.bottomleft[1]:
        #         return True
        # elif hero.direction == "D":
        #     if self.start_y + self.size >= npc.rect.topleft[1]:
        #         return True
        # elif hero.direction == "R":
        #     if self.start_x + self.size >= npc.rect.topleft[0]:
        #         return True
        # else:
        #     if self.start_x + self.size <= npc.rect.topright[0]:
        #         return True
        if hero.direction == "U":
            if self.rect.topleft[1] <= npc.rect.bottomleft[1]:
                return True
        elif hero.direction == "D":
            if self.rect.bottomleft[1] >= npc.rect.topleft[1]:
                return True
        elif hero.direction == "R":
            if self.rect.topright[0] >= npc.rect.topleft[0]:
                return True
        else:
            if self.rect.topleft[0] <= npc.rect.topright[0]:
                return True

        return False

    def check_attack_npc_collision(self, hero, npcs):
        for npc in npcs:
            if npc.rect.colliderect(self.rect):
                # if (self.start_x + self.size) >= npc.rect.x:
                if self.check_if_correct_distance(hero, npc):

                    # for one type of Elf attack
                    if self.attack_type == "heal_spell":
                        hero.heal_spell_attack(npc)

                    # for one type of Faerie attack
                    elif self.attack_type == "fire_spell":
                        hero.fire_spell_attack(npc)

                    # for every other attack
                    else:
                        npc.life -= self.strength

                    # check if NPC is still alive
                    if npc.life < 0:
                        npc.life = 0

                hero.performing_action = False
                hero.in_attack = False
                break

    def check_attack_hero_collision(self, npc, hero, npcs):

        if hero.rect.colliderect(self.rect):
            # if (self.start_x + self.size) >= npc.rect.x:
            if self.check_if_correct_distance(npc, hero):
                hero.life -= self.strength
                if hero.life < 0:
                    hero.life = 0

        self.check_attack_npc_collision(npc, npcs)
