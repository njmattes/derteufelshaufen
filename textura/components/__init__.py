# -*- coding: utf-8 -*-
from __future__ import division
from textura.components.groups.bowl import Bowl
from textura.components.groups.counter import Counter
from textura.components.groups.crossbar import Crossbar
from textura.components.groups.extender import Extender
from textura.components.groups.finial import Finial
from textura.components.groups.glyph import Glyph
from textura.components.groups.mark import Mark
from textura.components.groups.serif import Serif
from textura.components.groups.shoulder import Shoulder


class Components(object):
    def __init__(self, construction):
        self.serif = Serif(construction)
        self.counter = Counter(construction)
        self.crossbar = Crossbar(construction)
        self.extender = Extender(construction)
        self.bowl = Bowl(construction)
        self.finial = Finial(construction)
        self.shoulder = Shoulder(construction)
        self.glyph = Glyph(construction)
        self.mark = Mark(construction)
