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

        o = np.array( [0, -2, 0] )
        p1 = np.array( [3, 1, 0] )
        p2 = np.array( [1, 3, 0] )
        op1 = o + p1
        op2 = o + p2

        p1cap = p1/ np.linalg.norm( p1 )
        proj = np.dot( p2, p1cap ) * p1cap
        oproj = o + proj

        vproj = Line( start = o, end = oproj, color = PURPLE )
        vprojl = MathTex( concat( l.lr( l.dot( v, uhat ) ), uhat ) )
        vprojl.set_color( PURPLE )
        vprojl.next_to( vproj, DOWN )

        rej = p2 - proj
        vrej = Line( start = oproj, end = op2, color = GREEN )
        vrejl = MathTex( concat( l.lr( l.wedge( v, uhat ) ), uhat ) )
        vrejl.set_color( GREEN )
        vrejl.next_to( vrej, 0.2 * RIGHT )

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )
        v1l = MathTex( u )
        v1l.set_color( RED )
        v1l.next_to( v1, RIGHT )
        v2l = MathTex( v )
        v2l.set_color( YELLOW )
        v2l.next_to( v2, UP )

        all = VGroup( v1, v1l, v2, v2l, vproj, vrej, vprojl, vrejl )
        move = ( -6.5, 2, 0 )
        all.shift( move )

        self.add( all )


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

        eq.shift( 2.4 * RIGHT )

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
