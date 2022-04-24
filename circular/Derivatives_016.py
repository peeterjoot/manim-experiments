from helper import *

class Derivatives_016( Scene ):
    def construct( self ):

        title = Text( '.' )
        title = Text( 'Tangential unit vector derivative.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 5 )

        tprime = prime(r'\theta')

        eq = [ AcolorsMathTex( concat( prime(hat_theta), r' = ', l.frac('d', 'dt'), vec_e2, r'e^{i\theta}') ),
               AcolorsMathTex( concat(               ' = ', vec_e2, r'i e^{i\theta}', tprime ) ),
               AcolorsMathTex( concat(               ' = -', vec_e1, r' e^{i\theta}', tprime ) ),
               AcolorsMathTex( concat(               r' = -\omega', hat_r ) ) ]

        eq[0].shift( 1.5 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        i = 0
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )
        i = 1
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )
        i = 2
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )


# vim: et sw=4 ts=4
