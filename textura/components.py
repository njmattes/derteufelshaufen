# -*- coding: utf-8 -*-
from __future__ import division
from math import cos, tan, sin, atan, degrees, sqrt
from math import pi as math_pi


class Components(object):

    def __init__(self, construction):
        self.height = 700
        self.ascent = 200
        self.descent = 120
        self.nf = sqrt(2) / 2
        self.s = construction.s
        self.c = construction.c
        self.x = construction.overlap
        self.o = construction.offset
        self.r = construction.r
        self.th = construction.theta
        self.ph = construction.phi
        self.phs = construction.phi_steep
        self.pi = construction.pi
        self.si = construction.sigma
        self.eta = construction.eta
        self.pinch_y = construction.pinch_y
        self.n = construction.n
        self.nl = construction.nl
        self.nr = construction.nr

    def moveto_lower_bowl(self, xs, ys):
        xs[-1] = self.s * 2 + self.c
        ys[-1] = self.si * tan(self.th)
        return xs, ys

    def moveto_lower_counter(self, xs, ys):
        xs[-1] = self.s
        ys[-1] = self.si * tan(self.th)
        ys[-1] += self.pinch_y + self.c * tan(self.ph)
        # ys[-1] += (self.s + self.c - self.o) * tan(self.ph)
        return xs, ys

    def moveto_upper_bowl(self, xs, ys):
        xs[-1] = 0
        ys[-1] = self.height - self.si * tan(self.th)
        return xs, ys

    def moveto_foot_serif(self, xs, ys):
        ys[-1] = (tan(self.ph) * self.c * self.n + 2 * self.r * cos(self.ph))
        return xs, ys

    def moveto_upper_left_shoulder_serif(self, xs, ys):
        ys[-1] = self.height - 2 * self.r * cos(self.ph) - self.c * self.nl * tan(self.ph)
        return xs, ys

    def moveto_ascender(self, xs, ys):
        ys[-1] = self.height + self.ascent - self.s * tan(self.th)
        return xs, ys

    def lineto_ascender(self, xs, ys):
        _x = xs[-1]
        _y = self.height + self.ascent - self.s * tan(self.th)
        return _x, _y

    def ascender(self, xs, ys):
        _x, _y = self.lineto_ascender(xs, ys)
        xs.append(_x)
        ys.append(_y)

        _x += self.s
        _y += self.s * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_left_serif(self, xs, ys):
        a = self.ph
        cn = self.c * self.nl

        _x = xs[-1]
        _y = self.height - 2 * self.r * cos(a) - cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x -= cn
        _y += cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * self.r * sin(a)
        _y += 2 * self.r * cos(a)
        xs.append(_x)
        ys.append(_y)

        _xx = self.s + cn - 2 * self.r * sin(a)
        _x += _xx
        _y -= _xx * tan(a)
        xs.append(_x)
        ys.append(_y)

        return xs, ys



    def upper_left_shoulder_serif(self, xs, ys):
        a = self.ph
        cn = self.c * self.nl

        _x = xs[-1]
        _y = self.height - 2 * self.r * cos(a) - cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x -= cn
        _y += cn * tan(a)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * self.r * sin(a)
        _y += 2 * self.r * cos(a)
        xs.append(_x)
        ys.append(_y)

        #left-side of notch
        _x += self.eta
        _y -= tan(a) * self.eta
        xs.append(_x)
        ys.append(_y)

        _x += self.si - (self.eta + 2 * self.r * sin(a) - cn) # /
        _y += tan(a) * self.eta
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_right_shoulder(self, xs, ys):
        a = self.ph
        cn = self.c * self.nl

        _x = xs[-1]
        _y = ys[-1]
        # \
        _xx = 2 * self.s + self.c - self.si
        _x += _xx
        _y -= tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def foot_serif(self, xs, ys):
        """Draws three (six) strokes that make up a foot serif.
        Assumes vertical entry.
        Proceeds SE, SW, NW.
        :param xs: current x coords
        :param ys: current y coords
        :return: xs, ys
        :rtype: tuple
        """
        a = self.ph
        cn = self.c * self.nl

        _x = xs[-1]
        _y = tan(self.ph) * self.c * self.n + \
             2 * self.r * cos(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x = xs[-1] + cn
        _y = 2 * self.r * cos(a)
        xs.append(_x)
        ys.append(_y)
        # /
        _x -= 2 * self.r * sin(a)
        _y = 0
        xs.append(_x)
        ys.append(_y)
        # \
        _xx = (self.s + cn) - 2 * self.r * sin(a)
        _x -= _xx
        _y += tan(a) * _xx
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_left_serif(self, xs, ys):
        a = self.ph
        cn = self.c * self.nl

    def lower_bowl(self, xs, ys):
        _x = xs[-1]
        _y = self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x -= self.si
        _y -= self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.s * 2 + self.c) - self.si
        _x -= _xx
        _y += _xx * tan(self.ph)
        xs.append(_x)
        ys.append(_y)
        return xs, ys

    def upper_bowl(self, xs, ys):
        _x = xs[-1]
        _y = self.height - self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x += self.si
        _y += self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.s * 2 + self.c) - self.si
        _x += _xx
        _y -= _xx * tan(self.ph)
        xs.append(_x)
        ys.append(_y)
        return xs, ys

    def upper_counter(self, xs, ys):
        _x = xs[-1]

        _y = self.height - self.si * tan(self.th)
        _y -= self.pinch_y + self.c * tan(self.ph)
        print _y, self.pinch_y
        xs.append(_x)
        ys.append(_y)

        _x -= self.c
        _y += self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_counter(self, xs, ys):
        _x = xs[-1]

        _y = self.si * tan(self.th)
        _y += self.pinch_y + self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x += self.c
        _y -= self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def counter(self):

        xs = []
        ys = []

        _x = self.s + self.c
        _y = self.height - self.si * tan(self.th)
        _y -= self.pinch_y + self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x -= self.c
        _y += self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _y = self.si * tan(self.th)
        _y += self.pinch_y + self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _x += self.c
        _y -= self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        xs.append(xs[0])
        ys.append(ys[0])

        return xs, ys

    def upper_finial(self,xs, ys):
        """ /`\
             \/
        :param xs:
        :type xs:
        :param ys:
        :type ys:
        :return:
        :rtype:
        """
        _x = xs[-1]
        _y = self.height - self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        cn = self.c * self.nf
        phi = (math_pi / 2 - self.ph) * self.nf ** 2
        rho = self.s + cn + 2 * self.r * cos(phi) - self.si

        _x += self.si
        _y += self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x += rho
        _y -= rho / tan(phi)
        xs.append(_x)
        ys.append(_y)

        _x -= 2 * self.r * cos(phi)
        _y -= 2 * self.r * sin(phi)
        xs.append(_x)
        ys.append(_y)

        _x -= cn
        _y += cn / tan(phi)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def upper_finial2(self,xs, ys):
        """ /`\
             \/
        :param xs:
        :type xs:
        :param ys:
        :type ys:
        :return:
        :rtype:
        """
        _x = xs[-1]
        _y = self.height - self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x += self.si
        _y += self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        phi = (math_pi / 2 - self.ph) * .9
        _xx = (self.s * 2 + self.c) * .9 - self.si
        _x += _xx
        _y -= _xx / tan(phi)
        xs.append(_x)
        ys.append(_y)

        _x -= 2 * self.r * cos(phi)
        _y -= 2 * self.r * sin(phi)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.s * 2 + self.c) * .9 - 2 * self.r * cos(phi) - self.s
        _x -= _xx
        _y += _xx / tan(phi)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_finial(self, xs, ys):
        cn = self.c * self.nf * .9
        phi = (math_pi / 2 - self.ph) * self.nf *.9
        rho = self.s + cn + 2 * self.r * cos(phi) - self.si

        _x = xs[-1]
        _y = (self.si + rho - self.s) * tan(self.ph / 2) + 2 * self.r * cos(self.ph / 2)
        xs.append(_x)
        ys.append(_y)

        _x += (self.si + rho - self.s)
        _y -= (self.si + rho - self.s) * tan(self.ph / 2)
        xs.append(_x)
        ys.append(_y)

        _x -= 2 * self.r * sin(self.ph / 2)
        _y -= 2 * self.r * cos(self.ph / 2)
        xs.append(_x)
        ys.append(_y)

        _xx = rho + self.si - 2 * self.r * sin(self.ph / 2)
        _x -= _xx
        _y += _xx * tan(self.ph / 2)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def lower_finial2(self, xs, ys):
        rho = (self.s * 2 + self.c) * .9 ** 2 - self.si
        _x = xs[-1]
        _y = (self.si + rho - self.s) * tan(self.ph / 2) + 2 * self.r * cos(self.ph / 2)
        xs.append(_x)
        ys.append(_y)

        _x += (self.si + rho - self.s)
        _y -= (self.si + rho - self.s) * tan(self.ph / 2)
        xs.append(_x)
        ys.append(_y)

        _x -= 2 * self.r * sin(self.ph / 2)
        _y -= 2 * self.r * cos(self.ph / 2)
        xs.append(_x)
        ys.append(_y)

        _xx = (self.s * 2 + self.c) * .9 ** 2 - 2 * self.r * sin(self.ph / 2)
        _x -= _xx
        _y += _xx * tan(self.ph / 2)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def d(self, xs, ys):
        _x = xs[-1]
        _y = ys[-1]

        ang = atan((2 * self.s + self.c) / self.ascent)

        _x += self.c
        _y -= self.c * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _xx = self.s + self.c + 2 * self.r * cos(ang)
        _y = self.height + self.ascent - _xx / tan(ang) - 2 * self.r * sin(ang)
        xs.append(_x)
        ys.append(_y)


        _x -= _xx
        _y += _xx / tan(ang)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * self.r * cos(ang)
        _y += 2 * self.r * sin(ang)
        xs.append(_x)
        ys.append(_y)

        _x += 2 * self.s + self.c
        _y -= self.ascent
        xs.append(_x)
        ys.append(_y)

        _y = self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        xs, ys = self.lower_bowl(xs, ys)

        _x = xs[-1]
        _y = self.height + self.ascent - 2 * self.r * sin(ang)
        _y -= _xx / tan(ang)
        _y -= self.s * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x += self.s
        _y += self.s * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def p(self, xs, ys):
        _x = xs[-1]
        _y = self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x -= self.si
        _y -= self.si * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _xx = self.s + self.c - self.si
        _x -= _xx
        _y += _xx * tan(self.ph)
        xs.append(_x)
        ys.append(_y)

        _y -= self.descent - self.s * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x -= self.s
        _y -= self.s * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        return xs, ys

    def h_shoulder(self, xs, ys):
        #TODO: Base shoulder on width of NW crotch in n
        _x = xs[-1]
        _y = self.height - (self.si - self.s) * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        _x += (self.si - self.s)
        _y += (self.si - self.s) * tan(self.th)
        xs.append(_x)
        ys.append(_y)

        return xs, ys
