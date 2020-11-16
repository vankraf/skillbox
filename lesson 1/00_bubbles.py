# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

HEIGH = 600
WIDTH = 1200

sd.resolution = (WIDTH, HEIGH)

def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)

point = sd.get_point(300,300)

for y in range(300, 600, 100):
    for x in range(100, 1000, 100):
        point = sd.get_point(x, y)
        bubble(point,5)


for _ in range(100):
    point = sd.get_point(randint(0,WIDTH),randint(0,HEIGH))
    bubble(point,5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


