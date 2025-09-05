# we will conver
# classes ( furhter functions like movement and other)
# functions
# loops
# turtle functions like listen onkeypress 
import turtle

class Rod_ball(turtle.Turtle):
    def __init__(self,shape_parameter,color_p,width,height,position_x,position_y):
        super().__init__()
        self.shape(shape_parameter)
        self.shapesize(width,height)
        self.color(color_p)
        self.penup()
        self.goto(position_x,position_y)
    def move_up(self):
        if self.ycor()< 300:
            self.goto(self.xcor(),self.ycor()+20)
        turtle.update()
    def move_down(self):
        if self.ycor()>-300:
            self.goto(self.xcor(),self.ycor()-20)
        turtle.update()

right_Rod = Rod_ball("square","red",10,1,400,0)
left_rod = Rod_ball("square","green",10,1,-400,0)
ball = Rod_ball("circle","black",5,5,0,100)

turtle.tracer(0)
turtle.listen()
turtle.onkeypress(right_Rod.move_up,"Up")
turtle.onkeypress(right_Rod.move_down,"Down")
turtle.onkeypress(left_rod.move_up,"w")
turtle.onkeypress(left_rod.move_down,"s")





turtle.done()