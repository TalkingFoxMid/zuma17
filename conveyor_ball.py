class ConveyorBall:
    def __init__(self, color, parameter):
        self.parameter = parameter
        self.color = color
        self.x = 0
        self.y = 0
        self.diameter = 42
        self.must_been_deleted = False
        self.unriverable = False
