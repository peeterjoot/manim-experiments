from manim import *
import numpy as np
from mylatex import *

class ParallelogramComputationClassic(Scene):
    def construct(self):
        l = latex()
        vecu = r'\vec{u}'
        uhat = r'\hat{u}'
        vecv = r'\vec{v}'
        squ = l.mknorm2( vecu )
        sqv = l.mknorm2( vecv )
        vdotusq = l.lrsq( l.dot( vecv, uhat ) )
        rej = concat( vecv, '-', l.lbr, l.dot( vecv, uhat ), l.rbr, uhat )

        eq = MathTex( r'\text{Area} &= \text{base} \times \text{height} \\',
                      concat( r'{\text{Area}}^2 &= ', squ, l.mknorm2( rej ), l.nextline ),
                      concat( '&= ', squ, l.lbr, sqv, ' + ', vdotusq, '- 2 ', vdotusq, l.rbr, l.nextline ),
                      concat( '&= ', squ, l.lbr, sqv, ' - ', vdotusq, l.rbr, l.nextline ),
                      concat( '&= ', squ, sqv, ' - ', l.lrsq( l.dot( vecv, vecu ) ), l.nextline )
                    )

        self.play( Write( eq[0] ) )
        self.play( Write( eq[1] ) )
        self.play( Write( eq[2] ) )
        self.play( Write( eq[3] ) )
        self.play( Write( eq[4] ) )
        self.wait( )
