# -*- coding: utf-8 -*-
from __future__ import division
from math import radians
from textura.components import Components
from textura.construction import Construction
from textura.glyphs import Glyphs


class Font(object):
    def __init__(self, stem, counter, theta, radius=None, x=None,
                 n=.5, nl=.5, nr=.5, nf=.9):
        self.stem = stem
        self.counter = float(counter)
        self._theta = radians(float(theta))
        self._radius = radius
        self._phi = None
        self._pi = None
        self._phi_steep = None
        self._n = n
        self._nl = nl
        self._nr = nr
        self._nf = nf
        self.construction = Construction(self.stem, self.counter, self.radius,
                                         x, self.theta, self.n, self.nl,
                                         self.nr, self.nf)
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
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = value

    @property
    def nl(self):
        return self._nl

    @nl.setter
    def nl(self, value):
        self._nl = value

    @property
    def nr(self):
        return self._nr

    @nr.setter
    def nr(self, value):
        self._nr = value

    @property
    def nf(self):
        return self._nf

    @nf.setter
    def nf(self, value):
        self._nf = value

