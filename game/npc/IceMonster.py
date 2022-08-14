from game.npc.Npc import Npc

SPRITE_SIZE = 50


# Class for a npc of type Ice Monster, inherits from Npc class inheriting from Character class
class IceMonster(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y):
        super().__init__(name, side, mana, life, images, artifacts, quests)
        self.rect.x = x
        self.rect.y = y
        self.race = "Ice Monster"
