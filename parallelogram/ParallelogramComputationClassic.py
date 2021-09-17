from manim import *
import numpy as np
from mylatex import *

class ParallelogramComputationClassic(Scene):
    def construct(self):
        l = latex()
        u          = l.vec( 'u' )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )
        squ        = l.norm2( u )
        sqv        = l.norm2( v )
        vdotuhatsq = l.lrsq( l.dot( v, uhat ) )
        rej        = l.sub( v, l.mult( l.lr( l.dot( v, uhat ) ), uhat) )

        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.nextline ),
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ, l.norm2( rej ), l.nextline ),
                      concat( '&= ', squ, l.lr( l.add( sqv, vdotuhatsq ), l.neg( l.mult( '2', vdotuhatsq ) ) ), l.nextline ),
                      concat( '&= ', squ, l.lr( l.sub( sqv, vdotuhatsq ) ), l.nextline ),
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.lrsq( l.dot( v, u ) ) ), l.nextline )
                    )

        for item in eq:
            self.play( Write( item ) )
        self.wait( )
