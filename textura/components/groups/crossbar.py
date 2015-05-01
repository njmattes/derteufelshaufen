# -*- coding: utf-8 -*-
from math import tan, cos
from math import pi as math_pi
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Crossbar(ComponentGroup):
    def __init__(self, *args):
        super(Crossbar, self).__init__(*args)

    @property
    def left_crossbar(self):
        h = 20
        w = self.c / 2
        a = math_pi / 2 - self.ph
        return Component([
            [[1, 0],
             [0, self.height - h]],
            [[-1, w * (1 + cos(a))],
             [1, 0]],
            [[1, w * cos(a)],
             [1, h]],
            [[1, w],
             [1, 0]],
        ])

    @property
    def right_crossbar(self):
        h = 20
        w = self.c / 2
        a = math_pi / 2 - self.ph
        return Component([
            [[1, 0],
             [0, self.height]],
            [[1, w * (1 + cos(a))],
             [1, 0]],
            [[-1, w * cos(a)],
             [1, h]],
            [[-1, w],
             [1, 0]],
        ])