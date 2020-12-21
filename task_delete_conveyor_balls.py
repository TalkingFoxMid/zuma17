class TaskDeleteConveyorBalls:
    def __init__(self, balls_slice):
        self.balls_slice = balls_slice
        self.basic_remain = 11
        self.remain = self.basic_remain
    def tick(self):
        self.remain -= 1
        print(self.remain)
        if self.remain <= 0:
            for i in self.balls_slice:
                i.must_been_deleted = True
            return
        for i in self.balls_slice:
            if self.remain == self.basic_remain - 1:
                i.start_x = i.x
                i.start_y = i.y
            i.x = 400 + (i.start_x - 400) * (self.remain / self.basic_remain)
            i.y = 400 + (i.start_y - 400) * (self.remain / self.basic_remain)

            i.diameter *= 0.7

    def get_remain(self):
        return self.remain