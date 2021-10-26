# https://stackoverflow.com/questions/69702890/using-transform-and-replacementtransform-in-manim

from manim import *

class foo( Scene ):
    def construct( self ):

        lines1 = MathTex(r'\frac{1}{2}', r'\divisionsymbol', r'\frac{2}{3}')
        lines2 = MathTex(r'2 \divisionsymbol 3')
        lines3 = MathTex(r'\frac{2}{1} \times \frac{1}{3}')

        lines2.move_to(lines1[2], RIGHT)
        lines2.shift(RIGHT)
        lines3.move_to(lines2)
        self.play(Write(lines1))
        self.play(ReplacementTransform(lines1[2], lines2))
        #self.wait(1)
        self.play(ReplacementTransform(lines2, lines3))
        #self.wait(3)


# vim: et sw=4 ts=4
