import copy
import random

class Hat:
    def __init__(self, **ball_colors):
        self.contents = []
        for color, count in ball_colors.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents = []  # Empty the hat
            return drawn_balls

        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    def check_drawn_balls(drawn_balls, expected_balls):
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                return False
        return True

    success_count = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**{color: hat.contents.count(color) for color in hat.contents})
        drawn_balls = hat_copy.draw(num_balls_drawn)
        if check_drawn_balls(drawn_balls, expected_balls):
            success_count += 1
    
    return success_count / num_experiments

