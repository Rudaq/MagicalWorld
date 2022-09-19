
# Class modelling a quest (to be discussed)
# quests - short description, points, artifacts, whose quest, side, is_done flag, priority of the quest
class Quest:
    def __init__(self, description, points, artifacts, npcs, side, is_done, priority):
        self.description = description
        self.points = points
        self.artifacts = artifacts
        self.npcs = npcs
        self.side = side
        self.is_done = is_done
        self.priority = priority
        self.interactions = []
        self.sentiment = "Neutral"

    def show_quest(self):
        print(self.description)
