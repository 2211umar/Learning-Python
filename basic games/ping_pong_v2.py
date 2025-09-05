# we will conver
# classes ( furhter functions like movement and other)
# functions
# loops
# turtle functions like listen onkeypress 
import turtle
from ball_rod import Rod_ball
       

screen = turtle.Screen()

right_Rod = Rod_ball("square","red",10,1,400,0)
left_rod = Rod_ball("square","green",10,1,-400,0)
ball = Rod_ball("circle","black",1,1,0,100)



def press(k):
    keys[k] = True
    print(f'key {k} is pressed')

def release(k):
    keys[k] = False
    print(f'key {k} is release')



screen.listen()
screen.onkeypress(lambda:press("Up"),"Up")
screen.onkeypress(lambda:press("Down"),"Down")
screen.onkeypress(lambda:press("w"),"w")
screen.onkeypress(lambda:press("s"),"s")

# are you there? 
screen.onkeyrelease(lambda:release("Up"),"Up")
screen.onkeyrelease(lambda:release("Down"),"Down")
screen.onkeyrelease(lambda:release("w"),"w")
screen.onkeyrelease(lambda:release("s"),"s")

keys = {"Up":False,"Down":False,"w":False,"s":False} # states of keys

def update():
    if keys["Up"]: right_Rod.move_up()
    if keys["Down"]: right_Rod.move_down()
    if keys["w"]: left_rod.move_up()
    if keys["s"]: left_rod.move_down()
    screen.update()
    screen.ontimer(update,16) # 60 frame keep on checking what is in dictionary # 

update()

# update function is checkign dictionary
# and key pressed and key release is actually changing the dictionary
direct_x = 1
direct_y = 1
while True:
    ball.keep_moving(direct_x,direct_y)
    if abs(ball.xcor() - right_Rod.xcor())<15 and abs(ball.ycor() - right_Rod.ycor())<50:
        direct_x = -1
    if abs(ball.xcor() - left_rod.xcor())<25 and abs(ball.ycor() - left_rod.ycor())<50:
        direct_x = 1
    if ball.ycor()>300:
        direct_y = -1
    if ball.ycor()<-300:
        direct_y = 1
    
    


turtle.done()