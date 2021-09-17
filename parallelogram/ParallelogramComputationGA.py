from manim import *
import numpy as np
from mylatex import *

class ParallelogramComputationGA(Scene):
    def construct(self):
        l = latex()
        u          = l.vec('u')
        uhat       = l.hat('u')
        v          = l.vec('v')
        squ        = l.sq( u )
        sqv        = l.sq( v )
        vdotuhatsq = l.lrsq( l.dot( v, uhat ) )
        vwedgeuhat = l.wedge( v, uhat )
        vwedgeu    = l.wedge( v, u )
        uwedgev    = l.wedge( u, v )
        rej        = concat( l.lr( vwedgeuhat ), uhat )

        eq = MathTex( concat( l.text('Area'), r' &= ', l.text('base'), r' \times ', l.text('height'), l.nextline ),
                      concat( l.sq(l.text('Area')), r' &= ', squ, l.lrsq( rej ), l.nextline ),
                      concat( '&= -', squ, l.lrsq( vwedgeuhat ), l.nextline ),
                      concat( '&= - ', l.lrsq( vwedgeu ), l.nextline ),
                      concat( '&= ', l.dot( l.lr(vwedgeu), l.lr(uwedgev) ), l.nextline ),
                      concat( '&= ', squ, sqv, '-', l.lrsq( l.dot( v, u ) ), l.nextline )
                    )

        for item in eq:
            self.play( Write( item ) )
        self.wait( )
