from game_logic.conveyor_ball import ConveyorBall
from special_providers.color_distribution_provider import ColorDistributionProvider

color_distribution_provider = ColorDistributionProvider()


def test_color_distribution_provider():
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
