class Quest:
    def __init__(self, name, description, points, tasks, hero, is_done):
        self.name = name
        self.description = description
        self.points = points
        self.tasks = tasks
        self.hero = hero
        self.is_done = is_done
        self.interactions = []
        self.active_task = None
        self.active_task = None
        self.sentiment = "Neutral"
        # task 'skipped' because hero needs to et something for this task
        self.skipped_tasks = []

    def show_quest(self):
        print(self.description)

    def set_active_task(self):
        if len(self.tasks) > 0:
            self.active_task = self.tasks[0]
        else:
            self.hero.take_next_quest()
            self.active_task = None

    def task_completed(self, hero, npcs):
        hero.points += self.active_task.points
        self.active_task.is_done = True

        if self.active_task.gift is not None:
            hero.take_gift_from_npc(self.active_task.npc_take_artifact, npcs, self.active_task.gift)

        self.tasks.remove(self.active_task)
        if len(self.skipped_tasks) > 0:
            index = len(self.skipped_tasks) - 1
            self.active_task = self.skipped_tasks[index]
            self.skipped_tasks.remove(self.active_task)
        else:
            self.set_active_task()

    def set_next_active_task(self):
        self.skipped_tasks.append(self.active_task)
        index = 0
        for i in range(len(self.tasks) - 1):
            if self.tasks[i] == self.active_task:
                index = i + 1
                break
        self.active_task = self.tasks[index]
