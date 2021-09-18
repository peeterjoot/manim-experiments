from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex import *

class ParallelogramComputationGA(Scene):
    def construct(self):
        l = latex()
        u          = l.vec( 'u' )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )
        squ        = l.sq( u )
        sqv        = l.sq( v )
        vdotuhatsq = l.lrsq( l.dot( v, uhat ) )
        vwedgeu    = l.wedge( v, u )
        uwedgev    = l.wedge( u, v )
        rej        = l.mult( l.lr( l.wedge( v, uhat ) ), uhat )
        rrej       = l.mult( uhat, l.lr( l.wedge( uhat, v ) ) )

        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ ), concat( l.lrsq( rej ), l.newline ), # 1,2
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ ), concat( rej, rrej, l.newline ), # 3,4
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ ), concat( l.lr( l.wedge( v, uhat ) ), l.lr( l.wedge( uhat, v ) ), l.newline ), # 5,6
                      concat( '&= ', l.lr( l.wedge( v, u ) ), l.lr( l.wedge( u, v ) ), ' = ', l.neg( l.lrsq( l.wedge( v, u ) ) ), l.newline ),
                      #concat( '&= ', l.neg( l.lrsq( vwedgeu )), l.newline ),
                      concat( '&= ', l.dot( l.lr( vwedgeu ), l.lr( uwedgev ) ), l.newline ),
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.lrsq( l.dot( v, u ) ) ), l.newline )
                    )

        for i in range( 3 ):
            self.play( Write( eq[i] ) )
        eq[4].shift( 0.8 * UP )
        eq[6].shift( 2 * 0.8 * UP )

        self.play( ReplacementTransform( eq[2], eq[4] ) )
        self.wait( )
        self.play( ReplacementTransform( eq[4], eq[6] ) )
        self.wait( )

        for i in range( 7, 10 ):
            eq[i].shift( 2 * 0.8 * UP )
            self.play( Write( eq[i] ) )

        self.wait( )
