class TaskManager:
    """Содержит список задач, пробегается по ним, вызывает выполнение
    tick-а каждой из задач
    , удаляет, если те выполнены."""
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def task_tick(self):
        self.tasks = [i for i in self.tasks if i.get_remain() > 0]

        for i in self.tasks:
            i.tick()
