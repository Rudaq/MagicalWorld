from game.npc.Npc import Npc


# Class for a npc of type Dark Wizard, inherits from Npc class inheriting from Character class
class DarkWizard(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y):
        super().__init__(name, side, mana, life, images, artifacts, quests)
        self.rect.x = x
        self.rect.y = y
        self.race = "Dark Wizard"
