from game_logic.conveyor_ball import ConveyorBall
from special_providers.color_distribution_provider import ColorDistributionProvider
import unittest

color_distribution_provider = ColorDistributionProvider()

class TestColorDistributionProvider(unittest.TestCase):
    def test_color_distribution_provider(self):
        global color_distribution_provider
        assert color_distribution_provider.get_color_distribution(
            [
                ConveyorBall("red", 0),
                ConveyorBall("red", 0),
                ConveyorBall("red", 0),
                ConveyorBall("blue", 0),
                ConveyorBall("blue", 0),
                ConveyorBall("green", 0),
                ConveyorBall("yellow", 0),
            ]
        ) == [3, 2, 1, 1]
