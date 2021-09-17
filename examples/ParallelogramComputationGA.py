from manim import *
import numpy as np
from mylatex import *

class ParallelogramComputationGA(Scene):
    def construct(self):
        l = latex()
        vecu = r'\vec{u}'
        uhat = r'\hat{u}'
        vecv = r'\vec{v}'
        squ = l.sq( vecu )
        sqv = l.sq( vecv )
        vdotusq = l.lrsq( l.dot( vecv, uhat ) )
        vwedgeuhat = l.wedge( vecv, uhat )
        vwedgeu = l.wedge( vecv, vecu )
        uwedgev = l.wedge( vecu, vecv )
        rej = concat( l.lr( vwedgeuhat ), uhat )

        eq = MathTex( r'\text{Area} &= \text{base} \times \text{height} \\',
                      concat( r'{\text{Area}}^2 &= ', squ, l.lrsq( rej ), l.nextline ),
                      concat( '&= -', squ, l.lrsq( vwedgeuhat ), l.nextline ),
                      concat( '&= - ', l.lrsq( vwedgeu ), l.nextline ),
                      concat( '&= ', l.dot( l.lr(vwedgeu), l.lr(uwedgev) ), l.nextline ),
                      concat( '&= ', squ, sqv, '-', l.lrsq( l.dot( vecv, vecu ) ), l.nextline )
                    )

        self.play( Write( eq[0] ) )
        self.play( Write( eq[1] ) )
        self.play( Write( eq[2] ) )
        self.play( Write( eq[3] ) )
        self.play( Write( eq[4] ) )
        self.play( Write( eq[5] ) )
        self.wait( )
