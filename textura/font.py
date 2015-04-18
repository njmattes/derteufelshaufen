# -*- coding: utf-8 -*-
from __future__ import division
from math import tan, atan2, sin, asin, cos, sqrt, radians, degrees
from math import pi as math_pi
from textura.components import Components
from textura.glyphs import Glyphs


class Font(object):
    def __init__(self, stem, counter, theta, radius=None, x=None):
        self.stem = stem
        self.counter = float(counter)
        self._theta = radians(float(theta))
        self._radius = radius
        self._overlap = x
        self._phi = None
        self._pi = None
        self.n = .5
        self.nl = .5
        self.nr = .5
        self.components = Components(self.stem, self.counter, self.radius,
                                     self.overlap, self.theta, self.phi,
                                     self.pi, self.sigma)
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
    def pi(self):
        """Width of segment between serif and shoulder.
        :return: Width in units
        :rtype: float
        """
        if self._pi is None:
            pi = self.sigma * tan(self.theta)
            pi -= (2 * self.radius * sin(self.phi) - self.counter * self.n)
            pi *= tan(self.phi)
            pi /= (tan(self.phi) + tan(self.theta))
            self._pi = pi
        return self._pi

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
        if self._overlap is None:
            self.overlap = 0
        if self._overlap < -(self.offset + self.radius) / tan(self.theta):
            raise Exception('Invalid overlap. Minimum overlap = -(offset + radius) / tan(theta).')
        if self._overlap > self.stem:
            raise Exception('Invalid overlap. Maximum overlap = stem.')
        return self._overlap

    @overlap.setter
    def overlap(self, value):
        self._overlap = value

    @property
    def offset(self):
        return max(0, self.radius - self.stem * tan(self.theta))

    @property
    def a(self):
        return self.overlap * tan(self.theta)

    @property
    def phi(self):
        """Angle of stroke in top right.
        :return: Angle in radians
        :rtype: float
        """
        if self._phi is None:
            h = self.offset + self.overlap * tan(self.theta)
            w = 2 * self.stem + self.counter - self.overlap - self.radius
            self._phi = asin(self.radius / sqrt(h ** 2 + w ** 2)) + tan(h / w)

        return self._phi

    @property
    def sigma(self):
        """Distance from left edge to apex of top of o.
        :return: Distance in UPM
        :rtype: float
        """
        sigma = (
            self.radius * (cos(self.phi) - tan(self.phi) +
                           tan(self.phi) * sin(self.phi)) -
            (self.stem * 2 + self.counter) * tan(self.theta) -
                self.offset) / (
            tan(self.theta) + tan(self.phi)
        )
        sigma += (self.stem * 2 + self.counter)
        return sigma