# -*- coding: utf-8 -*-
from math import cos, tan, sin, atan, degrees
from math import pi as math_pi
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Glyph(ComponentGroup):
    def __init__(self, *args):
        super(Glyph, self).__init__(*args)

    def moveto_e_eye_counter(self):
        _a = self.si + self.rhs - self.s  # width of eye
        _b = (_a - 2 * self.r * sin(self.phs) -
              20 / cos(self.phs))
        return [self.s,
                self.height - (self.rhs * tan(self.phs) + _a / tan(self.phs)) + 20 / sin(self.phs)]

    @property
    def d_ascent(self):
        a = atan(self.ascent / (2 * self.s + self.c))
        _xx = self.s + self.c + 2 * self.r * sin(a)
        return Component(np.array([
            [[1, 0],
             [0, self.height]],
            [[-1, 2 * self.s + self.c],
             [1, (2 * self.s + self.c) * tan(a)]],
            [[-1, 2 * self.r * sin(a)],
             [-1, 2 * self.r * cos(a)]],
            [[1, _xx],
             [-1, _xx * tan(a)]],
        ]))

    @property
    def d_bowl(self):
        a = atan(self.ascent / (2 * self.s + self.c))
        _xx = self.s + self.c + 2 * self.r * sin(a)
        return Component(np.array([
            [[1, 0],
             [0, self.height + self.ascent - 2 * self.r * cos(a) -
              _xx * tan(a)]],
            [[-1, self.s],
             [-1, self.s * tan(self.th)]]
        ]))

    @property
    def e_eye(self):
        _a = self.si + self.rhs - self.s  # width of eye
        _b = (_a - 2 * self.r * sin(self.phs) -
              20 / cos(self.phs))
        return Component(np.array([
            [[1, 0],
             [0, self.height - (self.rhs * tan(self.phs) + _a / tan(self.phs))]],
            [[1, _a],
             [1, _a / tan(self.phs)]],
            [[-1, self.rhs],
             [1, self.rhs * tan(self.phs)]],
        ]))

    @property
    def e_eye_counter(self):
        _a = self.si + self.rhs - self.s  # width of eye
        _b = (_a - 2 * self.r * sin(self.phs) -
              20 / cos(self.phs))
        return Component(np.array([
            [[0, self.s],
             [0, self.height - (self.rhs * tan(self.phs) + _a / tan(self.phs)) + 20 / sin(self.phs)]],
            [[1, 0],
             [1, _b / tan(self.phs) + _b * tan(self.phs)]],
            [[1, _b],
             [-1, _b * tan(self.phs)]],
        ]))

    @property
    def h_shoulder(self):
        #TODO: Base shoulder on width of NW crotch in n
        return Component(np.array([
            [[-1, self.si - self.s],
             [-1, (self.si - self.s) * tan(self.th)]],
        ]))

    @property
    def m_shoulder(self):
        e = 2 * self.r * sin(self.ph) + self.eta[0] + self.eta[1] - self.c * self.nl
        _w = (3 * self.s + 2 * self.c) - e - (2 * self.s + self.c - self.si)
        _xx = _w / (1 + tan(self.th) / tan(self.ph))

        return Component(np.array([
            [[-1, _xx],
             [-1, _xx * tan(self.th)]],
            [[-1, (_w - _xx)],
             [1, (_w - _xx) * tan(self.ph)]],

        ]))

    @property
    def p_bowl(self):
        _xx = self.s + self.c - self.si
        return Component(np.array([
            [[1, 0],
             [0, _xx * tan(self.ph)]],
            [[1, _xx],
             [-1, _xx * tan(self.ph)]],
            [[1, self.si],
             [1, self.si * tan(self.th)]],
            [[1, 0],
             [0, self.height - self.rh * tan(self.ph)]],
        ]))

    @property
    def w_bowl(self):
        _w = (3 * self.s + 2 * self.c) - (self.si + self.rh)
        _xx = _w / (1 + tan(self.th) / tan(self.ph))
        return Component([
            [[1, 0],
             [0, self.rh * tan(self.ph)]],
            [[1, self.rh],
             [0, 0]],
            [[1, _xx],
             [1, _xx * tan(self.th)]],
            [[1, _w - _xx],
             [0, 0]],
            [[1, self.si],
             [1, self.si * tan(self.th)]],

        ])