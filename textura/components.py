# -*- coding: utf-8 -*-
from __future__ import division
from math import cos, tan, sin


class Components(object):

    def __init__(self, construction):
        self.height = 700
        self.ascent = 200
        self.n = .5
        self.nl = .5
        self.nr = .5
        self.s = construction.s
        self.c = construction.c
        self.o = construction.overlap
        self.r = construction.r
        self.th = construction.theta
        self.ph = construction.phi
        self.phs = construction.phi_steep
        self.pi = construction.pi
        self.si = construction.sigma

    def moveto_lower_bowl(self, xs, ys):
        ys[-1] = self.si * tan(self.th)
        return xs, ys

    def moveto_foot_serif(self, xs, ys):
        ys[-1] = (tan(self.ph) * self.c * self.n + 2 * self.r * cos(self.ph))
        return xs, ys

    def moveto_ascender(self, xs, ys):
        ys[-1] = self.height + self.ascent - self.s * tan(self.th)
        return xs, ys

    def ascender(self, xs, ys):
        _x = xs[-1]
        _y = self.height + self.ascent - self.s * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x += self.s
        _y += self.s * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_left_serif(self, xs, ys):
        a = self.ph
        cn = self.c * self.nl

        _x = xs[-1]
        _y = self.height - 2 * self.r * cos(a) - cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x -= cn
        _y += cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * self.r * sin(a)
        _y += 2 * self.r * cos(a)
        xs.append(_x)
        ys.append(_y)

        _xx = self.s + cn - 2 * self.r * sin(a)
        _x += _xx
        _y -= _xx * tan(a)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_left_shoulder_serif(self, xs, ys):
        a = self.ph
        cn = self.c * self.nl

        _x = xs[-1]
        _y = self.height - 2 * self.r * cos(a) - cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x -= cn
        _y += cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * self.r * sin(a)
        _y += 2 * self.r * cos(a)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.si * tan(self.th) - (2 * self.r * sin(a) - cn) * tan(a))
        _xx /= (tan(a) + tan(self.th))
        _x += _xx
        _y -= tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        _x += self.si - (_xx + 2 * self.r * sin(a) - cn) # /
        _y += tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_right_shoulder(self, xs, ys):
        a = self.ph
        cn = self.c * self.nl

        _x = xs[-1]
        _y = ys[-1]
        # \
        _xx = 2 * self.s + self.c - self.si
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
        a = self.ph
        cn = self.c * self.nl

        _x = xs[-1]
        _y = tan(self.ph) * self.c * self.n + \
             2 * self.r * cos(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x = xs[-1] + cn
        _y = 2 * self.r * cos(a)
        xs.append(_x)
        ys.append(_y)
        # /
        _x -= 2 * self.r * sin(a)
        _y = 0
        xs.append(_x)
        ys.append(_y)
        # \
        _xx = (self.s + cn) - 2 * self.r * sin(a)
        _x -= _xx
        _y += tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_left_serif(self, xs, ys):
        a = self.ph
        cn = self.c * self.nl

    def upper_counter(self, xs, ys):
        _x = xs[-1]

        _y = self.height - self.si * tan(self.th)
        _y -= (self.s - self.o - self.o * tan(self.th) / tan(self.ph)) * tan(self.ph)
        _y -= (self.s + self.c - self.o) * tan(self.ph)# _y -= (self.s * 2 + self.c - self.o - 2 * self.r -
        #     self.r * (1 - sin(self.ph))) * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x -= self.c
        _y += self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_counter(self, xs, ys):
        _x = xs[-1]

        _y = self.si * tan(self.th)
        _y += (self.s + self.c - self.o) * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x += self.c
        _y -= self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def counter(self):

        xs = []
        ys = []

        _x = self.s + self.c
        _y = self.height - self.si * tan(self.th)
        _y -= (self.s - self.o - self.o * tan(self.th) / tan(self.ph)) * tan(self.ph)
        _y -= (self.s + self.c - self.o) * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x -= self.c
        _y += self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _y = self.si * tan(self.th)
        _y += (self.s - self.o - self.o * tan(self.th) / tan(self.ph)) * tan(self.ph)
        _y += (self.s + self.c - self.o) * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x += self.c
        _y -= self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        xs.append(xs[0])
        ys.append(ys[0])

        return xs, ys

    def lower_bowl(self, xs, ys):
        _x = xs[-1]
        _y = self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x -= self.si
        _y -= self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.s * 2 + self.c) - self.si
        _x -= _xx
        _y += _xx * tan(self.ph)
        xs.append(_x)
        ys.append(_y)
        return xs, ys

    def upper_bowl(self, xs, ys):
        _x = xs[-1]
        _y = self.height - self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x += self.si
        _y += self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.s * 2 + self.c) - self.si
        _x += _xx
        _y -= _xx * tan(self.ph)
        xs.append(_x)
        ys.append(_y)
        return xs, ys