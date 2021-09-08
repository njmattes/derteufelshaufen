#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from math import tan


def split_triangle(base, theta, phi, inverted=False):

    splits = [
        base * tan(phi) / (tan(phi) + tan(theta)),
        base * tan(theta) / (tan(phi) + tan(theta)),
    ]
    if inverted:
        splits.reverse()
    return splits
