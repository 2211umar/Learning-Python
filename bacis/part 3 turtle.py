import turtle as tt 
import math
import random


t1 = tt.Turtle()
t1.color('red')
t1.shape('turtle')
t1.shapesize(2,2)


t2 = tt.Turtle()
t2.color('blue')
t2.shape('turtle')
t2.shapesize(2,2)


t0 = tt.Turtle()
t0.color('green')
t0.shape('turtle')
t0.shapesize(2,2)


t3 = tt.Turtle()
t3.color('white')
t3.shape('turtle')
t3.shapesize(2,2)


t4 = tt.Turtle()
t4.color('black')
t4.shape('turtle')
t4.shapesize(2,2)


myturles = [t1, t2, t3,t4,t0]

y_pos = -200
x_pos = -300
for i in range(5):
    current_tur = myturles[i]
    current_tur.goto(x_pos,y_pos)
    y_pos = y_pos + 100
 


tt.mainloop()


