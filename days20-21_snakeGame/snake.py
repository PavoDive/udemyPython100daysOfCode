from turtle import Turtle, Screen

MOVE_DISTANCE = 20
POSITIONS = [(0, 0), (0, -20), (0, -40)]

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0] # this is created to avoid repeating self.snake[0]

    def create_snake(self):
        for position  in POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, x_position):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.penup()
        new_segment.shape("square")
        new_segment.goto(x_position)
        self.snake.append(new_segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):

        for segment in range(len(self.snake) - 1, 0, -1):
            x_position = self.snake[segment - 1].xcor()
            y_position = self.snake[segment - 1].ycor()
            self.snake[segment].goto(x = x_position, y = y_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
