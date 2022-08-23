from game.hero.Character import Character


# Class for a hero of race Wizard, inherits from Character class
class Wizard(Character):
    def __init__(self, name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites=None):
        super().__init__(name, side, mana, life, images, active_quest, pos, groups, inflation, collision_sprites)
        self.race = "Wizard"
        self.collision_sprites = collision_sprites
        self.pos = pos