#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from math import tan, atan2, sin, cos, sqrt, radians, degrees
from math import pi as math_pi
import matplotlib.pyplot as plt


class Constructor(object):
    def __init__(self, stem, counter, theta, radius=None, x=None):
        self.stem = stem
        self.counter = float(counter)
        self._theta = radians(float(theta))
        self._radius = radius
        self._x = x
        self._psi = None
        self._pi = None
        self.height = 700
        self.ascent = 200
        self.n = .5
        self.nl = .5
        self.nr = .5

    @property
    def theta(self):
        """Angle of top left corner of o (of pen when drawing stems).
        :return: Number in degrees
        :rtype: float
        """
        return self._theta

    @theta.setter
    def theta(self, value):
        self._theta = value
        self._psi = None

    @property
    def pi(self):
        if self._pi is None:
            pi = self.sigma * tan(self.theta)
            pi -= (2 * self.radius * sin(self.phi) - self.counter * self.n)
            pi *= tan(self.phi)
            pi /= (tan(self.phi) + tan(self.theta))
            self._pi = pi
        return self._pi


    @property
    def radius(self):
        """Radius of circle in top right.
        Determines contrast of letterforms. Maximum value should be half
        of stem width. The lower the value the higher the contrast.
        :return: Number in UPM
        :rtype: float
        """
        if self._radius is None:
            self._radius = self.stem / 2
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._psi = None

    @property
    def x(self):
        """Overlap coefficient. Defaults to 0.
        x_range[] <= x <= x_range[1].
        :return:
        :rtype:
        """
        if self._x is None:
            self._x = self.x_range[1]
            # self._x = 0
            # self._x = (self.x_range[0] + self.x_range[1]) / 2
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def rise(self):
        return self.stem * tan(self.theta)

    @property
    def offset(self): 
        return max(0, self.radius - self.rise)

    @property
    def x_range(self):
        return [-(self.radius + self.offset) / tan(self.theta),
                self.stem]

    @property
    def a(self):
        return self.x * tan(self.theta)

    @property
    def phi(self):
        if self._psi is None:
            b = self.stem + self.counter + self.radius + (
                self.stem - 2 * self.radius) - self.x
            c = sqrt(self.a ** 2 + b ** 2)
            _psi = atan2(self.a, b)
            b = sqrt(c ** 2 - self.radius ** 2)
            _psi += atan2(self.radius, b)
            self._psi = _psi
        return self._psi

    @property
    def sigma(self):
        sigma = (
            self.radius * (cos(self.phi) - tan(self.phi) +
                           tan(self.phi) * sin(self.phi)) -
            (self.stem * 2 + self.counter) * tan(self.theta) -
                self.offset) / (
            tan(self.theta) + tan(self.phi)
        )
        sigma += (self.stem * 2 + self.counter)
        # sigma += self.radius * cos(self.psi) - self.offset
        # sigma -= self.radius * (1 - sin(self.psi)) * tan(self.psi)
        ## sigma /= tan(self.theta) + tan(self.psi)
        return sigma

    def draw_o(self, ax):
        height = 700
        _y = self.stem + self.counter + (self.stem - self.radius)
        _y += self.offset / tan(self.theta)
        _y *= sin(self.theta) * sin(self.phi)
        _y /= sin(2 * math_pi - self.theta - self.phi)
        _y -= self.offset
        _x = _y / tan(self.theta)
        xl = _x + (_x - self.x)
        yl = xl * tan(self.theta)
        xr = 2 * self.stem + self.counter - xl
        # yr = yl - tan(self.psi) * (xr - xl)
        yr = tan(self.phi) * (xr)
        x = [0, 0, 0, 0, 0, 0, 0]
        y = [0, 0, 0, 0, 0, 0, 0]
        x[0] = 0
        y[0] = height - yl
        x[1] = xl
        y[1] = height
        x[2] = 2 * self.stem + self.counter
        y[2] = height - yr
        x[3] = 2 * self.stem + self.counter
        y[3] = yl
        x[4] = xr
        y[4] = 0
        x[5] = 0
        y[5] = yr
        # x[6] = x[0]
        # y[6] = y[0]

        xi = [0, 0, 0, 0, 0, ]
        yi = [0, 0, 0, 0, 0, ]
        xi[0] = self.stem
        yil = (self.a - self.offset) - tan(self.phi) * (self.stem - self.x)
        yir = yil - tan(self.phi) * self.counter
        yi[0] = height - yl + yil
        xi[1] = self.stem + self.counter
        yi[1] = yi[0] - tan(self.phi) * self.counter
        xi[2] = xi[1]
        yi[2] = yl - yil
        xi[3] = xi[0]
        yi[3] = yl - yir
        xi[4] = xi[0]
        yi[4] = yi[0]

        ax.plot(x, y, color='black', )
        ax.plot(xi, yi, color='black', )

    def draw_o2(self, ax):
        theta = self.theta
        phi = self.phi
        s = self.stem
        c = self.counter
        n = .5
        nr = .5
        r = self.radius
        # α ν β ξ γ δ π ε ρ
        sigma = self.sigma
        height = 700
        xs = []
        ys = []

        _x = 0
        _y = 0
        xs.append(0); ys.append(0)

        _xx = 2 * s + c - sigma

        _x -= _xx
        _y += _xx * tan(phi)
        xs.append(_x)
        ys.append(_y)

        _y = height - sigma * tan(theta)
        xs.append(_x)
        ys.append(_y)

        _x += sigma
        _y = height
        xs.append(_x)
        ys.append(_y)

        _x += _xx
        _y = height - _xx * tan(phi)
        xs.append(_x)
        ys.append(_y)

        _y = sigma * tan(theta)
        xs.append(_x)
        ys.append(_y)

        xs.append(xs[0]); ys.append(ys[0])

        ax.plot(xs, ys, color='black', )

        xs = []
        ys = []

        _x = s - _xx
        _y = 2 * r * (cos(phi) - tan(phi) + tan(phi) * sin(phi)) + _xx * tan(phi)
        xs.append(_x)
        ys.append(_y)

        _y = height - (_y - c * tan(phi))
        xs.append(_x)
        ys.append(_y)

        _x += c
        _y -= c * tan(phi)
        xs.append(_x)
        ys.append(_y)

        _y = 2 * r * (cos(phi) - tan(phi) + tan(phi) * sin(phi)) + _xx * tan(phi) - c * tan(phi)
        xs.append(_x)
        ys.append(_y)

        xs.append(xs[0])
        ys.append(ys[0])

        ax.plot(xs, ys, color='black', )

        # xi = [0, 0, 0, 0, 0, ]
        # yi = [0, 0, 0, 0, 0, ]
        # xi[0] = self.stem
        # yil = (self.a - self.offset) - tan(self.psi) * (self.stem - self.x)
        # yir = yil - tan(self.psi) * self.counter
        # print yl, yil, yir
        # yi[0] = height - yl + yil
        # xi[1] = self.stem + self.counter
        # yi[1] = yi[0] - tan(self.psi) * self.counter
        # xi[2] = xi[1]
        # yi[2] = yl - yil
        # xi[3] = xi[0]
        # yi[3] = yl - yir
        # xi[4] = xi[0]
        # yi[4] = yi[0]

    def draw_n3(self, ax):
        theta = self.theta
        phi = self.phi
        s = self.stem
        c = self.counter
        n = .5
        nr = .5
        r = self.radius
        sigma = self.sigma
        height = 700
        xs = []
        ys = []

        _x = 0; _y = 0
        xs.append(_x)
        ys.append(_y)

        _x -= (s + c * n) - (2 * r * sin(phi))
        _y -= _x * tan(phi)
        xs.append(_x)
        ys.append(_y)

        _ang = phi
        _xx = c * nr

        _y = height - 2 * r * cos(_ang) - _xx * tan(_ang)
        xs.append(_x)
        ys.append(_y)

        _x -= _xx
        _y += _xx * tan(_ang)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * r * sin(_ang)
        _y += 2 * r * cos(_ang)
        xs.append(_x)
        ys.append(_y)

        _xx = (sigma * tan(theta) - (2 * r * sin(_ang) - _xx) * tan(_ang))
        _xx /= (tan(_ang) + tan(theta))
        # _xx += (2 * r * sin(_ang) + c * nr)
        _x += _xx
        # _x += _xx
        _y -= tan(_ang) * _xx
        xs.append(_x)
        ys.append(_y)

        _x += sigma - (_xx + 2 * r * sin(_ang) - c * nr) # /
        _y += tan(phi) * _xx
        xs.append(_x)
        ys.append(_y)

        _x += (2 * s + c) - sigma # \
        _y -= tan(phi) * ((2 * s + c) - sigma)
        xs.append(_x)
        ys.append(_y)

        _y = tan(phi) * c * nr + 2 * r * cos(phi) # |
        xs.append(_x)
        ys.append(_y)

        _x += c * nr
        _y = 2 * r * cos(phi)
        xs.append(_x)
        ys.append(_y)

        _x -= 2 * r * sin(phi)
        _y = 0
        xs.append(_x)
        ys.append(_y)

        _xx = (s + c * nr) - 2 * r * sin(phi)
        _x -= _xx
        _y += tan(phi) * _xx
        xs.append(_x)
        ys.append(_y)

        _y = height - sigma * tan(theta)
        _y -= (s + c - self.x) * tan(phi) - tan(theta) * self.x
        xs.append(_x)
        ys.append(_y)

        _x -= c
        _y += tan(phi) * c
        xs.append(_x)
        ys.append(_y)

        _y = tan(phi) * c * n + 2 * r * cos(phi)
        xs.append(_x)
        ys.append(_y)

        _x += c * n
        _y -= c * n * tan(phi)
        xs.append(_x)
        ys.append(_y)

        _x = xs[0]
        _y = ys[0]
        xs.append(_x)
        ys.append(_y)

        ax.plot(xs, ys, color='black', )

    def draw_c(self, ax):
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

    def ascender(self, xs, ys):
        _x = xs[-1]
        _y = self.height + self.ascent - self.stem * tan(self.theta)
        xs.append(_x)
        ys.append(_y)

        _x += self.stem
        _y += self.stem * tan(self.theta)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_left_serif(self, xs, ys):
        a = self.phi
        cn = self.counter * self.nl

        _x = xs[-1]
        _y = self.height - 2 * self.radius * cos(a) - cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x -= cn
        _y += cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * self.radius * sin(a)
        _y += 2 * self.radius * cos(a)
        xs.append(_x)
        ys.append(_y)

        _xx = self.stem + cn - 2 * self.radius * sin(a)
        _x += _xx
        _y -= _xx * tan(a)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_left_shoulder_serif(self, xs, ys):
        a = self.phi
        cn = self.counter * self.nl

        _x = xs[-1]
        _y = self.height - 2 * self.radius * cos(a) - cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x -= cn
        _y += cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * self.radius * sin(a)
        _y += 2 * self.radius * cos(a)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.sigma * tan(self.theta) - (2 * self.radius * sin(a) - cn) * tan(a))
        _xx /= (tan(a) + tan(self.theta))
        _x += _xx
        _y -= tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        _x += self.sigma - (_xx + 2 * self.radius * sin(a) - cn) # /
        _y += tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_right_shoulder(self, xs, ys):
        a = self.phi
        cn = self.counter * self.nl

        _x = xs[-1]
        _y = ys[-1]
        # \
        _xx = 2 * self.stem + self.counter - self.sigma
        _x += _xx
        _y -= tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def foot_serif(self, xs, ys):
        """Draws three (six) strokes that make up a foot serif.
        Assumes vertical entry.
        Proceeds SE, SW, NW.
        :param xs: current x coords
        :param ys: current y coords
        :return: xs, ys
        :rtype: tuple
        """
        a = self.phi
        cn = self.counter * self.nl

        _x = xs[-1]
        _y = tan(self.phi) * self.counter * self.n + \
             2 * self.radius * cos(self.phi)
        xs.append(_x)
        ys.append(_y)

        _x = xs[-1] + cn
        _y = 2 * self.radius * cos(a)
        xs.append(_x)
        ys.append(_y)
        # /
        _x -= 2 * self.radius * sin(a)
        _y = 0
        xs.append(_x)
        ys.append(_y)
        # \
        _xx = (self.stem + cn) - 2 * self.radius * sin(a)
        _x -= _xx
        _y += tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_left_serif(self, xs, ys):
        a = self.phi
        cn = self.counter * self.nl

    def upper_counter(self, xs, ys):
        _x = xs[-1]

        _y = self.height - self.sigma * tan(self.theta)
        _y -= (self.stem + self.counter - self.x) * tan(self.phi)
        # _y -= tan(self.theta) * self.x
        xs.append(_x)
        ys.append(_y)

        _x -= self.counter
        _y += self.counter * tan(self.phi)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_counter(self, xs, ys):
        _x = xs[-1]

        _y = self.sigma * tan(self.theta)
        _y += (self.stem + self.counter - self.x) * tan(self.phi)
        xs.append(_x)
        ys.append(_y)

        _x += self.counter
        _y -= self.counter * tan(self.phi)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_bowl(self, xs, ys):
        _x = xs[-1]
        _y = self.sigma * tan(self.theta)
        xs.append(_x)
        ys.append(_y)

        _x -= self.sigma
        _y -= self.sigma * tan(self.theta)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.stem * 2 + self.counter) - self.sigma
        _x -= _xx
        _y += _xx * tan(self.phi)
        xs.append(_x)
        ys.append(_y)
        return xs, ys

    def draw_n(self, ax):
        coords = ([0,],
                  [tan(self.phi) * self.counter * self.n +
                   2 * self.radius * cos(self.phi), ])
        coords = self.foot_serif(*coords)
        coords = self.upper_left_shoulder_serif(*coords)
        coords = self.upper_right_shoulder(*coords)
        coords = self.foot_serif(*coords)
        coords = self.upper_counter(*coords)

        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        ax.plot(coords[0], coords[1], color='black', )

    def draw_b(self, ax):
        coords = [[0, ],
                  [self.sigma * tan(self.theta)]]
        coords = self.lower_bowl(*coords)
        coords = self.ascender(*coords)
        coords = self.lower_counter(*coords)
        coords = self.upper_left_serif(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        ax.plot(coords[0], coords[1], color='black', )




if __name__ == '__main__':
    plt.figure(figsize=(15, 8))

    x = Constructor(20, 100, 30, radius=9, x=15)
    ax = plt.subplot(231, aspect='equal')
    x.draw_b(ax)
    ax = plt.subplot(234, aspect='equal')
    x.draw_c(ax)
    x = Constructor(75, 100, 45, radius=35, x=30)
    ax = plt.subplot(232, aspect='equal')
    x.draw_b(ax)
    ax = plt.subplot(235, aspect='equal')
    x.draw_c(ax)
    x = Constructor(200, 100, 20, radius=90, x=150)
    ax = plt.subplot(233, aspect='equal')
    x.draw_b(ax)
    ax = plt.subplot(236, aspect='equal')
    x.draw_c(ax)

    plt.show()
