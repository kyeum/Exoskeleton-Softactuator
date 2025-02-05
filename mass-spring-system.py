from vpython import *

#display(width=600,height=600,center=vector(6,0,0),background=color.white)

wall=box(pos=vector(0,0,0),size=vector(10,2,10),color=color.green)
#floor=box(pos=vector(6,-0.6,0),size=vector(14,0.2,4),color=color.green)
Mass=box(pos=vector(0,-9,0),velocity=vector(0,0,0),size=vector(1,1,1),mass=0.5,color=color.blue)
pivot=vector(0,0,0)
#spring constant
G = 8000
d = 0.08
D = 0.8
n = 12
k = G*pow(d,4)/(8*pow(D,3)*n)

spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.4,constant=k,thickness=0.04,coils=12,color=color.red)
eq=vector(0,-9,0)
t=0
dt=0.01
g = vector(0,-9.8,0)
f1 = graph(width=400,height=400,title='A First graph',xtitle='time',ytitle='Force',foreground=color.black, background=color.white)
f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.red)
temp = 0

while (t<50):
  rate(100)
  acc=(eq-Mass.pos)*(spring.constant/Mass.mass)+g
  Mass.velocity=Mass.velocity+acc*dt
  Mass.pos=Mass.pos+Mass.velocity*dt
  spring.axis=Mass.pos-spring.pos
  f1.plot(t,spring.constant)  
  f2.plot(t,acc.z)
  t=t+dt
  
'''
#display(width=500,height=500,center=vector(6,0,0),background=color.white)
wall=box(pos=vector(0,1,0),size=vector(0.2,3,2),color=color.green) 
floor=box(pos=vector(6,-0.6,0),size=vector(14,0.2,4),color=color.green)
Mass=box(pos=vector(9,0,0),velocity=vector(1,0,0),size=vector(1,1,1),mass=1.0,color=color.blue)
pivot=vector(0,0,0)
spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.4,constant=1,thickness=0.1,coils=20,color=color.red)
eq=vector(9,0,0)
t=0
dt=0.001
graph1=gdisplay(x=550,y=0,width=400,height=400,title='Energy Vs. Time', xtitle='time',ytitle='Energy',foreground=color.black, background=color.white)
graph2=gdisplay(x=950,y=0,width=400,height=400,title='Phase Diagram', xtitle='Position',ytitle='Velocity',foreground=color.black, background=color.white)
fke=gcurve(gdisplay=graph1,color=color.red)
fpe=gcurve(gdisplay=graph1,color=color.blue)
fte=gcurve(gdisplay=graph1,color=color.black)
fphase=gcurve(gdisplay=graph2,color=color.black)
while (t<50):
  rate(100)
  acc=(eq-Mass.pos)*(spring.constant/Mass.mass)
  Mass.velocity=Mass.velocity+acc*dt
  Mass.pos=Mass.pos+Mass.velocity*dt
  spring.axis=Mass.pos-spring.pos
  KE=0.5*Mass.mass*(Mass.velocity.x)**2
  PE=0.5*spring.constant*(eq.x-Mass.pos.x)**2
  fke.plot(pos=(t,KE))
  fpe.plot(pos=(t,PE))
  fte.plot(pos=(t,KE+PE))
  fphase.plot(pos=(eq.x-Mass.pos.x,Mass.velocity.x))
  t=t+dt
'''
