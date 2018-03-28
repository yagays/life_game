import sys
import time
import numpy as np
import curses


class LifeGame():
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.grid = np.zeros([self.height, self.width])
        self.generation = 0
        self.max_generation = 10

    def set_grid(self, grid):
        self.grid = grid

    def view(self):
        output = ""
        for row in self.grid:
            for cell in row:
                if cell == 1:
                    output += "＊"
                else:
                    output += "・"
            output += "\n"
        stdscr = curses.initscr()
        stdscr.addstr(0, 0, "Generation: {}\n".format(self.generation))
        stdscr.addstr(1, 0, output)
        time.sleep(0.1)

    def around(self, x, y):
        if x in (0, self.height - 1) or y in (0, self.width - 1):
            return 0
        count = 0
        # for i in range(-1, 2):
        #     for j in range(-1, 2):
        #         count += self.grid[x + i][y + j]
        count += self.grid[x - 1][y - 1]
        count += self.grid[x][y - 1]
        count += self.grid[x + 1][y - 1]
        count += self.grid[x - 1][y]
        # count += self.grid[x][y] # exclude target cell
        count += self.grid[x + 1][y]
        count += self.grid[x - 1][y + 1]
        count += self.grid[x][y + 1]
        count += self.grid[x + 1][y + 1]
        return count

    def run(self):
        self.view()
        for i in range(self.max_generation):
            self.step()
            self.generation += 1
            self.view()

    def step(self):
        new_grid = np.zeros([self.height, self.width])
        for x in range(self.height):
            for y in range(self.width):
                target_cell = self.grid[x][y]
                around_cell_num = self.around(x, y)
                if target_cell == 1:
                    if around_cell_num in (2, 3):
                        new_grid[x][y] = 1
                    else:
                        new_grid[x][y] = 0
                else:
                    if around_cell_num == 3:
                        new_grid[x][y] = 1
                    else:
                        new_grid[x][y] = 0
        self.grid = new_grid

    def add_glider(self, position_x, position_y):
        self.grid[position_x][position_y + 1] = 1
        self.grid[position_x + 1][position_y + 2] = 1
        self.grid[position_x + 2][position_y + 2] = 1
        self.grid[position_x + 2][position_y + 1] = 1
        self.grid[position_x + 2][position_y] = 1

    def random(self):
        self.grid = np.random.randint(0, 2, (self.height, self.width))

    def random_ratio(self, ratio):
        n = int(self.width * self.height * ratio)
        x = np.random.randint(0, self.width, n)
        y = np.random.randint(0, self.height, n)
        for i, j in zip(x, y):
            self.grid[i][j] = 1
