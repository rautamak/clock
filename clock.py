import math
import datetime
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

    def drawHour(self, x, y):
        self.c.create_line(WIDTH/2, HEIGHT/2, WIDTH/2 + x, HEIGHT/2 + y, width=7)

    def drawMinute(self, x, y):
        self.c.create_line(WIDTH/2, HEIGHT/2, WIDTH/2 + x * WIDTH/3, HEIGHT/2 + y * WIDTH/3, width=2)

def countMinutePosition():
    min = int(datetime.datetime.now().strftime('%M'))

    minuteAngle = (360/60) * min -90
    pos = [math.cos(math.radians(minuteAngle)), math.sin(math.radians(minuteAngle))]

    return pos

def main():
    window = Tk()
    window.title("Clock")

    c = Canvas(window, width=WIDTH, heigh=HEIGHT)
    c.pack()

    clock = Clock(c, 50, 50)
#    clock.drawHour()
    clock.drawMinute(countMinutePosition()[0], countMinutePosition()[1])

    window.mainloop()

main()

