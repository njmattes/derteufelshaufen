#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import degrees, asin, sin
import matplotlib.pyplot as plt
from textura.font import Font


def draw(g, ax):
    for c in g:
        ax.plot(c[0], c[1], color='black', )

def draw_n_o():
    plt.figure(figsize=(15, 8))

    f = Font(20, 100, 30, radius=9, x=15)
    ax = plt.subplot(231, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(234, aspect='equal')
    draw(f.g.n, ax)

    f = Font(75, 100, 45, radius=30, x=30)
    ax = plt.subplot(232, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(235, aspect='equal')
    draw(f.g.n, ax)

    f = Font(200, 100, 20, radius=90, x=100)
    ax = plt.subplot(233, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(236, aspect='equal')
    draw(f.g.n, ax)

    plt.show()


if __name__ == '__main__':
    f = Font(200, 100, 20, radius=90, x=100)
    o = f.construction.d_ascent2()
    a = f.construction.d_ascent()
    print a, o
    print degrees(a)
    print o / 180, asin(o/180), degrees(asin(o/180))