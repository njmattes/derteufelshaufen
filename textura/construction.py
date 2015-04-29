#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from math import sqrt, sin, asin, tan, atan, cos
from math import pi as math_pi

class Construction(object):
    def __init__(self, stem, counter, radius, x, theta):
        self.s = stem
        self.c = counter
        self.r = radius
        self._overlap = x
        self.theta = theta
        self._phi = None
        self._phi_steep = None
        self._rho_steep = None
        self._pi = None
        self.n = .5
        self.nl = .5
        self.nr = .5
        self.nf = sqrt(2) / 2

    @property
    def phi(self):
        """Angle of stroke in top right.
        :return: Angle in radians
        :rtype: float
        """
        if self._phi is None:
            h = self.offset + self.overlap * tan(self.theta)
            w = 2 * self.s + self.c - self.overlap - self.r
            self._phi = asin(self.r / sqrt(h ** 2 + w ** 2)) + tan(h / w)

        return self._phi

    @property
    def pi(self):
        """Width of segment between serif and shoulder.
        :return: Width in units
        :rtype: float
        """
        if self._pi is None:
            pi = self.sigma * tan(self.theta)
            pi -= (2 * self.r * sin(self.phi) - self.c * self.n)
            pi *= tan(self.phi)
            pi /= (tan(self.phi) + tan(self.theta))
            self._pi = pi
        return self._pi

    @property
    def sigma(self):
        """Distance from left edge to apex of top of o.
        :return: Distance in UPM
        :rtype: float
        """
        sigma = (
            self.r * (cos(self.phi) - tan(self.phi) +
                           tan(self.phi) * sin(self.phi)) -
            (self.s * 2 + self.c) * tan(self.theta) -
                self.offset) / (
            tan(self.theta) + tan(self.phi)
        )
        sigma += (self.s * 2 + self.c)
        return sigma

    @property
    def rho(self):
        return 2 * self.s - self.c - self.sigma

    @property
    def offset(self):
        return max(0, self.r - self.s * tan(self.theta))

    @property
    def a(self):
        return self.overlap * tan(self.theta)

    @property
    def overlap(self):
        """Overlap coefficient. Defaults to 0.
        :return:
        :rtype:
        """
        if self._overlap is None:
            self.overlap = 0
        if self._overlap < -(self.offset + self.r) / tan(self.theta):
            raise Exception('Invalid overlap. Minimum overlap = -(offset + radius) / tan(theta).')
        if self._overlap > self.s:
            raise Exception('Invalid overlap. Maximum overlap = stem.')
        return self._overlap

    @overlap.setter
    def overlap(self, value):
        self._overlap = value

    @property
    def pinch_y(self):
        y = (self.offset + self.r * cos(self.phi))
        y -= tan(self.phi) * ((self.s + self.c) - (self.r * (1 + sin(self.phi))))
        return y

    @property
    def eta(self):
        """Width of one side of NW notch in n
        :return:
        """
        _eta = self.sigma + (self.c * self.nl - 2 * self.r * sin(self.phi))
        _eta *= -tan(self.phi)
        _eta /= (tan(self.phi) + tan(self.theta))
        _eta += self.sigma
        return [
            _eta + (self.c * self.nl - 2 * self.r * sin(self.phi)),
            self.sigma - _eta
        ]

    @property
    def phi_steep(self):
        if self._phi_steep is None:
            return math_pi / 2 - (math_pi / 2 - self.phi) * self.nf ** 2
        return self._phi_steep

    @property
    def rho_steep(self):
        if self._rho_steep is None:
            cn = self.c * self.nf  * .9
            self._rho_steep = self.s + cn + 2 * self.r * sin(self.phi_steep) - self.sigma
        return self._rho_steep