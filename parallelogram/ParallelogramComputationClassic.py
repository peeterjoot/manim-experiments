from manim import *
import numpy as np
from mylatex import *

class ParallelogramComputationClassic(Scene):
    def construct(self):
        l = latex()
        u          = l.vec('u')
        uhat       = l.hat('u')
        v          = l.vec('v')
        squ        = l.mknorm2( u )
        sqv        = l.mknorm2( v )
        vdotuhatsq = l.lrsq( l.dot( v, uhat ) )
        rej        = concat( v, '-', l.lbr, l.dot( v, uhat ), l.rbr, uhat )

        eq = MathTex( concat( l.text('Area'), r' &= ', l.text('base'), r' \times ', l.text('height'), l.nextline ),
                      concat( l.sq(l.text('Area')), r' &= ', squ, l.mknorm2( rej ), l.nextline ),
                      concat( '&= ', squ, l.lbr, sqv, ' + ', vdotuhatsq, '- 2 ', vdotuhatsq, l.rbr, l.nextline ),
                      concat( '&= ', squ, l.lbr, sqv, ' - ', vdotuhatsq, l.rbr, l.nextline ),
                      concat( '&= ', squ, sqv, ' - ', l.lrsq( l.dot( v, u ) ), l.nextline )
                    )

        for item in eq:
            self.play( Write( item ) )
        self.wait( )
