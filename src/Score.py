from turtle import Turtle
import random
motiv=["Negm","Allah 3alek","Dbaba","Eh el 7lawa de","Y gd3","msh momken","Ya nhar abyad"]
FONT = ("Courier", 20, "normal")

mot=Turtle()
class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-295, 305)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.write(f"Level : {self.level} ", align='left', font=FONT)

        
    def motivation(self):
        mot.clear()
        mot.color("pink")
        mot.hideturtle()
        mot.pu()
        mot.goto(-10,305)
        r=random.randint(0,len(motiv)-1)
        mot.write(motiv[r],  font=FONT)
        
    def clear_motiv(self):
        mot.clear()
    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
