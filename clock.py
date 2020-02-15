import time
import math
import datetime
from tkinter import *

WIDTH = 400
HEIGHT = 400

class Clock:

    def __init__(self, canvas, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.c = canvas

    def drawHour(self, x, y):
        h = self.c.create_line(WIDTH/2, HEIGHT/2, WIDTH/2 + x * WIDTH/4, HEIGHT/2 + y * WIDTH/4, width=7)
        return h

    def drawMinute(self, x, y):
        m = self.c.create_line(WIDTH/2, HEIGHT/2, WIDTH/2 + x * WIDTH/3, HEIGHT/2 + y * WIDTH/3, width=2)
        return m


    def clear(self, items):
        for item in items:
            self.c.delete(item)

def countHourPosition():
    hour = int(datetime.datetime.now().strftime('%-I')) + int(datetime.datetime.now().strftime('%M')) / 60

    print(hour)
    hourAngle = (360/12) * hour - 90
    pos = [math.cos(math.radians(hourAngle)), math.sin(math.radians(hourAngle))]

    return pos

def countMinutePosition():
    min = int(datetime.datetime.now().strftime('%M'))

    minuteAngle = (360/60) * min - 90
    pos = [math.cos(math.radians(minuteAngle)), math.sin(math.radians(minuteAngle))]

    return pos

def runClock(window, clock, h, m):
    clock.clear([h, m])
    h = clock.drawHour(countHourPosition()[0], countHourPosition()[1])
    m = clock.drawMinute(countMinutePosition()[0], countMinutePosition()[1])
    print("Clock updated")
    window.after(1000, runClock, window, clock, h, m)

def main():
    window = Tk()
    window.title("Clock")

    c = Canvas(window, width=WIDTH, heigh=HEIGHT)
    c.pack()

    clock = Clock(c, 50, 50)
    h = clock.drawHour(countHourPosition()[0], countHourPosition()[1])
    m = clock.drawMinute(countMinutePosition()[0], countMinutePosition()[1])

    runClock(window, clock, h, m);
    window.mainloop()

main()

