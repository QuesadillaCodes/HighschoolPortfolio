from microbit import *
x, y = 0, 2
dir_x, dir_y = 1, 1

while y < 5:
    x = x + dir_x
    y = y + dir_y
    
    if x == 0 or x == 4:
        dir_x = -dir_x
    
    if y == 0 or y == 4:
        dir_y = -dir_y
    
    display.set_pixel(x, y, 9)
    sleep(100)
    display.set_pixel(x, y, 0)
