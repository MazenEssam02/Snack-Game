from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self) :
        super().__init__()
        self.generatefood()

    def generatefood(self):
        self.shape("circle")
        self.shapesize(0.6)
        self.pu()
        self.color('red')
        self.speed('fastest')
        self.goto(random.randint(-270,270),random.randint(-270,270))
        #ddddd
