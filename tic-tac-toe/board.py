from turtle import Turtle, Screen

class Board(Turtle):
    def __init__(self):
        super().__init__()
        #self.x



    screen = Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("Black")
    screen.title("Tic Tac Toe")

    # = [['x'], [], [],
    #      [], [], [],
    #      [], [], []]

    screen.exitonclick()