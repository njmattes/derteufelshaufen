# -*- coding: utf-8 -*-
from math import cos, tan, sin
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Shoulder(ComponentGroup):
    def __init__(self, *args):
        super(Shoulder, self).__init__(*args)

    @property
    def upper_left_shoulder(self):
        cn = self.c * self.nl
        return Component(np.array([
            [[1, 0],
             [0, self.height - 2 * self.r * cos(self.ph) - cn * tan(self.ph)]],
            [[-1, cn],
             [1, cn * tan(self.ph)]],
            [[1, 2 * self.r * sin(self.ph)],
             [1, 2 * self.r * cos(self.ph)]],
            [[1, self.eta[0]],
             [-1, self.eta[0] * tan(self.ph)]],
            [[1, self.eta[1]],
             [1, self.eta[1] * tan(self.th)]],
        ]))

    @property
    def lower_left_shoulder(self):
        _xx = 2 * self.s + self.c - self.si
        return Component(np.array([
            [[1, _xx],
             [-1, _xx * tan(self.ph)]]
        ]))

    @property
    def upper_right_shoulder(self):
        _xx = 2 * self.s + self.c - self.si
        return Component(np.array([
            [[-1, _xx],
             [1, _xx * tan(self.ph)]],
        ]))