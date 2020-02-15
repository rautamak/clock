from tkinter import *

WIDTH = 400
HEIGHT = 400

class Clock:
    hour_length = 75
    minute_length = 100

    def __init__(self, canvas, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.c = canvas

    def drawHour(self, hour, minute):
        self.c.create_line(WIDTH/2, HEIGHT/2, WIDTH/2 + 100, HEIGHT/2 + 100, width=7)

    def drawMinute(self, hour, minute):
        self.c.create_line(WIDTH/2, HEIGHT/2, WIDTH/2 + 120, HEIGHT/2, width=2)

def main():
    window = Tk()
    window.title("Clock")

    c = Canvas(window, width=WIDTH, heigh=HEIGHT)
    c.pack()

    clock = Clock(c, 50, 50)
    clock.drawHour(1,1)
    clock.drawMinute(1,1)

    window.mainloop()

main()
