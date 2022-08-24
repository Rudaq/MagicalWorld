from game.npc.Npc import Npc


# Class for a npc of type Ice Monster, inherits from Npc class inheriting from Character class
class IceMonster(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation, collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Ice Monster"
        self.collision_sprites = collision_sprites
        self.can_talk = True