from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex import *

class RejIsScalar(Scene):
    def construct(self):
        l = latex()
        uhat       = l.hat( 'u' )
        u          = l.vec( 'u' )
        v          = l.vec( 'v' )
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble( r'\usepackage{cancel}' )

        eq = MathTex(
                l.Rej( u, v ), r' &\equiv ', l.lr( l.wedge( v, uhat ) ), uhat, l.nextline,
                r'&= ', l.add( l.dot( l.lr( l.wedge( v, uhat ) ), uhat, l.wedge( l.lr( l.wedge( v, uhat ) ), uhat ), l.nextline,
                r'&= ', l.add( l.dot( l.lr( l.wedge( v, uhat ) ), uhat), l.wedge( v, l.cancel( l.wedge( uhat, uhat ) ) ), l.nextline,
                r'&= ', l.dot( l.lr( l.wedge( v, uhat ) ), uhat, l.nextline,
                r'&= ', v, l.sub( l.lr( l.dot( uhat, uhat ) ), l.mult( uhat, l.lr( l.dot( v, uhat) ) ), l.nextline,
                r'&= ', v, l.neg( uhat, l.lr( l.dot( v, uhat ) ), l.nextline,
                      tex_template = myTemplate )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
