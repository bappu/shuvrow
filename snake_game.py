import simplegui
import random

frame_width=300
frame_height=300
x_axis=50
y_axis=70
rand_x=90
rand_y=20
#random point for snake tales

r_x=random.randrange(0,300)
r_y=random.randrange(0,300)
increment=20

left=False
right=True
up=False
down=False



def rand_line():
    global rand_x,rand_y,frame_width,frame_height
    rand_x=random.randrange(20,280)
    rand_y=random.randrange(20,280)
    
    return
def move_snake_head():
    global x_axis,y_axis
    if right==True:
        x_axis=x_axis+1
        if x_axis==frame_width:
            x_axis=0
            return
  
    if left==True:
        x_axis=x_axis-1
        if x_axis==0:
            x_axis=300
            return

    if up==True:
        y_axis=y_axis-1
        if y_axis==0:
            y_axis=300
            
            return
 
    if down==True:
        y_axis=y_axis+1
        if y_axis==300:
            y_axis=0
            return
      
def draw(canvas):  
    global x_axis,y_axis,r_x,r_y,increment
    canvas.draw_line([r_x,r_y],[r_x+20,r_y],5,'Cyan')
    if x_axis==r_x and y_axis==r_y:
        
        increment=increment+20
        print increment
        canvas.draw_line([x_axis,y_axis],[x_axis+increment,y_axis],5,'Cyan')
        r_x=random.randrange(0,290)
        r_y=random.randrange(0,290)
        return
    elif x_axis != r_x:
        canvas.draw_line([x_axis,y_axis],[x_axis+increment,y_axis],5,'Cyan')
  
    
#    canvas.draw_line([rand_x,rand_y],[rand_x+20,rand_y],12,'Cyan')

def time():
    move_snake_head()

def key_handler(key):
    global x_axis,y_axis,left,right,up,down
    if key==simplegui.KEY_MAP['left']:
        #If right button is active, than snake will unable to move to left
        if right==True:
            left=False
            right=True
            up=False
            down=False
            return
        #x_axis= x_axis-2
        else: 
            left=True
            right=False
            up=False
            down=False
            return
    
    if key==simplegui.KEY_MAP['right']:
        #x_axis= x_axis+2
        
        if left==True:
            left=True
            right=False
            up=False
            down=False
            return
        else:
            left=False
            right=True
            up=False
            down=False
    
    if key==simplegui.KEY_MAP['up']:
        #y_axis= y_axis-2       
        
        if down==True:
            left=False
            right=False
            up=False
            down=True
            return
        else: 
            left=False
            right=False
            up=True
            down=False
            return
    if key==simplegui.KEY_MAP['down']:
        #y_axis= y_axis+2  
        if up==True:
            left=False
            right=False
            up=True
            down=False
            return
        else:
            left=False
            right=False
            up=False
            down=True

frame=simplegui.create_frame("Snake Game",frame_width,frame_height)
timer=simplegui.create_timer(50,time)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler)
frame.start()
timer.start()
