from game.npc.Npc import Npc


# Class for a npc of type Druid, inherits from Npc class inheriting from Character class
class Druid(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y):
        super().__init__(name, side, mana, life, images, artifacts, quests)
        self.rect.x = x
        self.rect.y = y
        self.race = "Druid"
