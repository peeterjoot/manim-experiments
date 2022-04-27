from helper import *

class Derivatives_015( Scene ):
    def construct( self ):

        title = Text( 'Unit vector derivatives.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 5 )

        tprime = prime(r'\theta')

        eq = [ AcolorsMathTex( concat( prime(hat_r), r' = ', l.frac('d', 'dt'), vec_e1, r'e^{i\theta}') ),
               AcolorsMathTex( concat(               ' = ', vec_e1, r'e^{i\theta} i', tprime ) ),
               AcolorsMathTex( concat(               ' = ', hat_r, 'i', tprime ) ),
               AcolorsMathTex( concat(               r' = \omega', hat_theta ) ) ]

        eq[0].shift( 1.5 * UP + 3 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        i = 0
        write_aligned( self, eq[i], eq[i+1], 1.15 * DOWN + 0.30 * RIGHT, None )
        self.wait( 5 )
        i = 1
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )
        i = 2
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )

        eq2 = [ AcolorsMathTex( concat( prime(hat_theta), r' = ', l.frac('d', 'dt'), vec_e1, r'e^{i\theta} i') ),
                AcolorsMathTex( concat(                    ' = ', vec_e1, r'e^{i\theta} i^2', tprime ) ),
                AcolorsMathTex( concat(                    ' = - ', hat_r, tprime ) ),
                AcolorsMathTex( concat(                   r' = - \omega', hat_r ) ) ]

        eq2[0].shift( 1.5 * UP + 3 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )

        i = 0
        write_aligned( self, eq2[i], eq2[i+1], 1.15 * DOWN + 0.30 * RIGHT, None )
        self.wait( 5 )
        i = 1
        write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )
        i = 2
        write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )


# vim: et sw=4 ts=4
