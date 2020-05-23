from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    DEFAULT_BG = 'white'

    def __init__(self):
        self.root = Tk()

        self.c = Canvas(self.root, bg=self.DEFAULT_BG, width=800, height=600)
        self.c.grid(row=1, columnspan=6)

        self.pen_button = Button(self.root, text='Pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.clear_button = Button(self.root, text='Clear', command=self.clear_canvas)
        self.clear_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='Color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.bg_button = Button(self.root, text='BackGround', command=self.choose_bg_color)
        self.bg_button.grid(row=0, column=4)

        self.choose_size_button = Scale(self.root, from_= 1, to = 50, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.bg_color = self.DEFAULT_BG
        self.pen_color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def clear_canvas(self):
        self.c.delete('all')

    def choose_bg_color(self):
        self.eraser_on = False
        self.bg_color = askcolor(color=self.bg_color)[1]
        self.c.configure(bg=self.bg_color)

    def choose_color(self):
        self.eraser_on = False
        self.pen_color = askcolor(color=self.pen_color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = self.bg_color if self.eraser_on else self.pen_color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        # if smooth is True, splinesteps sets the number of line segments in a smooth curve.
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()

