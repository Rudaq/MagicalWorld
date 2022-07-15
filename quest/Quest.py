class Quest:
    def __init__(self, description, points, artifacts, npcs):
        self.description = description
        self.points = points
        self.artifacts = artifacts
        self.npcs = npcs

    def show_quest(self):
        print(self.description)
