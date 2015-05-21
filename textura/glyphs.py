# -*- coding: utf-8 -*-
from __future__ import division
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
    def a(self):
        # TODO: Add a
        return None

    @property
    def b(self):
        return Glyph([Contour([
            self.components.bowl.lower_bowl,
            self.components.serif.upper_left_serif,
            self.components.counter.lower_counter,
            self.components.extender.ascender,],
            self.components.bowl.moveto_lower_bowl())])

    @property
    def c(self):
        return Glyph([Contour([
            self.components.finial.lower_finial,
            self.components.finial.upper_finial,
            self.components.bowl.linefrom_upper_bowl_apex,],
            self.components.finial.moveto_lower_finial())])

    @property
    def d(self):
        return Glyph([Contour([
            self.components.bowl.lower_bowl,
            self.components.glyph.d_ascent,
            self.components.counter.lower_counter,
            self.components.glyph.d_bowl,],
            self.components.bowl.moveto_lower_bowl())])

    @property
    def e(self):
        return Glyph([
            Contour([
                self.components.bowl.linefrom_upper_bowl_apex,
                self.components.finial.lower_finial,
                self.components.glyph.e_eye,],
                self.components.bowl.moveto_upper_bowl_apex()),
            Contour([
                self.components.glyph.e_eye_counter,],
                self.components.glyph.moveto_e_eye_counter(),
                ccw=False)])

    @property
    def f(self):
        # TODO: Fix f
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
    def g(self):
        # TODO: Add g
        return None

    @property
    def h(self):
        return Glyph([Contour([
            self.components.serif.foot_serif,
            self.components.counter.upper_counter,
            self.components.serif.foot_serif,
            self.components.shoulder.upper_right_shoulder,
            self.components.glyph.h_shoulder,
            self.components.extender.ascender,],
            self.components.serif.moveto_foot_serif())])

    @property
    def i(self):
        # TODO: Better dot placement on i (and j)
        return Glyph([Contour([
            self.components.serif.foot_serif,
            self.components.serif.upper_left_serif,
        ], self.components.serif.moveto_foot_serif()),
        Contour([
            self.components.mark.tittle,
        ], self.components.mark.moveto_tittle())])

    @property
    def j(self):
        # TODO: Add j`
        return None

    @property
    def k(self):
        # TODO: Add k
        return None

    @property
    def l(self):
        return Glyph([Contour([
            self.components.serif.foot_serif,
            self.components.extender.ascender,
        ], self.components.serif.moveto_foot_serif())])

    @property
    def m(self):
        return Glyph([Contour([
            self.components.serif.foot_serif,
            self.components.counter.upper_counter,
            self.components.serif.foot_serif,
            self.components.counter.upper_counter,
            self.components.serif.foot_serif,
            self.components.shoulder.upper_right_shoulder,
            self.components.glyph.m_shoulder,
            self.components.serif.upper_left_shoulder_serif,],
            self.components.serif.moveto_foot_serif())])

    @property
    def n(self):
        return Glyph([Contour([
            self.components.serif.foot_serif,
            self.components.counter.upper_counter,
            self.components.serif.foot_serif,
            self.components.shoulder.upper_right_shoulder,
            self.components.serif.upper_left_shoulder_serif,],
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
                self.components.counter.moveto_lower_counter(),
                ccw=False)])

    @property
    def p(self):
        return Glyph([
            Contour([
                self.components.serif.upper_left_shoulder_serif,
                self.components.extender.descender,
                self.components.glyph.p_bowl,
                self.components.shoulder.upper_right_shoulder,],
                self.components.serif.moveto_upper_left_shoulder_serif()),
            Contour([
                self.components.counter.counter,],
                self.components.counter.moveto_lower_counter(),
                ccw=False)])

    @property
    def q(self):
        # TODO: Add q
        return None

    @property
    def r(self):
        return Glyph([
            Contour([
                self.components.serif.upper_left_shoulder_serif,
                self.components.serif.foot_serif,
                self.components.finial.upper_finial,],
                self.components.serif.moveto_upper_left_shoulder_serif()
            )
        ])

    @property
    def s(self):
        # TODO: Add s
        return None

    @property
    def t(self):
        # TODO: Add t
        return None

    @property
    def u(self):
        return Glyph([
            Contour([
                self.components.serif.upper_left_serif,
                self.components.shoulder.lower_left_shoulder,
                self.components.serif.lower_right_shoulder_serif,
                self.components.serif.upper_left_serif,
                self.components.counter.lower_counter,],
                self.components.serif.moveto_upper_serif()),])

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
                self.components.serif.upper_left_serif,
                self.components.glyph.w_bowl,
                self.components.serif.upper_left_serif,
                self.components.counter.lower_counter,
                self.components.serif.upper_left_serif,
                self.components.counter.lower_counter,],
                self.components.serif.moveto_upper_serif()),])

    @property
    def x(self):
        # TODO: Add x
        return None

    @property
    def y(self):
        # TODO: Add y
        return None

    @property
    def z(self):
        # TODO: Add z
        return None