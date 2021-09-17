from manim import *
import numpy as np
from mylatex import *

class ProjRej(Scene):
    def construct(self):
        l = latex()
        vecu       = l.vec('u')
        uhat       = l.hat('u')
        vecv       = l.vec('v')

        eq = MathTex( concat( vecv, r' &= ', vecv, r'\times 1', l.nextline ),
                      concat( r' &= ', vecv, uhat, uhat, l.nextline ),
                      concat( r' &= ', l.lr(vecv, uhat), uhat, l.nextline ),
                      concat( r' &= ', l.lr( concat( l.dot(vecv, uhat), ' + ', l.wedge(vecv, uhat) ) ), uhat, l.nextline ),
                      concat( r' &= ', l.lr( l.dot(vecv, uhat) ), uhat, ' + ', l.lr(l.wedge(vecv, uhat)), uhat, l.nextline )
                    )

        self.play( Write( eq[0] ) )
        self.play( Write( eq[1] ) )
        self.play( Write( eq[2] ) )
        self.play( Write( eq[3] ) )
        self.play( Write( eq[4] ) )
        self.wait( )
