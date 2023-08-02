from helper import *

class Multivector_40 ( Scene ):
    def construct( self ):

        title = Text( '2D Geometric algebra: The multivector.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = AcolorsMathTex( concat( r'M = \alpha + ', '+ a ', vec_e1, ' + b ', vec_e2, r' + \beta', vec_e1, vec_e2 ) );
        eq.move_to( UP * 2.0 )
        self.play( Write( eq ) )
        self.wait( 5 )

        #eq2 = 

        fadeall( self )

# vim: et sw=4 ts=4
