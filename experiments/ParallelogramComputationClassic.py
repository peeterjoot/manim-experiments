from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
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

        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ, l.norm2( rej ), l.newline ), # 1
                      concat( '&= ', squ), concat( l.lr( l.add( sqv, vdotuhatsq ), l.neg( l.mult( '2', vdotuhatsq ) ) ), l.newline ), # 2,3
                      concat( '&= ', squ), concat( l.lr( l.sub( sqv, vdotuhatsq ) ), l.newline ), # 4,5
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.lrsq( l.dot( v, u ) ) ), l.newline ) # 6
                    )

        for i in range( 4 ):
            self.play( Write( eq[i] ) )
        self.wait( )
        eq[5].shift( 1.1 * UP )

        self.play( ReplacementTransform( eq[3], eq[5] ) )
        self.wait( 2 )

        i=6
        eq[i].shift( UP )
        self.play( Write( eq[i] ) )

        self.wait( )
