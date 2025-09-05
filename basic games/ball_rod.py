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
        
    def move_down(self):
        if self.ycor()>-300:
            self.goto(self.xcor(),self.ycor()-20)

    def keep_moving(self,x,y):
        current_pos_x = self.xcor() + x
        current_pos_y = self.ycor() + y
        self.goto(current_pos_x,current_pos_y)

        
    