# -*- coding: utf-8 -*-
import numpy as np
from __future__ import division


class Contour(object):
    def __init__(self, components, start, ccw=True):
        self._components = components
        self._start = start
        self.ccw = ccw

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        self._components = value

    @property
    def start(self):
        if self._start is None:
            self._start = [0, 0]
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def coords(self):
        coords = [self.start, ]
        for component in self.components:
            for c in component.coords:
                signs = [1 if c[0][0] >= 0 else -1,
                         1 if c[1][0] >= 0 else -1]
                coords.append([
                    coords[-1][0] * abs(c[0][0]) + signs[0] * c[0][1],
                    coords[-1][1] * abs(c[1][0]) + signs[1] * c[1][1],])
        coords.append(coords[0])
        if self.ccw:
            coords.reverse()
        return np.array(coords)

    @property
    def xs(self):
        return self.coords[:,0]

    @property
    def ys(self):
        return self.coords[:,1]

    @property
    def area(self):
        xs = self.coords[:,0]
        ys = self.coords[:,1]
        a = 0
        for i in range(len(self.coords)):
            a += xs[i-1] * ys[i] - xs[i] * ys[i-1]
        return a / 2

    @property
    def centroid(self):
        xs = self.coords[:,0]
        ys = self.coords[:,1]
        xy = np.array([0, 0])
        for i in range(len(self.coords)):
            d = xs[i-1] * ys[i] - xs[i] * ys[i-1]
            xy += np.array([(self.xs[i-1] + self.xs[i]) * d,
                            (self.ys[i-1] + self.ys[i]) * d])
        return 1 / 6 * xy / self.area

    @property
    def inertia_x(self):
        coords = self.coords - self.centroid
        xs = coords[:,0]
        ys = coords[:,1]
        ix = 0
        for i in range(len(self.coords)):
            d = xs[i-1] * ys[i] - xs[i] * ys[i-1]
            ix += (xs[i-1] ** 2 + xs[i] * xs[i-1] + xs[i] ** 2) * d
        return 1 / 12 * ix / self.area

    @property
    def inertia_y(self):
        coords = self.coords - self.centroid
        xs = coords[:,0]
        ys = coords[:,1]
        iy = 0
        for i in range(len(self.coords)):
            d = xs[i-1] * ys[i] - xs[i] * ys[i-1]
            iy += (ys[i-1] ** 2 + ys[i] * ys[i-1] + ys[i] ** 2) * d
        return 1 / 12 * iy / self.area

    @property
    def inertia_xy(self):
        coords = self.coords - self.centroid
        xs = coords[:,0]
        ys = coords[:,1]
        ixy = 0
        for i in range(len(self.coords)):
            d = xs[i-1] * ys[i] - xs[i] * ys[i-1]
            ixy += (2 * self.xs[i-1] * self.ys[i-1] +
                    self.xs[i] * self.ys[i-1] +
                    self.ys[i] * self.xs[i-1] +
                    2 * self.xs[i] * self.ys[i]) * d
        return 1 / 24 * ixy / self.area

