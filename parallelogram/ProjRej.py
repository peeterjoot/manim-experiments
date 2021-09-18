from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex import *

class ProjRej(Scene):
    def construct(self):
        l = latex()
        u          = l.vec('u')
        uhat       = l.hat('u')
        v          = l.vec('v')
        proj       = l.mult( l.lr( l.dot(v, uhat) ), uhat )
        rej        = l.mult( l.lr( l.wedge(v, uhat) ), uhat )

        eq = MathTex( concat( v, r' &= ', v, r'\times 1', l.newline ),
                      concat( r' &= ', v, uhat, uhat, l.newline ),
                      concat( r' &= ', l.lr(v, uhat), uhat, l.newline ),
                      concat( r' &= ', l.lr( l.add( l.dot(v, uhat), l.wedge(v, uhat) ) ), uhat, l.newline ),
                      concat( r' &= ', l.add( proj, rej ), l.newline ),
                      concat( l.Proj(u, v), ' &\equiv ', proj, l.newline ),
                      concat( l.Rej(u, v),  ' &\equiv ', rej, l.newline )
                    )

        for item in eq:
           self.play( Write( item ) )

        self.wait( )
