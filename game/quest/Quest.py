# Class modelling a quest (to be discussed)
class Quest:
    def __init__(self, description, points, artifacts, npcs):
        self.description = description
        self.points = points
        self.artifacts = artifacts
        self.npcs = npcs
        self.interactions = []
        self.sentiment = "Neutral"

    def show_quest(self):
        print(self.description)
