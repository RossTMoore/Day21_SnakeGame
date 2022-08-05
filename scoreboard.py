from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Monaco", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.penup()
        self.setposition(0, 270)
        self.color("white")
        self.add_points()

    def add_points(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)




