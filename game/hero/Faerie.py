from game.hero.Character import Character


# Class for a hero of race Faerie, inherits from Character class
class Faerie(Character):
    def __init__(self, name, side, mana, life, images, active_quest):
        super().__init__(name, side, mana, life, images, active_quest)
        self.race = "Faerie"
