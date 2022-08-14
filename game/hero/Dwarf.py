from game.hero.Character import Character

SPRITE_SIZE = 50


# Class for a hero of race Dwarf, inherits from Character class
class Dwarf(Character):
    def __init__(self, name, side, mana, life, images, active_quest):
        super().__init__(name, side, mana, life, images, active_quest)
        self.race = "Dwarf"