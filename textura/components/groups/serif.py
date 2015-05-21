# -*- coding: utf-8 -*-
from math import cos, tan, sin
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Serif(ComponentGroup):
    def __init__(self, *args):
        super(Serif, self).__init__(*args)

    def moveto_foot_serif(self):
        return [0,
                (self.s + self.c * self.nr - 2 * self.r * sin(self.ph)) * tan(self.ph)]

    def moveto_upper_left_shoulder_serif(self):
        return [self.si,
                self.height]

    def moveto_upper_serif(self):
        return [self.s,
                self.height - (self.s + self.c * self.nr - 2 * self.r * sin(self.ph)) * tan(self.ph)]
                # self.height - (self.s + self.c * self.nl - 2 * self.r * sin(self.ph))]

    @property
    def upper_left_serif(self):
        cn = self.c * self.nl
        _xx = self.s + cn - 2 * self.r * sin(self.ph)
        return Component(np.array([
            [[1, 0],
             [0, self.height - (self.s + self.c * self.nr - 2 * self.r * sin(self.ph)) * tan(self.ph)]],
            [[-1, _xx],
             [1, _xx * tan(self.ph)]],
            [[-1, 2 * self.r * sin(self.ph)],
             [-1, 2 * self.r * cos(self.ph)]],
            [[1, cn],
             [-1, cn * tan(self.ph)]],

        ]))

    @property
    def foot_serif(self):
        """Draws three (six) strokes that make up a foot serif.
        Assumes vertical entry.
        Proceeds SE, SW, NW.
        :param xs: current x coords
        :param ys: current y coords
        :return: xs, ys
        :rtype: tuple
        """
        cn = self.c * self.nl
        _xx = (self.s + cn) - 2 * self.r * sin(self.ph)
        return Component(np.array([
            [[1, 0],
             [0, (self.s + self.c * self.nr - 2 * self.r * sin(self.ph)) * tan(self.ph)]],
            [[1, _xx],
             [-1, _xx * tan(self.ph)]],
            [[1, 2 * self.r * sin(self.ph)],
             [1, 2 * self.r * cos(self.ph)]],
            [[-1, cn],
             [1, cn * tan(self.ph)]],
        ]))

    @property
    def upper_left_shoulder_serif(self):
        cn = self.c * self.nl
        return Component(np.array([
            [[-1, self.eta[1]],
             [-1, self.eta[1] * tan(self.th)]],
            [[-1, self.eta[0]],
             [1, self.eta[0] * tan(self.ph)]],
            [[-1, 2 * self.r * sin(self.ph)],
             [-1, 2 * self.r * cos(self.ph)]],
            [[1, cn],
             [-1, cn * tan(self.ph)]],

        ]))

    @property
    def lower_right_shoulder_serif(self):
        cn = self.c * self.nl
        return Component(np.array([
            [[1, self.eta[1]],
             [1, self.eta[1] * tan(self.th)]],
            [[1, self.eta[0]],
             [0, 0]],
            [[1, 2 * self.r * sin(self.ph)],
             [1, 2 * self.r * cos(self.ph)]],
            [[-1, cn],
             [1, cn * tan(self.ph)]],
            # [[1, 0],
            #  [0, 2 * self.r * cos(self.ph) + cn * tan(self.ph)]],
        ]))