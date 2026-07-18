import time, os

WIDTH = 35
HEIGHT = 35
theta = 5
grid = [["~" for col in range(WIDTH)] for row in range(HEIGHT)]
coord = (18, 18)
grid[coord[0]][coord[1]] = "#"


def main():
    for i in range(100):
        os.system('clear')
        print('\n'.join(''.join(row) for row in grid))
        time.sleep(.1)

main()

