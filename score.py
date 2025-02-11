from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day20/again/data.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.goto(x=0, y=260)
        self.penup()
        self.color("white")
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score} Highscore= {self.highscore}', move=False, align='center', font=('Arial', 24, 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.update_score()
    
    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("day20/again/data.txt", "w") as file:
                file.write(f"{self.score}")
        # with open("day20/again/data.txt") as file:
        #     self.highscore = int(file.read())
        self.score = 0
        self.update_score()
    
    # def game_over(self):
    #     self.clear()
    #     self.goto(x=0, y=0)
    #     self.write(f'GAME OVER! Final score is {self.score}', move=False, align='center', font=('Arial', 24, 'normal'))