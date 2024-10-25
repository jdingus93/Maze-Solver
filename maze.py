from cell import *
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _create_cells(self):
        self._cells = []

        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
        
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell = self._cells[self._num_rows-1][self._num_cols-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        
        while True:
            possible_directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            # right
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            # down
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            
            random_index = random.randrange(len(possible_directions))
            next_cell = possible_directions[random_index]

            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i +1][j].has_left_wall = False
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])