from helper import *

class m010_GAvectorProduct( Scene ):
    def construct( self ):

        title = Text( '2D Geometric algebra: Vector product.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = AcolorsMathTex( concat( l.text('Given '), vec_x, ' = a ', vec_e1, ' + b ', vec_e2, ', ',
                                     vec_y, ' = c ', vec_e1, ' + d ', vec_e2 ) )

        eq.move_to( UP * 2.0 )
        self.play( Write( eq ) )
        self.wait( 5 )

        eq2 = [ AcolorsMathTex( concat( vec_x, vec_y, ' = ', l.lr( 'a ', vec_e1, ' + b ', vec_e2 ), l.lr( 'c ', vec_e1, ' + d ', vec_e2 ) ) ),
                AcolorsMathTex( concat(               ' = a c', l.sq( vec_e1 ), ' + b d', l.sq( vec_e2 ), '+ a d', vec_e1, vec_e2, ' + b c', vec_e2, vec_e1 ) ),
                AcolorsMathTex( concat(               ' = a c + b d', '+ (a d - b c)', vec_e1, vec_e2 ) ) ]
        eq2[0].shift( 1.0 * UP )

        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        for i in range(1):
            write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
            self.wait( 7 )
        self.wait( 5 )

        eq3 = [ MathTex( concat( l.sq( vec_e1 ), ' = 1' ) ),
                MathTex( concat( l.sq( vec_e2 ), ' = 1' ) ),
                MathTex( concat( vec_e2, vec_e1, ' = -', vec_e1, vec_e2 ) ) ]
        eq3[0].move_to( LEFT * 5.0 + DOWN * 1.5 )
        self.play( Write( eq3[0] ) )
        self.wait( 5 )
        for i in range(2):
            write_aligned( self, eq3[i], eq3[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
            self.wait( 7 )
        self.wait( 5 )
        g3 = VGroup( *eq3 )
        self.play( FadeOut( g3 ) )

        for i in range(1, 2):
            write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
            self.wait( 7 )
        self.wait( 5 )
        eq2p = AcolorsMathTex( concat( vec_x, vec_y, ' = a c + b d', '+ (a d - b c)', vec_e1, vec_e2 ) )
        eq2p.move_to( eq2[0] )
        self.play( ReplacementTransform( VGroup(*eq2), eq2p ) )

        eq4 = [ AcolorsMathTex( concat( vec_x, vec_y, ' = ', l.gpgradezero( vec_x, vec_y ), '+', l.gpgradetwo( vec_x, vec_y ) ) ),
                AcolorsMathTex( concat( l.gpgradezero( vec_x, vec_y ), '=', l.dot( vec_x, vec_y ), ' = a c + b d' ) ),
                AcolorsMathTex( concat( l.gpgradetwo( vec_x, vec_y ), '=', l.wedge( vec_x, vec_y ), '=', l.det22( 'a', 'b', 'c', 'd' ), vec_e1, vec_e2 ) ) ]
        eq4[0].shift( 0.0 * UP )
        self.play( Write( eq4[0] ) )
        self.wait( 5 )
        for i in range(2):
            write_aligned( self, eq4[i], eq4[i+1], 1.25 * DOWN + 1.0 * LEFT, None )
            self.wait( 7 )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
