# -*- coding: utf-8 -*-
from __future__ import division
from math import cos, tan, sin
import numpy as np
from textura.glyph import Glyph


class Glyphs(object):
    def __init__(self, components):
        self.components = components

    def zero(self, g):
        g = np.array(g)
        g[0][:] -= min(g[0][:])
        g[1][:] -= min(g[1][:])
        return g

    @property
    def b(self):
        coords = [[0, ], [0, ], ]
        coords = self.components.moveto_lower_bowl(*coords)
        coords = self.components.lower_bowl(*coords)
        coords = self.components.ascender(*coords)
        coords = self.components.lower_counter(*coords)
        coords = self.components.upper_left_serif(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords)]

    @property
    def c(self):
        coords = [[0, ], [0, ], ]
        coords = self.components.moveto_upper_bowl(*coords)
        coords = self.components.upper_finial(*coords)
        coords = self.components.lower_finial(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords)]

    @property
    def d(self):
        coords = [[0, ], [0, ], ]
        coords = self.components.moveto_lower_counter(*coords)
        coords = self.components.d(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords)]

    @property
    def n(self):
        coords = [[0,], [0, ]]
        coords = self.components.moveto_foot_serif(*coords)
        coords = self.components.foot_serif(*coords)
        coords = self.components.upper_left_shoulder_serif(*coords)
        coords = self.components.upper_right_shoulder(*coords)
        coords = self.components.foot_serif(*coords)
        coords = self.components.upper_counter(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords)]

    @property
    def o(self):
        coords = [[0,], [0, ], ]
        coords = self.components.moveto_lower_bowl(*coords)
        coords = self.components.lower_bowl(*coords)
        coords = self.components.upper_bowl(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords), self.components.counter()]

    @property
    def v(self):
        coords = [[0,], [0, ], ]
        coords = self.components.moveto_lower_bowl(*coords)
        coords = self.components.lower_bowl(*coords)
        coords = self.components.upper_left_serif(*coords)
        coords = self.components.lower_counter(*coords)
        coords = self.components.upper_left_serif(*coords)
        coords[0].append(coords[0][0])
        coords[1].append(coords[1][0])
        return [self.zero(coords)]