from microbit import *
import random

random.seed(2857740885)

wall = Image("55555:00000:00000:00000:00000")
field = Image()
i_wall = 0
player_x = 2
player_y = 3

scrollMs = 500
score = 0

nextScroll = running_time() + scrollMs

while True:
    if field.get_pixel(player_x, player_y):
        break
    
    if button_a.was_pressed() and player_x > 0:
        player_x = player_x - 1
    
    if button_b.was_pressed() and player_x < 4:
        player_x = player_x + 1
        
    display.set_pixel(player_x, player_y, 9)
    
    
    
    if running_time() > nextScroll:
        field = field.shift_down(1)
        nextScroll = nextScroll +  scrollMs
        
        i_wall = i_wall + 1
        if i_wall == 3:
            i_wall = 0
            field = field + wall
            
            gate = random.randrange(5)
            field.set_pixel(gate, 0, 0)
            
            score = score + 1
            
            if scrollMs > 200:
                scrollMs -= 5
            
        

        display.show(field)

display.show(Image.SAD)
sleep(500)
display.scroll(str(score), loop=True, wait=False)
        
