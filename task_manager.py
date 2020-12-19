class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def task_tick(self):
        for i in self.tasks:
            if i.get_remain() <= 0:
                self.tasks.remove(i)
        for i in self.tasks:
            i.tick()