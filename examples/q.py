from manim import *
from operator import add, sub
import numpy as np
import math as libm

class DrawParallelogram(Scene):
    def construct(self):
        o = (0, 0, 0)
        p1 = (1, 0.5, 0)
        p2 = (-0.5, 1.5, 0)

        v1 = Arrow(start=o, end=p1, buff=0)
        v2 = Arrow(start=o, end=p2, buff=0)

        s = libm.sqrt(np.dot(p1, p1))
        p1cap = [element / s for element in p1]
        p1dotp1cap = np.dot(p2, p1cap)
        proj = [element * p1dotp1cap for element in p1cap]
        oproj = tuple(map(add, o, proj))
        vproj = Line(start=o, end=oproj, color=RED)

        rej = tuple(map(sub, p2, proj))
        vrej = Line(start=oproj, end=p2, color=RED)

        op3 = tuple(map(add, p1, p2))
        parallelogram = [o, p1, op3, p2]
        poly = Polygon(*parallelogram)

        cut = tuple(map(add, p1, rej))
        recttop = tuple(map(sub, cut, p1))
        dashrej = DashedLine(start=p1, end=cut)
        dashtop = DashedLine(start=cut, end=recttop)
        dashside = DashedLine(start=recttop, end=o)

        self.play(Create(v1))
        self.play(Create(v2))
        self.play(Create(poly))
        self.play(Create(vproj))
        self.play(Create(vrej))
        self.play(Create(dashrej))
        self.play(Create(dashtop))
        self.play(Create(dashside))
        self.play(FadeOut(vproj, vrej))

        move = (-5, 1.5, 0)
        a = VGroup(dashrej, dashtop, dashside, v1, v2, poly)
        tx = tuple(map(add, a.get_center(), move))
        a.move_to( tx )
        self.play(Create(a))
