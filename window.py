from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Window")

        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill = fill_color,
            width=2
        )

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self):
        if self.has_left_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x1, self._y2)
            line = Line(start, end)
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            start = Point(self._x2, self._y1)
            end = Point(self._x2, self._y2)
            line = Line(start, end)
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            start = Point(self._x1, self._y1)
            end = Point(self._x2, self._y1)
            line = Line(start, end)
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            start = Point(self._x1, self._y2)
            end = Point(self._x2, self._y2)
            line = Line(start, end)
            self._win.draw_line(line, "black")

if __name__ == "__main__":
    win = Window(1920, 1440)

    cell1 = Cell(50, 100, 50, 100, win)
    cell1.draw()

    cell2 = Cell(150, 200, 50, 100, win)
    cell2.has_right_wall= False
    cell2.has_bottom_wall= False
    cell2.draw()

    win.wait_for_close()

