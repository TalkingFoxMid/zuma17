import math

from special_providers.angle_provider import AngleProvider
import unittest



class TestAngleProvider(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.angle_provider = AngleProvider()
    def angle_provider_test(self):
        global angle_provider
        assert self.angle_provider.get_angle(1, 0) == 0.0
        assert self.angle_provider.get_angle(0, 1) == 1.5707963267948966
        assert self.angle_provider.get_angle(0, -1) == -1.5707963267948966
        assert self.angle_provider.get_angle(-1, 0) == 3.141592653589793
        assert self.angle_provider.get_angle(2, 1) == 0.4636476090008061
        assert self.angle_provider.get_angle(44, 123) == 1.2272574533610034
        assert self.angle_provider.get_angle(-41, 14) == 2.8125429587494537
