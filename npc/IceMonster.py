from npc.Npc import Npc

SPRITE_SIZE = 50


class IceMonster(Npc):
    def __init__(self, name, side, mana, life, image, image_left, image_right, race, artifacts, quests, x, y):
        super().__init__(name, side, mana, life, image, image_left, image_right, race, artifacts, quests)
        self.rect.x = x
        self.rect.y = y
