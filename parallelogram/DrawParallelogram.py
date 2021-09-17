from manim import *
import numpy as np
from mylatex import *

#   p1 + p2
#     /\
#    /  \
#   p2   \p1
#    \   /
#     \ /
#      o

class DrawParallelogram(Scene):
    def construct(self):
        l = latex()
        u          = l.vec('u')
        uhat       = l.hat('u')
        v          = l.vec('v')

        o = np.array([0, -2, 0])
        p1 = np.array([3, 1, 0])
        p2 = np.array([1, 3, 0])
        op1 = o + p1
        op2 = o + p2

        v1 = Arrow(start=o, end=op1, buff=0)
        v2 = Arrow(start=o, end=op2, buff=0)

        v1l = MathTex( u )
        v2l = MathTex( v )
        v1l.next_to(v1, RIGHT)
        v2l.next_to(v2, UP)

        p1cap = p1/ np.linalg.norm(p1)
        proj = np.dot(p2, p1cap) * p1cap
        oproj = o + proj
        vproj = Line(start=o, end=oproj, color=RED)
        vprojl = MathTex( concat( l.lr( l.dot( v, uhat ) ), uhat ) )
        vprojl.next_to(vproj, DOWN)
        v1g = VGroup(v1, v1l)
        vprojg = VGroup(vproj, vprojl)

        rej = p2 - proj
        vrej = Line(start=oproj, end=op2, color=RED)
        vrejl = MathTex( concat( v, ' - ', l.lr( l.dot( v, uhat ) ), uhat ) )
        vrejl.next_to(vrej, RIGHT)
        vrejl.shift((-0.5,0,0))
        v2g = VGroup(v2, v2l)
        vrejg = VGroup(vrej, vrejl)

        op3 = op1 + p2
        parallelogram = [o, op1, op3, op2]
        poly = Polygon(*parallelogram)

        cut = op1 + rej
        recttop = cut - p1
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

        move = (-5, 1, 0)
        a = VGroup(dashrej, dashtop, dashside, v1, v1l, v2, v2l, poly)
        self.play(a.animate.shift(move))
        self.wait(1)
