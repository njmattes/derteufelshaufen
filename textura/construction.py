#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from math import sqrt, sin, asin, tan, atan, cos, acos, degrees

class Construction(object):
    def __init__(self, stem, counter, radius, x, theta):
        self.s = stem
        self.c = counter
        self.r = radius
        self._overlap = x
        self.theta = theta
        self._phi = None
        self._phi_steep = None
        self._pi = None
        self.n = .5
        self.nl = .5
        self.nr = .5

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
    def phi_steep(self):
        if self._phi_steep is None:
            # _phi_steep = 4 * self.r * cos(self.theta)
            # _phi_steep /= 2 * self.sigma - (self.overlap + self.s)
            # print 1,_phi_steep
            # self._phi_steep = asin(_phi_steep) - self.theta

            x = self.sigma - 2 * self.r * cos(self.theta)
            self._phi_steep = atan(x * tan(self.theta / abs(self.s - x)))
        return self._phi_steep

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

    def d_ascent(self):
        h = 200 + ((self.s * 2 + self.c) - self.sigma) * tan(self.phi)
        w = (self.s * 2 + self.c) * 1.1
        r = 2 * self.r
        x = (h ** 2 / r - sqrt(h ** 2 * (h ** 2 + 4 * r ** 2)) / r) / 2 * h
        y = -sqrt((sqrt(h ** 4 + 4 * h **2 * r ** 2) / 2 * r ** 2 - h ** 2 / 2 * r ** 2))
        a = abs(atan(x/y))
        return a

    def d_ascent2(self):
        a = 200 + ((self.s * 2 + self.c) - self.sigma) * tan(self.phi)
        b = (self.s * 2 + self.c) * 1.1
        c = 2 * self.r
        x=b/2-1/2*sqrt(-a**2+1/3*(a**2+b**2)+(2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2+sqrt((2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2)**2-4*((a**2+b**2)**2-12*a**2*c**2)**3))**(1/3)/(3*2**(1/3))+(2**(1/3)*((a**2+b**2)**2-12*a**2*c**2))/(3*(2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2+sqrt((2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2)**2-4*((a**2+b**2)**2-12*a**2*c**2)**3))**(1/3)))+1/2*sqrt(-a**2+b**2+1/3*(-a**2-b**2)-(2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2+sqrt((2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2)**2-4*((a**2+b**2)**2-12*a**2*c**2)**3))**(1/3)/(3*2**(1/3))-(2**(1/3)*((a**2+b**2)**2-12*a**2*c**2))/(3*(2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2+sqrt((2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2)**2-4*((a**2+b**2)**2-12*a**2*c**2)**3))**(1/3))-(8*b**3-8*b*(a**2+b**2))/(4*sqrt(-a**2+1/3*(a**2+b**2)+(2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2+sqrt((2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2)**2-4*((a**2+b**2)**2-12*a**2*c**2)**3))**(1/3)/(3*2**(1/3))+(2**(1/3)*((a**2+b**2)**2-12*a**2*c**2))/(3*(2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2+sqrt((2*(a**2+b**2)**3+72*a**2*c**2*(a**2+b**2)-108*a**2*b**2*c**2)**2-4*((a**2+b**2)**2-12*a**2*c**2)**3))**(1/3)))))
        return x