#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from textura.font import Font


def draw(g, ax):
    for c in g:
        ax.plot(c[0], c[1], color='black', )


if __name__ == '__main__':
    plt.figure(figsize=(15, 8))

    f = Font(20, 100, 30, radius=9, x=15)
    ax = plt.subplot(231, aspect='equal')
    draw(f.g.v, ax)
    ax = plt.subplot(234, aspect='equal')
    draw(f.g.n, ax)

    f = Font(75, 100, 45, radius=30, x=30)
    ax = plt.subplot(232, aspect='equal')
    draw(f.g.v, ax)
    ax = plt.subplot(235, aspect='equal')
    draw(f.g.n, ax)

    f = Font(200, 100, 20, radius=90, x=150)
    ax = plt.subplot(233, aspect='equal')
    draw(f.g.v, ax)
    ax = plt.subplot(236, aspect='equal')
    draw(f.g.n, ax)

    plt.show()