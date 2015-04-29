# -*- coding: utf-8 -*-
from __future__ import division
from math import radians
from textura.components import Components
from textura.construction import Construction
from textura.glyphs import Glyphs


class Font(object):
    def __init__(self, stem, counter, theta, radius=None, x=None, ):
        self.stem = stem
        self.counter = float(counter)
        self._theta = radians(float(theta))
        self._radius = radius
        self._phi = None
        self._pi = None
        self._phi_steep = None
        self.n = .5
        self.nl = .5
        self.nr = .5
        self.construction = Construction(self.stem, self.counter, self.radius,
                                         x, self.theta, )
        self.components = Components(self.construction)
        self.g = Glyphs(self.components)


    @property
    def theta(self):
        """Angle of top left corner of o (angle of 'pen' when drawing stems).
        :return: Angle in radians
        :rtype: float
        """
        return self._theta

    @theta.setter
    def theta(self, value):
        self._theta = value
        self._psi = None

    @property
    def radius(self):
        """Radius of circle in top right.
        Determines contrast of letterforms. Maximum value is half
        of stem width. The lower the value the higher the contrast.
        :return: Number in UPM
        :rtype: float
        """
        if self._radius is None:
            self._radius = self.stem / 2
        if self._radius * 2 > self.stem:
            raise Exception('Invalid radius. Maximum radius = 2 * stem.')
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._phi = None

    @property
    def overlap(self):
        """Overlap coefficient. Defaults to 0.
        :return:
        :rtype:
        """
        return self.construction.overlap

    @overlap.setter
    def overlap(self, value):
        self.construction.overlap = value