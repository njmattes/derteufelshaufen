#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import degrees, asin, sin
import matplotlib.pyplot as plt
from textura.font import Font


def draw(g, ax):
    for c in g:
        ax.plot(c[0], c[1], color='black', )

def draw_alpha(s, c, a, r, x):
    plt.figure(figsize=(24, 4))
    n = 9

    f = Font(s, c, a, radius=r, x=x)
    ax = plt.subplot('1{}6'.format(n), aspect='equal')
    draw(f.g.n, ax)
    ax = plt.subplot('1{}1'.format(n), sharey=ax, aspect='equal')
    draw(f.g.b, ax)
    ax = plt.subplot('1{}2'.format(n), sharey=ax, aspect='equal')
    draw(f.g.c, ax)
    ax = plt.subplot('1{}3'.format(n), sharey=ax, aspect='equal')
    draw(f.g.d, ax)
    ax = plt.subplot('1{}4'.format(n), sharey=ax, aspect='equal')
    draw(f.g.h, ax)
    ax = plt.subplot('1{}5'.format(n), sharey=ax, aspect='equal')
    draw(f.g.l, ax)
    ax = plt.subplot('1{}7'.format(n), sharey=ax, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot('1{}8'.format(n), sharey=ax, aspect='equal')
    draw(f.g.p, ax)
    ax = plt.subplot('1{}9'.format(n), sharey=ax, aspect='equal')
    draw(f.g.v, ax)

    plt.show()

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

def draw_c_o():
    plt.figure(figsize=(15, 8))

    f = Font(20, 100, 30, radius=9, x=15)
    ax = plt.subplot(231, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(234, aspect='equal')
    draw(f.g.c, ax)

    f = Font(75, 100, 45, radius=35, x=30)
    ax = plt.subplot(232, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(235, aspect='equal')
    draw(f.g.c, ax)

    f = Font(200, 100, 20, radius=90, x=100)
    ax = plt.subplot(233, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(236, aspect='equal')
    draw(f.g.c, ax)

    plt.show()

def draw_d_o():
    plt.figure(figsize=(20, 4))

    f = Font(20, 100, 30, radius=9, x=15)
    ax = plt.subplot(231, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(234, aspect='equal')
    draw(f.g.d, ax)

    f = Font(75, 100, 45, radius=35, x=30)
    ax = plt.subplot(232, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(235, aspect='equal')
    draw(f.g.d, ax)

    f = Font(200, 100, 20, radius=90, x=100)
    ax = plt.subplot(233, aspect='equal')
    draw(f.g.o, ax)
    ax = plt.subplot(236, aspect='equal')
    draw(f.g.d, ax)

    plt.show()

def draw_h():
    plt.figure(figsize=(20, 9))

    f = Font(20, 70, 30, 9, 15)
    ax = plt.subplot(231, aspect='equal')
    draw(f.g.h, ax)
    ax = plt.subplot(234, aspect='equal')
    draw(f.g.n, ax)

    f = Font(75, 100, 45, 35, 40)
    ax = plt.subplot(232, aspect='equal')
    draw(f.g.h, ax)
    ax = plt.subplot(235, aspect='equal')
    draw(f.g.n, ax)

    f = Font(200, 100, 20, 90, 100)
    ax = plt.subplot(233, aspect='equal')
    draw(f.g.h, ax)
    ax = plt.subplot(236, aspect='equal')
    draw(f.g.n, ax)

    plt.show()




if __name__ == '__main__':
    draw_h()
    # draw_alpha(200, 80, 20, 95, -10)
    # draw_alpha(70, 80, 30, 34, -10)
    # draw_alpha(20, 80, 45, 10, 15)