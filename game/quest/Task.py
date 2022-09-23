
# tasks - short description, points, artifacts, whose quest, side, is_done flag, priority of the quest
class Task:
    def __init__(self, name, description, artifact, npc, points, hero, is_done):
        self.name = name
        self.description = description
        self.artifact = artifact
        self.points = points
        self.hero = hero
        self.is_done = is_done
        self.npc = npc
        self.interactions = []
        self.sentiment = "Neutral"

    def show_task(self):
        print(self.description)
