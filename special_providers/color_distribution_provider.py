class ColorDistributionProvider:
    def get_color_distribution(self, balls_list):
        color_distribution = [0, 0, 0, 0]
        colors = ['red', 'blue', 'green', 'yellow']
        for i in balls_list:
            color_distribution[
                colors.index(
                    i.color
                )
            ] += 1
        return color_distribution
