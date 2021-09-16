from manim import *
import numpy as np
#from operator import add, sub
#import math as libm

def mknorm(v):
    return r'\left\lVert{' + v + r'}\right\rVert'
def mknorm2(v):
    return r'{\left\lVert{' + v + r'}\right\rVert}^2'
def lr(v):
    return r'\left( ' + v + r' \right)'

#   p1 + p2
#     /\
#    /  \
#   p2   \p1
#    \   /
#     \ /
#      o

class DrawParallelogram(Scene):
    def construct(self):
        o = np.array([0, -2, 0])
        p1 = np.array([2, 1, 0])
        p2 = np.array([-0.5, 3, 0])
        op1 = o + p1
        op2 = o + p2

        v1 = Arrow(start=o, end=op1, buff=0)
        v2 = Arrow(start=o, end=op2, buff=0)

        v1l = Tex(r'$\vec{u}$').scale(1)
        v2l = Tex(r'$\vec{v}$').scale(1)
        v1l.next_to(v1, RIGHT)
        v2l.next_to(v2, UP)

        p1cap = p1/ np.linalg.norm(p1)
        proj = np.dot(p2, p1cap) * p1cap
        oproj = o + proj
        vproj = Line(start=o, end=oproj, color=RED)
        vprojl = Tex(r'$\left(\vec{v} \cdot \hat{u}\right) \hat{u}$').scale(1)
        vprojl.next_to(vproj, DOWN)
        v1g = VGroup(v1, v1l)
        vprojg = VGroup(vproj, vprojl)

        rej = p2 - proj
        vrej = Line(start=oproj, end=op2, color=RED)
        vrejl = Tex(r'$\vec{v} - \left(\vec{v} \cdot \hat{u}\right) \hat{u}$').scale(1)
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

#class ParallelogramComputationClassic(Scene):
#    def construct(self):
#        line1a = Tex(r'$\text{Area}$').scale(1)
#        line1b = Tex('$=$').scale(1)
#        line1c = Tex(r'$\text{base} \times \text{height}$').scale(1)
#        line1a.next_to(a, 4*RIGHT + UP/2)
#        line1b.next_to(line1a, RIGHT)
#        line1c.next_to(line1b, RIGHT)
#
#        line2a = Tex(r'$\text{base}^2$').scale(1)
#        line2b = line1a.copy()
#        line2c = Tex('$' + mknorm2(r'\vec{u}') + '$').scale(1)
#        #line2a.shift(DOWN)
#        #line2b.shift(DOWN)
#        #line2c.shift(DOWN)
#        line2a.align_to(line1a,DOWN)
#        line2b.align_to(line1b,DOWN)
#        line2c.align_to(line1c,DOWN)
#
#        #line2.next_to(line1, DOWN)
#        #line3a = Tex(r'$\text{height}^2 = $')
#        #line3b1 = Tex(r'$' + mknorm2(r'\vec{v} - \left(\vec{v} \cdot \hat{u}\right) \hat{u}') + r'$').scale(1)
#        #line3a.next_to(line2, DOWN)
#        #line3b1.next_to(line3a, RIGHT)
#        #line3b2 = Tex(r'$' + mknorm2(r'\vec{v}')
#        #        + r'+ {\left(\vec{v} \cdot \hat{u}\right)}^2 -2 {\left(\vec{v} \cdot \hat{u}\right)}^2 $').scale(1)
#        #line3b2.next_to(line3a, RIGHT)
#        #line3b3 = Tex(r'$' + mknorm2(r'\vec{v}') + r'-{\left(\vec{v} \cdot \hat{u}\right)}^2 $').scale(1)
#        #line3b3.next_to(line3a, RIGHT)
#        self.add(Write(line1a), Write(line1b), Write(line1c))
#        #self.wait(1)
#        self.add(Write(line2a), Write(line2b), Write(line2c))
#        self.wait(1)
#        #self.play(Write(line3a))
#        #self.play(Write(line3b1))
#        #self.play(FadeOut(line3b1))
#        #self.play(Write(line3b2))
#        #self.play(FadeOut(line3b2))
#        #self.play(Write(line3b3))
#        #self.play(Write(line4))
#        #self.play(Write(line1), Write(line2), Write(line3))
#        self.wait(1)
