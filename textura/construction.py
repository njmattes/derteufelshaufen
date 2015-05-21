# -*- coding: utf-8 -*-
from __future__ import division
from math import sin, tan, atan, cos, floor, sqrt
from math import pi as math_pi


class Construction(object):
    def __init__(self, stem, counter, radius, x, theta, n, nl, nr, nf):
        self.s = stem
        self.c = counter
        self.r = radius
        self._overlap = x
        self.theta = theta
        self._phi = None
        self._phi_steep = None
        self._rho_steep = None
        self._pi = None
        self.n = n
        self.nl = nl
        self.nr = nr
        self.nf = nf

    @property
    def phi(self):
        """Angle of stroke in top right.
        :return: Angle in radians
        :rtype: float
        """
        if self._phi is None:
            self._phi = atan(self.s * tan(self.theta) / (self.s +
                                                         self.c - self.r))
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
        return 2 * self.s + self.c - self.sigma

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
            self._overlap = self.s - (self.r / (cos(self.phi) * tan(self.theta)
                                                + sin(self.phi)))
        if self._overlap < -(self.offset + self.r) / tan(self.theta):
            raise Exception('''Invalid overlap.
Minimum overlap = -(offset + radius) / tan(theta).''')
        if self._overlap > self.s:
            raise Exception('Invalid overlap. Maximum overlap = stem.')
        return self._overlap

    @property
    def pinch_y(self):
        y = (self.offset + self.r * cos(self.phi))
        y -= tan(self.phi) * ((self.s + self.c) -
                              (self.r * (1 + sin(self.phi))))
        return y

    @property
    def eta(self):
        """Width of one side of NW notch in n
        :return:
        """
        _eta = self.sigma + (self.c * self.nl - 2 * self.r * sin(self.phi))
        _eta0 = _eta * tan(self.theta) / (tan(self.theta) + tan(self.phi))
        return [
            _eta0,
            _eta - _eta0
        ]

    @property
    def phi_steep(self):
        if self._phi_steep is None:
            self._phi_steep = math_pi / 2 - (math_pi / 2 -
                                             self.phi) * self.nf ** 2
            self._phi_steep = self.phi + (math_pi / 2 -
                                          self.phi) * self.phi / (math_pi / 2)
        return self._phi_steep

    @property
    def rho_steep(self):
        if self._rho_steep is None:
            cn = self.c * self.nf
            self._rho_steep = self.s + cn + \
                              2 * self.r * sin(self.phi_steep) - self.sigma
        return self._rho_steep

    @property
    def hairline(self):
        return 20 if self.s > 25 else floor(self.s * sqrt(2) / 2)