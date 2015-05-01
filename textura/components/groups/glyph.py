# -*- coding: utf-8 -*-
from math import cos, tan, sin, atan
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Glyph(ComponentGroup):
    def __init__(self, *args):
        super(Glyph, self).__init__(*args)

    @property
    def d_ascent(self):
        ang = atan((2 * self.s + self.c) / self.ascent)
        _xx = self.s + self.c + 2 * self.r * cos(ang)
        return Component(np.array([
            [[1, 0],
             [0, self.height + self.ascent - _xx / tan(ang) -
              2 * self.r * sin(ang)]],
            [[-1, _xx],
             [1, _xx / tan(ang)]],
            [[1, 2 * self.r * cos(ang)],
             [1, 2 * self.r * sin(ang)]],
            [[1, 2 * self.s + self.c],
             [-1, self.ascent]],
            [[1, 0],
             [0, self.si * tan(self.th)]],
        ]))

    @property
    def d_bowl(self):
        ang = atan((2 * self.s + self.c) / self.ascent)
        _xx = self.s + self.c + 2 * self.r * cos(ang)
        return Component(np.array([
            [[1, 0],
             [0, self.height + self.ascent - 2 * self.r * sin(ang) -
              _xx / tan(ang) - self.s * tan(self.th)]],
            [[1, self.s],
             [1, self.s * tan(self.th)]]
        ]))

    @property
    def p_bowl(self):
        _xx = self.s + self.c - self.si
        return Component(np.array([
            [[1, 0],
             [0, self.si * tan(self.th)]],
            [[-1, self.si],
             [-1, self.si * tan(self.th)]],
            [[-1, _xx],
             [1, _xx * tan(self.ph)]],
            [[1, 0],
             [-1, self.descent - self.s * tan(self.th)]],
            [[-1, self.s],
             [-1, self.s * tan(self.th)]],
        ]))

    @property
    def h_shoulder(self):
        #TODO: Base shoulder on width of NW crotch in n
        return Component(np.array([
            [[1, 0],
             [0, self.height - (self.si - self.s) * tan(self.th)]],
            [[1, self.si - self.s],
             [1, (self.si - self.s) * tan(self.th)]]
        ]))

    @property
    def e_eye(self):
        cn = self.c * self.nf
        return Component(np.array([
            [[1, self.rhs], # SE
             [-1, self.rhs * tan(self.phs)]],
            [[-1, self.si + self.rhs - self.s], # SW
             [-1, (self.si + self.rhs - self.s) * tan(self.rhs)]],
            [[1, 0], # N
             [1, 20 * cos(self.phs)]],
            [[], # NE
             []],
            [[], # NW
             []],

        ]))