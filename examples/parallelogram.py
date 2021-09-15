from manim import *
from operator import add, sub
import numpy as np
import math as libm

#   p1 + p2
#     /\
#    /  \
#   p2   \p1
#    \   /
#     \ /
#      o

class DrawParallelogram(Scene):
    def construct(self):
        o = (0, -2, 0)
        p1 = (2, 1, 0)
        p2 = (-0.5, 3, 0)
        op1 = tuple(map(add, o, p1))
        op2 = tuple(map(add, o, p2))

        v1 = Arrow(start=o, end=op1, buff=0)
        v2 = Arrow(start=o, end=op2, buff=0)

        v1l = Tex(r'$\vec{a}$').scale(1)
        v2l = Tex(r'$\vec{b}$').scale(1)
        v1l.next_to(v1, RIGHT)
        v2l.next_to(v2, UP)

        s = libm.sqrt(np.dot(p1, p1))
        p1cap = [element / s for element in p1]
        p1dotp1cap = np.dot(p2, p1cap)
        proj = [element * p1dotp1cap for element in p1cap]
        oproj = tuple(map(add, o, proj))
        vproj = Line(start=o, end=oproj, color=RED)
        vprojl = Tex(r'$\left(\vec{b} \cdot \hat{a}\right) \hat{a}$').scale(1)
        vprojl.next_to(vproj, DOWN)
        v1g = VGroup(v1, v1l)
        vprojg = VGroup(vproj, vprojl)

        rej = tuple(map(sub, p2, proj))
        vrej = Line(start=oproj, end=op2, color=RED)
        vrejl = Tex(r'$\vec{b} - \left(\vec{b} \cdot \hat{a}\right) \hat{a}$').scale(1)
        vrejl.next_to(vrej, RIGHT)
        v2g = VGroup(v2, v2l)
        vrejg = VGroup(vrej, vrejl)

        op3 = tuple(map(add, op1, p2))
        parallelogram = [o, op1, op3, op2]
        poly = Polygon(*parallelogram)

        cut = tuple(map(add, op1, rej))
        recttop = tuple(map(sub, cut, p1))
        dashrej = DashedLine(start=op1, end=cut)
        dashtop = DashedLine(start=cut, end=recttop)
        dashside = DashedLine(start=recttop, end=o)

        self.play(Create(v1g))
        self.play(Create(v2g))
        self.play(Create(poly))
        self.play(Create(vprojg))
        self.play(Create(vrejg))
        self.play(Create(dashrej))
        self.play(Create(dashtop))
        self.play(Create(dashside))
        self.play(FadeOut(vprojg, vrejg))

        move = (-5, 1.5, 0)
        a = VGroup(dashrej, dashtop, dashside, v1, v1l, v2, v2l, poly)
        tx = tuple(map(add, a.get_center(), move))
        a.move_to( tx )
        self.play(Create(a))
