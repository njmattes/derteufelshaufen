# -*- coding: utf-8 -*-
from math import tan
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Extender(ComponentGroup):
    def __init__(self, *args):
        super(Extender, self).__init__(*args)

    def moveto_ascender(self):
        return [0, self.height + self.ascent - self.s * tan(self.th)]

    def moveto_descender(self):
        return [0, -self.descent]

    @property
    def lineto_ascender(self):
        return Component(np.array([
            [[1, 0],
             [0, self.height + self.ascent - self.s * tan(self.th)]]
        ]))

    @property
    def lineto_ascent_apex(self):
        return Component(np.array([
            [[1, 0],
             [0, self.height + self.ascent - self.si * tan(self.th)]],
            [[1, self.si],
             [1, self.si * tan(self.th)]],
        ]))

    @property
    def ascender(self):
        return Component([
            [[1, 0],
             [0, self.height + self.ascent]],
            [[-1, self.s],
             [-1, self.s * tan(self.th)]],
        ])

    @property
    def descender(self):
        return Component([
            [[1, 0],
             [0, -self.descent]],
            [[1, self.s],
             [1, self.s * tan(self.th)]],
        ])

