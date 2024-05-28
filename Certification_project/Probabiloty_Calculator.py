import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for key,value in kwargs.items():
            for  _ in range(value):
                self.contents.append(key)

    def draw(self, number):
        # If the number of balls to draw is greater than the available balls, return all the balls
        if number >= len(self.contents):
            drawn = self.contents[:]
            self.contents = []  # All balls are drawn, so empty the hat
        else:
            drawn = random.sample(self.contents, number)
            for item in drawn:
                self.contents.remove(item)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count=0
    for i in range(num_experiments):
        expected_copy=copy.deepcopy(expected_balls)
        hat_copy=copy.deepcopy(hat)
        color_gotten=hat_copy.draw(num_balls_drawn)
        for color in color_gotten:
            if color in expected_copy:
                expected_copy[color]-=1
        if all(x<=0 for x in expected_copy.values() ):
            count+=1
    return count/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
