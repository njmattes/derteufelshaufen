#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import tan, cos, sin
from math import pi as math_pi
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Mark(ComponentGroup):
    def __init__(self, *args):
        super(Mark, self).__init__(*args)

    def moveto_tittle(self):
        w = 2 * self.r * sin(self.ph) + self.s
        h = self.s * tan(self.ph) + 2 * self.r * cos(self.ph)
        y = self.height + 10 if h >= self.ascent else self.height + self.ascent - h
        return [0 - 2 * self.r * sin(self.ph) / 2, y]

    @property
    def tittle(self):
        return Component(np.array([
            [[-1, self.s],
             [1, self.s * tan(self.ph)]],
            [[1, 2 * self.r * sin(self.ph)],
             [1, 2 * self.r * cos(self.ph)]],
            [[1, self.s],
             [-1, self.s * tan(self.ph)]],
        ]))

