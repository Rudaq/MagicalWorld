from game.npc.Npc import Npc


# Class for a npc of type Mermaid, inherits from Npc class inheriting from Character class
class Mermaid(Npc):
    def __init__(self, name, side, mana, life, images, artifacts, quests, x, y, pos, groups, inflation, collision_sprites):
        super().__init__(name, side, mana, life, images, artifacts, quests, pos, groups, inflation, collision_sprites)
        self.rect.x = x
        self.rect.y = y
        self.race = "Mermaid"
        self.collision_sprites = collision_sprites

    # Method move to stop mermaid from moving (not moving; on the beach)
    def move(self, direction="R", dx=0, dy=0):
        pass
