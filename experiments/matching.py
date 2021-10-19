from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex import *

# also:
# https://infograph.tistory.com/27

class MatchingEquationParts(Scene):
    def construct(self):
        l = latex( )
        veca = l.doublebr( l.vec('a') )
        vecb = l.doublebr( l.vec('b') )
        vecc = l.doublebr( l.vec('c') )
        print( veca )
        print( vecb )
        print( vecc )
        colors = { l.vec('a'): YELLOW,
                   l.vec('b'): RED,
                   l.vec('c'): BLUE }
        eq1 = MathTex( veca, ' + ', vecb, ' = ', vecc, tex_to_color_map = colors )
        eq2 = MathTex( veca, ' = ', vecc, ' - ', vecb, tex_to_color_map = colors )
        #eq1.set_color_by_tex( l.vec('a'), YELLOW )
        #eq1.set_color_by_tex( l.vec('b'), RED )
        #eq1.set_color_by_tex( l.vec('c'), BLUE )
        #eq2.set_color_by_tex( l.vec('a'), YELLOW )
        #eq2.set_color_by_tex( l.vec('b'), RED )
        #eq2.set_color_by_tex( l.vec('c'), BLUE )

        #eq1 = MathTex("{", "a_{1}", r"\over", "b_{1}", "}", " = ", "{", "a_{2}", r"\over", "b_{2}", "}")
        #eq1.set_color_by_tex("a_{1}", color=RED, substring=False)
        #eq1.set_color_by_tex("a_{2}", color=RED, substring=False)
        #eq1.set_color_by_tex("b_{1}", color=YELLOW, substring=False)
        #eq1.set_color_by_tex("b_{2}", color=YELLOW, substring=False)

        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(0.5)

# vim: et sw=4 ts=4
