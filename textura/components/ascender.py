#!/usr/bin/env python
# -*- coding: utf-8 -*-

from textura.components import Component

class Ascender(Component):

    def construction(self):
        _x = self.xs[-1]
        _y = self.height + self.ascent - self.stem * tan(self.theta)
        xs.append(_x)
        ys.append(_y)

        _x += self.stem
        _y += self.stem * tan(self.theta)
        xs.append(_x)
        ys.append(_y)

        return xs, ys