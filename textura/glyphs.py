# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
from textura.contour import Contour


class Glyph(object):
    def __init__(self, contours, start=None):
        self._contours = contours
        self._start = start

    @property
    def contours(self):
        return self._contours

    @contours.setter
    def contours(self, value):
        self._contours = value


class Glyphs(object):
    def __init__(self, components):
        self.components = components

    @property
    def b(self):
        return Glyph([Contour([
            self.components.bowl.lower_bowl,
            self.components.extender.ascender,
            self.components.counter.lower_counter,
            self.components.serif.upper_left_serif,],
            self.components.bowl.moveto_lower_bowl())])

    @property
    def c(self):
        return Glyph([Contour([
            self.components.bowl.lineto_upper_bowl_apex,
            self.components.finial.upper_finial,
            self.components.finial.lower_finial,],
            self.components.bowl.moveto_upper_bowl())])

    @property
    def d(self):
        return Glyph([Contour([
            self.components.bowl.lower_bowl,
            self.components.glyph.d_bowl,
            self.components.counter.lower_counter,
            self.components.glyph.d_ascent,],
            self.components.bowl.moveto_lower_bowl())])

    @property
    def e(self):
        return Glyph([Contour([
            self.components.bowl.lineto_upper_bowl_apex,
            self.components.glyph.e_eye,
            self.components.finial.lower_finial,],
            self.components.bowl.moveto_upper_bowl())])

    @property
    def f(self):
        return Glyph([Contour([
            self.components.serif.foot_serif,
            # self.components.crossbar.left_crossbar,
            self.components.extender.lineto_ascender,
            self.components.extender.lineto_ascent_apex,
            # self.components.extender.ascender,
            self.components.finial.upper_finial,],
            # self.components.crossbar.right_crossbar,],
            self.components.serif.moveto_foot_serif())])

    @property
    def h(self):
        return Glyph([Contour([
            self.components.serif.foot_serif,
            self.components.extender.ascender,
            self.components.glyph.h_shoulder,
            self.components.shoulder.upper_right_shoulder,
            self.components.serif.foot_serif,
            self.components.counter.upper_counter,],
            self.components.serif.moveto_foot_serif())])

    @property
    def l(self):
        return Glyph([Contour([
            self.components.serif.foot_serif,
            self.components.extender.ascender,
        ], self.components.serif.moveto_foot_serif())])

    @property
    def n(self):
        return Glyph([Contour([
            self.components.serif.foot_serif,
            self.components.serif.upper_left_shoulder_serif,
            self.components.shoulder.upper_right_shoulder,
            self.components.serif.foot_serif,
            self.components.counter.upper_counter,],
            self.components.serif.moveto_foot_serif())])

    @property
    def o(self):
        return Glyph([
            Contour([
                self.components.bowl.lower_bowl,
                self.components.bowl.upper_bowl,],
                self.components.bowl.moveto_lower_bowl()),
            Contour([
                self.components.counter.counter,],
                self.components.counter.moveto_lower_counter())])

    @property
    def p(self):
        return Glyph([
            Contour([
                self.components.serif.upper_left_shoulder_serif,
                self.components.shoulder.upper_right_shoulder,
                self.components.glyph.p_bowl,],
                self.components.serif.moveto_upper_left_shoulder_serif()),
            Contour([
                self.components.counter.counter,],
                self.components.counter.moveto_lower_counter())])

    @property
    def r(self):
        return Glyph([
            Contour([
                self.components.serif.upper_left_shoulder_serif,
                self.components.finial.upper_finial,
                self.components.serif.foot_serif,],
                self.components.serif.moveto_upper_left_shoulder_serif()
            )
        ])

    @property
    def u(self):
        return Glyph([
            Contour([
                self.components.serif.upper_left_serif,
                self.components.counter.lower_counter,
                self.components.serif.upper_left_serif,
                self.components.serif.lower_right_shoulder_serif,
                self.components.shoulder.lower_left_shoulder,],
                self.components.serif.moveto_upper_left_shoulder_serif()),])

    @property
    def v(self):
        return Glyph([
            Contour([
                self.components.bowl.lower_bowl,
                self.components.serif.upper_left_serif,
                self.components.counter.lower_counter,
                self.components.serif.upper_left_serif,],
                self.components.bowl.moveto_lower_bowl()),])

    @property
    def w(self):
        return Glyph([
            Contour([
                self.components.bowl.lower_bowl,
                self.components.glyph.w_bowl,
                self.components.serif.upper_left_serif,
                self.components.counter.lower_counter,
                self.components.serif.upper_left_serif,
                self.components.counter.lower_counter,
                self.components.serif.upper_left_serif,],
                self.components.bowl.moveto_lower_bowl()),])