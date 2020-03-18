from vpython import *
ball = sphere(pos=vec(0,10,0), radius=1, color=color.red)
floor= box(pos=vec(0,0,0),size=vec(10,0.5,10),color=color.green)
dt = 0.01 #time intervals
ball.velocity = vector(0,0,0)
t = 0
g = -9.8
while(t<20):
    rate(100)
    ball.velocity.y = ball.velocity.y + g*dt
    ball.pos = ball.pos+ball.velocity*dt
    if ball.pos.y<floor.pos.y:
        ball.velocity.y = -ball.velocity.y 
    t = t+dt
