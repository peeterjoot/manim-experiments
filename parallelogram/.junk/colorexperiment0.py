from manim import *
import numpy as np
from mylatex import *

class ProjRej(Scene):
    def construct(self):
        l = latex()
        u          = l.vec('u')
        v          = l.vec('v')
        a          = l.vec('a')
        b          = l.vec('b')

        eq = MathTex( 
                l.norm2( v ), l.norm2( u ), l.neg( l.lrsq( l.dot( u, v ) ) ),
                l.norm2( b ), l.norm2( a ), l.neg( l.lrsq( l.dot( a, b ) ) )
                )
        eq.set_color_by_tex_to_color_map( { 
                  "u": RED, "v": YELLOW,
                  "a": RED, "b": YELLOW 
                  } )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
