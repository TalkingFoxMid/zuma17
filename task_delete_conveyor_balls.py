class TaskDeleteConveyorBalls:
    def __init__(self, balls_slice, balls_conveyor):
        self.balls_slice = balls_slice
        self.basic_remain = 11
        self.balls_conveyor = balls_conveyor
        self.remain = self.basic_remain

    def tick(self):
        self.remain -= 1
        if self.remain <= 0:
            for i in self.balls_slice:
                i.must_been_deleted = True
            try:
                index1 = self.balls_conveyor.balls_list.index(self.balls_slice[0]) - 1
                if index1 > 0:
                    self.balls_conveyor.balls_list[index1].hot = True
            except ValueError:
                pass
            index2 = self.balls_conveyor.balls_list.index(self.balls_slice[-1]) + 1

            if index2 != len(self.balls_slice):
                try:
                    self.balls_conveyor.balls_list[index2].hot = True
                except ValueError:
                    pass
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
