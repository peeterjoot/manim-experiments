from manim import *
import numpy as np
from mylatex import *

class ParallelogramComputationGA(Scene):
    def construct(self):
        l = latex()
        vecu       = l.vec('u')
        uhat       = l.hat('u')
        vecv       = l.vec('v')
        squ        = l.sq( vecu )
        sqv        = l.sq( vecv )
        vdotuhatsq = l.lrsq( l.dot( vecv, uhat ) )
        vwedgeuhat = l.wedge( vecv, uhat )
        vwedgeu    = l.wedge( vecv, vecu )
        uwedgev    = l.wedge( vecu, vecv )
        rej        = concat( l.lr( vwedgeuhat ), uhat )

        eq = MathTex( concat( l.text('Area'), r' &= ', l.text('base'), r' \times ', l.text('height'), l.nextline ),
                      concat( l.sq(l.text('Area')), r' &= ', squ, l.lrsq( rej ), l.nextline ),
                      concat( '&= -', squ, l.lrsq( vwedgeuhat ), l.nextline ),
                      concat( '&= - ', l.lrsq( vwedgeu ), l.nextline ),
                      concat( '&= ', l.dot( l.lr(vwedgeu), l.lr(uwedgev) ), l.nextline ),
                      concat( '&= ', squ, sqv, '-', l.lrsq( l.dot( vecv, vecu ) ), l.nextline )
                    )

        for item in eq:
            self.play( Write( item ) )
        self.wait( )
