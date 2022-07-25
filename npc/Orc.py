from npc.Npc import Npc

SPRITE_SIZE = 50


# Class for a npc of type Orc, inherits from Npc class inheriting from Character class
class Orc(Npc):
    def __init__(self, name, side, mana, life, images, race, artifacts, quests, x, y):
        super().__init__(name, side, mana, life, images, race, artifacts, quests)
        self.rect.x = x
        self.rect.y = y
