# -*- coding: utf-8 -*-


class Contour(object):
    def __init__(self, components, start):
        self._components = components
        self._start = start

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        self._components = value

    @property
    def start(self):
        if self._start is None:
            self._start = [0, 0]
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def coords(self):
        coords = [self.start, ]
        for component in self.components:
            for c in component.coords:
                signs = [1 if c[0][0] >= 0 else -1,
                         1 if c[1][0] >= 0 else -1]
                coords.append([
                    coords[-1][0] * abs(c[0][0]) + signs[0] * c[0][1],
                    coords[-1][1] * abs(c[1][0]) + signs[1] * c[1][1],])
        coords.append(coords[0])
        return coords

    @property
    def xs(self):
        return [x[0] for x in self.coords]

    @property
    def ys(self):
        return [x[1] for x in self.coords]
