# -*- coding: utf-8 -*-
from math import tan
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Counter(ComponentGroup):
    def __init__(self, *args):
        super(Counter, self).__init__(*args)

    def moveto_lower_counter(self):
        return [self.s,
                self.si * tan(self.th) + self.pinch_y + self.c * tan(self.ph)]

    @property
    def upper_counter(self):
        return Component(np.array([
            [[1, 0],
             [0, self.height - (self.si * tan(self.th) + self.pinch_y)]],
            [[1, self.c],
             [-1, self.c * tan(self.ph)]]
        ]))

    @property
    def lower_counter(self):
        return Component([
            [[1, 0],
             [0, self.si * tan(self.th) + self.pinch_y]],
            [[-1, self.c],
             [1, self.c * tan(self.ph)]]
        ])

    @property
    def counter(self):
        #Starts in bottom left from moveto_lower_counter()
        return Component(np.array([
            [[1, 0],
             [0, self.height - (self.si * tan(self.th) + self.pinch_y)]],
            [[1, self.c],
             [-1, self.c * tan(self.ph)]],
            [[1, 0],
             [0, self.si * tan(self.th) + self.pinch_y]],
        ]))