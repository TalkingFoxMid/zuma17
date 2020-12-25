class TaskFreePlaceConveyor:
    """Сдигвает набор новогодних шариков на конвеере,
            чтобы места хватило для нового шарика"""
    def __init__(self, balls_slice):
        self.balls_slice = balls_slice
        self.remain = 7

    def tick(self):

        if self.remain <= 0:
            return
        for i in self.balls_slice:
            i.parameter += 0.01
        self.remain -= 1

    def get_remain(self):
        return self.remain
