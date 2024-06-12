from turtle import Turtle
LEFT=180
UP=90
RIGHT=0
DOWN=270
step=20


class Snake(Turtle):
    def __init__(self) :
        super().__init__()
        self.all_snakes = []
        self.addsegment((0,0))
        self.head=self.all_snakes[0]

    # def createsnake(self):

        
    def addsegment(self,position):
        snake = Turtle('square')
        snake.color('lightblue')
        snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
        snake.pu()
        
        snake.goto(position)
        self.all_snakes.append(snake)
    
    def extend(self):
        self.addsegment(self.all_snakes[-1].position())
    def move(self):
        for segments in range(len(self.all_snakes)-1,0,-1):
            self.all_snakes[segments].goto(self.all_snakes[segments-1].position())
        self.head.forward(step)
    
    def UP(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def DOWN(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def RIGHT(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def LEFT(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
