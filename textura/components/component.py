#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Component(object):
    def __init__(self, coords):
        self._coords = coords

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, value):
        self._coords = value

    @property
    def xs(self):
        return [x[:,0] for x in self.coords]

    @property
    def ys(self):
        return [x[:,1] for x in self.coords]