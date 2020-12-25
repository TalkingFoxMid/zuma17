import math
import unittest

from special_providers.angle_provider import AngleProvider


class TestAngleProvider(unittest.TestCase):
    angle_provider = AngleProvider()

    def test_0(self):
        assert self.angle_provider.get_angle(1, 0) == 0.0

    def test_90(self):
        assert self.angle_provider.get_angle(0, 1) == 1.5707963267948966

    def test_270(self):
        assert self.angle_provider.get_angle(0, -1) == -1.5707963267948966

    def test_180(self):
        assert self.angle_provider.get_angle(-1, 0) == 3.141592653589793

    def test_quoter_1(self):
        assert self.angle_provider.get_angle(2, 1) == 0.4636476090008061

    def test_quoter_2(self):
        assert self.angle_provider.get_angle(-44, 123) == 1.9143352002287897

    def test_quoter_3(self):
        assert self.angle_provider.get_angle(-41, -14) == 3.4706423484301325

    def test_quoter_4(self):
        assert self.angle_provider.get_angle(41, -14) == -0.3290496948403394
