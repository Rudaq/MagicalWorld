
# tasks - short description, points, artifacts, whose quest, side, is_done flag, priority of the quest
class Task:
    def __init__(self, name, description, artifact, points, npc_give_task, npc_take_artifact, next_npc, gift, hero, is_done):
        self.name = name
        self.description = description
        self.artifact = artifact
        self.points = points
        self.hero = hero
        self.is_done = is_done
        # NPC from which hero gets the task
        self.npc_give_task = npc_give_task
        # NPC to which hero needs to give the artifact
        self.npc_take_artifact = npc_take_artifact
        # NPC which needs to give you something in order to finish the active quest
        self.next_npc = next_npc
        # gift which hero will get from NPC after finishing a task
        self.gift = gift
        self.interactions = []
        self.sentiment = "Neutral"
        # check if hero have seen the task
        self.is_opened = False

    def show_task(self):
        print(self.description)
