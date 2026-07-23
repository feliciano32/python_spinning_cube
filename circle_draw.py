import time, os
import math

WIDTH = 15
HEIGHT = 15
theta = .05*math.pi
grid = [["~" for col in range(WIDTH)] for row in range(HEIGHT)]
HALF = math.floor(WIDTH/2)
v_endpt = [HEIGHT-1, HALF]
circle_num = 0
grid[v_endpt[1]][v_endpt[0]] = "#"

def rotate(circle_num, vecpos):
    v_x, v_y = vecpos[0] - HALF, (vecpos[1] - HALF)*(-1)
    v_newx = v_x*math.cos(theta) - v_y*math.sin(theta)
    v_newy = v_x*math.sin(theta) + v_y*math.cos(theta)
    vecpos[0], vecpos[1] = v_newx + HALF, (v_newy - HALF)*(-1)


for i in range(300):
    os.system('clear')
    grid[round(v_endpt[1])][round(v_endpt[0])] = "#"
    print('\n'.join(''.join(row) for row in grid))
    rotate(circle_num, v_endpt)
    time.sleep(.025)
    if i != 0 and i%40 == 0:
        circle_num+=1
        v_endpt = [14-circle_num, 7]
    os.system('clear')
