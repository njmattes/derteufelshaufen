# -*- coding: utf-8 -*-
from __future__ import division
from math import cos, tan, sin
import numpy as np
from textura.glyph import Glyph


class Glyphs(object):
    def __init__(self, components):
        self.components = components

    def zero(self, g):
        g = np.array(g)
        g[0][:] -= min(g[0][:])
        g[1][:] -= min(g[1][:])
        return g

    @property
    def b(self):
        coords = [[0,], [0, ], ]
        coords = self.components.moveto_lower_bowl(*coords)
        coords = self.components.lower_bowl(*coords)
        coords = self.components.ascender(*coords)
        coords = self.components.lower_counter(*coords)
        coords = self.components.upper_left_serif(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords)]

    def c(self, ax):
        theta = self.theta
        phi = self.phi
        s = self.stem
        c = self.counter
        n = .5
        nr = .5
        r = self.radius
        sigma = self.sigma
        rho = (s * 2 + c - sigma)
        height = 700
        xs = []
        ys = []
        _ang = phi

        _xx = s + c + 2 * r * sin(_ang) - sigma

        _x = 0
        _y = 0
        xs.append(_x)
        ys.append(_y)

        _x -= (sigma + _xx) * .9 - 2 * r * sin(_ang/2)
        _y -= _x * tan(_ang/2)
        xs.append(_x)
        ys.append(_y)

        _y = height - sigma * tan(theta)
        xs.append(_x)
        ys.append(_y)

        _x += sigma
        _y += sigma * tan(theta)
        xs.append(_x)
        ys.append(_y)


        _x += _xx
        _y -= _xx * tan(_ang)
        xs.append(_x)
        ys.append(_y)

        _x -= 2 * r * sin(_ang)
        _y -= 2 * r * cos(_ang)
        xs.append(_x)
        ys.append(_y)

        _x -= c
        _y += c * tan(_ang)
        xs.append(_x)
        ys.append(_y)

        _y = ((sigma + _xx) * .9 - s) * tan(_ang/2) + 2 * r * cos(_ang/2)
        xs.append(_x)
        ys.append(_y)

        _x += ((sigma + _xx) * .9 - s)
        _y = 2 * r * cos(_ang/2)
        xs.append(_x)
        ys.append(_y)

        _x = xs[0]
        _y = ys[0]
        xs.append(_x)
        ys.append(_y)

        ax.plot(xs, ys, color='black', )

    @property
    def n(self):
        coords = [[0,], [0, ]]
        coords = self.components.moveto_foot_serif(*coords)
        coords = self.components.foot_serif(*coords)
        coords = self.components.upper_left_shoulder_serif(*coords)
        coords = self.components.upper_right_shoulder(*coords)
        coords = self.components.foot_serif(*coords)
        coords = self.components.upper_counter(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords)]

    @property
    def o(self):
        coords = [[0,], [0, ], ]
        coords = self.components.moveto_lower_bowl(*coords)
        coords = self.components.lower_bowl(*coords)
        coords = self.components.upper_bowl(*coords)
        return [self.zero(coords), self.components.counter()]

    @property
    def v(self):
        coords = [[0,], [0, ], ]
        coords = self.components.moveto_lower_bowl(*coords)
        coords = self.components.lower_bowl(*coords)
        coords = self.components.upper_left_serif(*coords)
        coords = self.components.lower_counter(*coords)
        coords = self.components.upper_left_serif(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords)]