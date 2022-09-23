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

    def show_quest(self):
        print(self.description)

    def set_active_task(self):
        if len(self.tasks) > 0:
            self.active_task = self.tasks[0]
        else:
            self.hero.take_next_quest()
            self.active_task = None

    def task_completed(self, hero):
        hero.points += self.active_task.points
        self.active_task.is_done = True
        self.tasks.pop()
        self.set_active_task()



