# -*- coding: utf-8 -*-
from math import cos, tan, sin
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Finial(ComponentGroup):
    def __init__(self, *args):
        super(Finial, self).__init__(*args)

    def moveto_lower_finial(self):
        a = (self.si + self.rhs) * self.finial_scale_factor
        _xx = a - 2 * self.r * sin(self.ph / 2)
        return [0, _xx * tan(self.ph / 2)]

    @property
    def finial_scale_factor(self):
        e = ((sin(self.phs) * cos(self.phs) -
              sin(self.ph / 2) * cos(self.ph / 2)) /
             2 * cos(self.ph))
        r = self.r * 2 * e
        return (self.si + self.rhs - r) / (self.si + self.rhs)


    @property
    def upper_finial(self):
        """ /`\
             \/
        :param xs:
        :type xs:
        :param ys:
        :type ys:
        :return:
        :rtype:
        """
        cn = self.c * self.nf
        return Component(np.array([
            [[1, 0],
             [0, self.height - (self.rhs * tan(self.phs) +
                                2 * self.r * cos(self.phs) -
                                cn * tan(self.phs))]],
            [[1, cn],
             [-1, cn * tan(self.phs)]],
            [[1, 2 * self.r * sin(self.phs)],
             [1, 2 * self.r * cos(self.phs)]],
            [[-1, self.rhs],
             [1, self.rhs * tan(self.phs)]],
        ]))

    @property
    def lower_finial(self):
        a = (self.si + self.rhs) * self.finial_scale_factor
        _xx = a - 2 * self.r * sin(self.ph / 2)
        return Component(np.array([
            [[1, 0],
             [0, _xx * tan(self.ph / 2)]],
            [[1, _xx],
             [-1, _xx * tan(self.ph / 2)]],
            [[1, 2 * self.r * sin(self.ph / 2)],
             [1, 2 * self.r * cos(self.ph / 2)]],
            [[-1, a - self.s],
             [1, (a - self.s) * tan(self.ph / 2)]],
        ]))

