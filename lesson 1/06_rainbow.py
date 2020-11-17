# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


HEIGH = 600
WIDTH = 1200

sd.resolution = (WIDTH, HEIGH)


for y, color in enumerate(rainbow_colors):
    start_point = sd.get_point(300, 30 + y * 10)
    end_point = sd.get_point(700, 30 + y * 10)
    sd.line(start_point=start_point, end_point=end_point, width=4, color=color)



point = sd.get_point(700, 0)
for y, color in enumerate(rainbow_colors):

    sd.circle(width=4, color=color, radius=200+y*10, center_position=point)

sd.pause()
