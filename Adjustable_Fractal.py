#!/usr/bin/python

import numpy as np
import math
from tree_class import Tree
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
plt.axis([-10, 10, 0, 10])

a0 = 10
f0 = 45
axcolor = 'lightgoldenrodyellow'
angle = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
iter = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sangle = Slider(angle, 'Angle', 1, 75, valinit=f0)
siter = Slider(iter, 'Iterations', 1, 15, valinit=a0)

def update_angle(val):
    fig.canvas.draw_idle()
sangle.on_changed(update_angle)

def update_iter(val):
    fig.canvas.draw_idle()
siter.on_changed(update_iter)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sangle.reset()
    siter.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)

def colorfunc(label):
    tree.l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

tree = Tree()
tree.origin(ax)

tree.iterate_tree(ax)
tree.iterate_tree(ax)
tree.iterate_tree(ax)
tree.iterate_tree(ax)
tree.iterate_tree(ax)
tree.iterate_tree(ax)


plt.show()
