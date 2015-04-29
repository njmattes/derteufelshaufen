# -*- coding: utf-8 -*-
from math import cos, tan, sin
from math import pi as math_pi
import numpy as np
from textura.components.component import Component
from textura.components.groups import ComponentGroup


class Finial(ComponentGroup):
    def __init__(self, *args):
        super(Finial, self).__init__(*args)

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
        #TODO: phi is rotated 90 degrees
        cn = self.c * self.nf
        phi = (math_pi / 2 - self.ph) * self.nf ** 2
        rho = self.s + cn + 2 * self.r * cos(phi) - self.si
        return Component(np.array([
            # [[ 1, 0],
            #  [ 0, self.height - self.si * tan(self.th)]],
            # [[ 1, self.si],
            #  [ 1, self.si * tan(self.th)]],
            [[ 1, rho],
             [-1, rho / tan(phi)]],
            [[-1, 2 * self.r * cos(phi)],
             [-1, 2 * self.r * sin(phi)]],
            [[-1, cn],
             [ 1, cn / tan(phi)]]
        ]))

    @property
    def lower_finial(self):
        cn = self.c * self.nf * .9
        phi = (math_pi / 2 - self.ph) * self.nf *.9
        rho = self.s + cn + 2 * self.r * cos(phi) - self.si
        _xx = rho + self.si - 2 * self.r * sin(self.ph / 2)
        return Component(np.array([
            [[ 1, 0],
             [ 0, (self.si + rho - self.s) * tan(self.ph / 2) + 2 * self.r * cos(self.ph / 2)]],
            [[ 1, self.si + rho - self.s],
             [-1, (self.si + rho - self.s) * tan(self.ph / 2)]],
            [[-1, 2 * self.r * sin(self.ph / 2)],
             [-1, 2 * self.r * cos(self.ph / 2)]],
            [[-1, _xx],
              [1, _xx * tan(self.ph / 2)]],
        ]))

