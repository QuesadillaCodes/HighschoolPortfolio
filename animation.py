import simplegui
import random


# Create Global Variable

global water_level
water_level = 0

global close_water
close_water = 0

global water_depleted
water_depleted = 0

global ramen_height
ramen_height = 0

global ramen_size

global water_fill
water_fill = 1

global bubble_level
global stir
stir = 0

global fork_level
fork_level = 0

# Functions

def draw_table(canvas, size):
    size = 600 - size
    canvas.draw_polygon(((0, size), (600, size), (600, 600), (0, 600), (0, size)), 5, "black", "brown")


def draw_kettle(canvas, point, width, height):
    x, y = point
    # Kettle
    canvas.draw_polygon((
                          (x - width, y),
                          (x - width, y - height), 
                          (x + width, y - height),
                          (x + width, y),
                          (x - width, y)),
                          5,
                          "black",
                          "grey"
                          )
    # Pan handle
    pan_handle_distance = x + width * 2
    canvas.draw_polygon(((x + width, y - height),
                         (pan_handle_distance, y - height),
                         (pan_handle_distance, y - height + 30),
                         (x + width, y - height + 30)
                         ), 
                         5,
                         "black",
                         "darkgrey"
                         )


def waterfall(canvas, point, point_end, size):
    global water_level
    inc_by = 1 if water_level != size else 0
    water_level += inc_by
    x, y = point
    end_x, end_y = point_end
    
    
    canvas.draw_line((end_x, end_y), (x, y), water_level, "lightblue")
        

def clear_canvas(canvas, color):
    canvas.draw_polygon(((0, 0), (600, 0), (600, 600), (0, 600), (0, 0)), 1, color, color)
    

def draw_bowl(canvas):
    # canvas.draw_circle((, 325), 100, 5, "black", "white")
    canvas.draw_polygon([(200, 300), (400, 300), (350, 400), (250, 400), (200, 300)], 5, "black", "white")
    

def draw_fork(canvas, point):
    x, y = point
    canvas.draw_polygon([(x, y), (x + 10, y), (x + 10, y + 150), (x, y + 150), (x, y)], 5, "black", "grey")
    canvas.draw_polygon([(x - 50, y + 150), (x + 60 , y + 150),(x + 60, y + 160), (x - 50, y + 160), (x - 50, y + 150)], 5, "black", "grey")
    for i in range(x - 50, x + 60, 20):
        canvas.draw_polygon([(i, 160 + y), (i + 5, 160 + y), (i + 5, 220 + y), (i - 5, 220 + y), (i, 160 + y)], 5, "black", "grey")


# Scenes

def kettle_scene(canvas):
    global close_water
    
    draw_table(canvas, 200)
    waterfall(canvas, (300, 0), (300, 400), 50)
    draw_kettle(canvas, (300, 400), 100, 150)
    
    close_water += 5 if close_water != 495 else 0
    canvas.draw_line((250, 0), (450, 0), close_water, "AntiqueWhite")
    
    
def inside_kettle(canvas):
    global water_depleted
    
    canvas.draw_polygon((
                        (0, 0),
                        (100, 0),
                        (100, 600),
                        (0, 600),
                        (0, 0)
                        ),
                        1,
                        "grey",
                        "grey"
                        )
    
    canvas.draw_polygon((
                        (500, 0),
                        (600, 0),
                        (600, 600),
                        (500, 600),
                        (500, 0)
                        ),
                        1,
                        "grey",
                        "grey"
                        )
    water_depleted += 10
                        
    canvas.draw_line((300, 600), (300, 200), 400, "lightblue")
    canvas.draw_line((300, 0), (300, water_depleted), 400, "black")
    
def ramen_fall(canvas):
    global ramen_height
    global ramen_size
    ramen_height += 20
    
    
    for i in range(250, 350, 20):
        ramen_size = random.randint(80, 160)
        
        
        canvas.draw_line((i, ramen_height), (i, ramen_height + ramen_size), 3, "gold")
        
    
    draw_bowl(canvas)
    draw_table(canvas, 200)
        
    
    
def inside_bowl(canvas):
    global water_fill
    global bubble_level
    global stir
    
    canvas.draw_circle((300, 300), 300, 5, "black", "white")
    canvas.draw_circle((300, 300), 150, 5, "lightgrey", "lightgrey")
    
    
    canvas.draw_line((200, 180), (580, 360),  5, "gold")
    canvas.draw_line((170, 400), (380, 200),  5, "gold")
    canvas.draw_line((250, 10), (400, 260),  5, "gold")
    canvas.draw_line((450, 200), (100, 500),  5, "gold")
    
    canvas.draw_line((100, 150), (190, 250),  5, "gold")
    canvas.draw_line((540, 400), (250, 200),  5, "gold")
    canvas.draw_line((370, 300), (190, 120),  5, "gold")
    canvas.draw_line((125, 400), (260, 560),  5, "gold")
    
    canvas.draw_line((500, 160), (400, 575), 5, "gold")
    canvas.draw_line((150, 123), (250, 566), 5, "gold")
    canvas.draw_line((110, 275), (465, 450), 5, "gold")
    canvas.draw_line((20, 240), (400, 500), 5, "gold")
    
    water_fill += 1 if water_fill <= 250 else 0
    
    canvas.draw_circle((300, 300), water_fill, 5, "darkblue", "skyblue")
    if water_fill >= 250:
        for bubble_x in range(100, 500, 20):
            bubble_level = random.randint(150, 450)
            canvas.draw_circle((bubble_x, bubble_level), 5, 2, "gold", "gold") # Ramen poweder
        
        
        stir += 1
        canvas.draw_circle((300, 300), stir, 1, "goldenrod", "goldenrod")
            

def fork_fall(canvas):
    global fork_level
    
    fork_level += 10 if fork_level <= 150 else 0
    draw_fork(canvas, (300, fork_level))
    draw_bowl(canvas)
    draw_table(canvas, 200)
    



def draw_handler(canvas):
    global close_water
    global water_level
    global water_fill
    global stir
    
    
    
    kettle_scene(canvas)
    if close_water == 495:
        clear_canvas(canvas, "black")
        inside_kettle(canvas)
    if water_depleted >= 600:
        clear_canvas(canvas, "AntiqueWhite")
        ramen_fall(canvas)
    if ramen_height >= 500:
        clear_canvas(canvas, "brown")
        inside_bowl(canvas)
    if stir >= 250:
        clear_canvas(canvas, "AntiqueWhite")
        fork_fall(canvas)
            
    


frame = simplegui.create_frame('Ramen', 600, 600)
frame.set_canvas_background("AntiqueWhite")
frame.set_draw_handler(draw_handler)
frame.start()