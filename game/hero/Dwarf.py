from game.hero.Character import Character


# Class for a hero of race Dwarf, inherits from Character class
# images = entries from HERO_ANIMATIONS['Dwarf'] dict
class Dwarf(Character):
    def __init__(self, name, side, mana, life, images, active_quest):
        super().__init__(name, side, mana, life, images, active_quest)
        self.race = "Dwarf"
