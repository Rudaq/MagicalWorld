from npc.Npc import Npc

SPRITE_SIZE = 50


# Class for a npc of type Mermaid, inherits from Npc class inheriting from Character class
class Mermaid(Npc):
    def __init__(self, name, side, mana, life, images, race, artifacts, quests, x, y):
        super().__init__(name, side, mana, life, images, race, artifacts, quests)
        self.rect.x = x
        self.rect.y = y

    # Method move to stop mermaid from moving (not moving; on the beach)
    def move(self, direction="R", dx=0, dy=0):
        pass

