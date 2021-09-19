from manim import *
import numpy as np
from sys import *
sys.path.append(r'../bin')
from mylatex import *

#   p1 + p2
#     /\
#    /  \
#   p2   \p1
#    \   /
#     \ /
#      o

class DrawParallelogram( Scene ):
    def construct( self ):
        l = latex( )
        u          = l.vec( 'u' )
        uhat       = l.hat( 'u' )
        v          = l.vec( 'v' )

        o = np.array( [0, -2, 0] )
        p1 = np.array( [3, 1, 0] )
        p2 = np.array( [1, 3, 0] )
        op1 = o + p1
        op2 = o + p2

        v1 = Arrow( start = o, end = op1, buff = 0, color = RED )
        v2 = Arrow( start = o, end = op2, buff = 0, color = YELLOW )

        v1l = MathTex( u )
        v2l = MathTex( v )
        v1l.set_color( RED )
        v1l.next_to( v1, RIGHT )
        v2l.next_to( v2, UP )
        v2l.set_color( YELLOW )

        p1cap = p1/ np.linalg.norm( p1 )
        proj = np.dot( p2, p1cap ) * p1cap
        oproj = o + proj
        vproj = Line( start = o, end = oproj, color = PURPLE )
        vprojl = MathTex( concat( l.lr( l.dot( v, uhat ) ), uhat ) )
        vprojl.next_to( vproj, DOWN )
        v1g = VGroup( v1, v1l )
        vprojg = VGroup( vproj, vprojl )

        rej = p2 - proj
        vrej = Line( start = oproj, end = op2, color = GREEN )
        vrejl = MathTex( concat( v, ' - ', l.lr( l.dot( v, uhat ) ), uhat ) )
        vrejl.next_to( vrej, RIGHT )
        vrejl.shift( (-0.5,0,0 ))
        v2g = VGroup( v2, v2l )
        vrejg = VGroup( vrej, vrejl )

        op3 = op1 + p2
        v1p = Arrow( start = op1, end = op3, buff = 0, color = YELLOW )
        v2p = Arrow( start = op2, end = op3, buff = 0, color = RED )
        #parallelogram = [o, op1, op3, op2]
        #poly = Polygon( *parallelogram )

        cut = op1 + rej
        recttop = cut - p1
        dashrej = DashedLine( start = op1, end = cut, color = BLUE )
        dashtop = DashedLine( start = cut, end = recttop )
        dashside = DashedLine( start = recttop, end = o, color = BLUE )

        self.play( Create( v1g ))
        self.play( Create( v2g ))
        v1c = v1.copy()
        v2c = v2.copy()
        self.add( v1c )
        self.add( v2c )
        self.play( ReplacementTransform( v1c, v1p ) )
        self.play( ReplacementTransform( v2c, v2p ) )
        #self.play( Create( poly ))
        self.play( Create( vprojg ))
        self.play( Create( vrejg ))
        self.play( Create( dashrej ))
        self.play( Create( dashtop ))
        self.play( Create( dashside ))
        self.play( FadeOut( vprojg, vrejg ))

        move = ( -6, 1, 0 )
        a = VGroup( dashrej, dashtop, dashside, v1, v1l, v2, v2l, v1p, v2p ) # , poly
        self.play( a.animate.shift( move ))
        self.wait( 1 )

        squ        = l.norm2( u )
        sqv        = l.norm2( v )
        vdotuhatsq = l.lrsq( l.dot( v, uhat ) )
        rej        = l.sub( v, l.mult( l.lr( l.dot( v, uhat ) ), uhat ) )

        eq2 = MathTex( l.text( 'base' ), r'& = \Vert', u, concat( r'\Vert', l.newline ),
                       l.text( 'height' ), '& = ', concat( l.norm( rej ), l.newline ) )

        eq = MathTex( concat( l.text( 'Area' ), r' &= ', l.text( 'base' ), r' \times ', l.text( 'height' ), l.newline ), # 0
                      concat( l.sq( l.text( 'Area' ) ), r' &= ', squ, l.norm2( rej ), l.newline ), # 1
                      concat( '&= ', squ ), concat( l.lr( l.add( sqv, vdotuhatsq ), l.neg( l.mult( '2', vdotuhatsq ) ) ), l.newline ), # 2,3
                      concat( '&= ', squ ), concat( l.lr( l.sub( sqv, vdotuhatsq ) ), l.newline ), # 4,5
                      concat( '&= ', l.sub( l.mult( squ, sqv ), l.lrsq( l.dot( v, u ) ) ), l.newline ) # 6
                    )

        eq.shift( 2.4 * RIGHT )
        eq2.shift( 3 * DOWN + 3 * LEFT )
        #eq2[0].set_color( RED )
        ##eq2[2].set_color( RED )
        #eq2[4].set_color( BLUE )
        self.play( Write( eq[0] ),
                   Write( eq2[0] ),
                   Write( eq2[1] ),
                   Write( eq2[2] ),
                   Write( eq2[3] ),
                   Write( eq2[4] ),
                   Write( eq2[5] ),
                   Write( eq2[6] ) )

        for i in range( 1, 4 ):
            self.play( Write( eq[i] ) )
        self.wait( )
        eq[5].shift( 1.1 * UP )

        self.play( ReplacementTransform( eq[3], eq[5] ) )
        self.wait( 2 )

        i = 6
        eq[i].shift( UP )
        self.play( Write( eq[i] ) )

        self.wait( )
