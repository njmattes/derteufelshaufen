# -*- coding: utf-8 -*-


class ComponentGroup(object):
    def __init__(self, construction):
        self.construction = construction
        self.height = 700
        self.ascent = 200
        self.descent = 120
        self.s = construction.s
        self.c = construction.c
        self.x = construction.overlap
        self.o = construction.offset
        self.r = construction.r
        self.th = construction.theta
        self.ph = construction.phi
        self.rh = construction.rho
        self.phs = construction.phi_steep
        self.rhs = construction.rho_steep
        self.pi = construction.pi
        self.si = construction.sigma
        self.eta = construction.eta
        self.pinch_y = construction.pinch_y
        self.n = construction.n
        self.nl = construction.nl
        self.nr = construction.nr
        self.nf = construction.nf
        self.hairline = construction.hairline