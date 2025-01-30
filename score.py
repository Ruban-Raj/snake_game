from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(x=0, y=260)
        self.penup()
        self.color("white")
        self.update_score()
    
    def update_score(self):
        self.write(f'Score = {self.score}', move=False, align='center', font=('Arial', 24, 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f'GAME OVER! Final score is {self.score}', move=False, align='center', font=('Arial', 24, 'normal'))