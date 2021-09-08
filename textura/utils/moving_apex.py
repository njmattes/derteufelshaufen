#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from scipy.optimize import curve_fit
from math import pi as math_pi

def f(x, a, b, c):
    return a * x ** b + c


def get_apex(o_phi, sigma, rho, phi):
    x = [0, o_phi, math_pi / 2]
    y = [0, sigma / (sigma + rho), 1]
    a, b, c = curve_fit(f, x, y)[0]
    return f(phi, a, b, c) * (sigma + rho)


if __name__ == '__main__':
    a, b, c = get_apex()[0]
    for i in range(11):
        x = i  / 10 * (math_pi / 2)
        print(x, f(x, a, b, c))