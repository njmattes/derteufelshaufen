# -*- coding: utf-8 -*-
from math import tan
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Bowl(ComponentGroup):
    def __init__(self, *args):
        super(Bowl, self).__init__(*args)

    def moveto_lower_bowl(self):
        return [self.s * 2 + self.c,
                self.si * tan(self.th),]

    def moveto_upper_bowl(self):
        return [0,
                self.height - self.si * tan(self.th)]

    @property
    def lineto_upper_bowl_apex(self):
        return Component(np.array([
            [[1, 0],
             [0, self.height - self.si * tan(self.th)]],
            [[1, self.si],
             [1, self.si * tan(self.th)]],
        ]))

    @property
    def lower_bowl(self):
        _xx = (self.s * 2 + self.c) - self.si
        return Component([
            [[1, 0],
             [0, self.si*tan(self.th)]],
            [[-1, self.si],
             [-1, self.si * tan(self.th)]],
            [[-1, _xx],
             [1, _xx * tan(self.ph)]]
        ])

    @property
    def upper_bowl(self):
        _xx = (self.s * 2 + self.c) - self.si
        return Component(np.array([
            [[1, 0],
             [0, self.height - self.si * tan(self.th)]],
            [[1, self.si],
             [1, self.si * tan(self.th)]],
            [[1, _xx],
             [-1, _xx * tan(self.ph)]]
        ]))

