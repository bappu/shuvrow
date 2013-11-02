import simplegui
width_move=400
height_move=200
up_key=0
#defult left key
left_key=0
down_key=0
right_key=0
#count=200
image_width=100
image_height=100
def down_handler(key):
    global height_move,width_move,up_key,left_key,right_key,down_left
    if key == simplegui.KEY_MAP["up"]:
        height_move=height_move-1
        print "Works"
        up_key=1
        down_key=0
        left_key=1
        right_key=0
        
#def up_handler(key):
#    global height_move
    if key == simplegui.KEY_MAP["down"]:
        height_move=height_move+1
        print "Works"
        down_key=1
        left_key=1
        right_key=0
        up_key=0
    if key == simplegui.KEY_MAP["left"]:
        #height_move=height_move+1
        width_move=width_move-1
        print "Works"
        left_key=0
        down_key=0
        right_key=0
        up_key=0
    if key == simplegui.KEY_MAP["right"]:
        width_move=width_move+1
        print "Works"
        right_key=1
        down_key=0
        left_key=1
        up_key=0
    
    

def draw(canvas):
    global width_move,height_move,up_key,down_key,left_key,right_key
    if up_key==1:
        
        canvas.draw_image(image,(image_width/2,image_height/2),(image_width,image_height),(width_move,height_move),(30,30))
        width_move=width_move-1
        height_move=height_move-1
    #print move
    if left_key==0:
        if width_move >0:        
            canvas.draw_image(image,(image_width/2,image_height/2),(image_width,image_height),(width_move,height_move),(30,30))
        if width_move==0:
            width_move=400    
    
    
    if down_key==1:
        
        canvas.draw_image(image,(image_width/2,image_height/2),(image_width,image_height),(width_move,height_move),(30,30))
        width_move=width_move-1
        height_move=height_move+1
    
#    elif move >200:
#        global count
#        print count
#        canvas.draw_image(image,(100/2,100/2),(100,100),(200+count,200),(30,30))
#        count=count-1
#        if count == 1:
#            
#            count=200
        
        
        
def timer():
    global width_move
    width_move=width_move-1
    
    
frame=simplegui.create_frame("Test",400,400)
image=simplegui.load_image('https://dl.dropboxusercontent.com/u/68965335/panda-images/angry12.jpg')
time=simplegui.create_timer(50,timer)
drawing=frame.set_draw_handler(draw)
frame.set_keydown_handler(down_handler)
#frame.set_keyup_handler(up_handler)
frame.start()
time.start()
