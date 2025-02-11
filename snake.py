POSITION = [(0,0), (-20,0), (-40,0)]
from turtle import Turtle
class Snake():
    
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for seg in POSITION:
            self.add_segment(seg)
            
    def add_segment(self, seg): #each segments are turtles
        self.new_tur = Turtle(shape="square")
        self.new_tur.color("white")
        self.new_tur.penup()
        self.new_tur.speed("normal")
        self.new_tur.goto(seg)
        self.segments.append(self.new_tur)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
            
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1): #(start, stop, step)
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
    
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
    
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
        
