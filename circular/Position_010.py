from helper import *

class Position_010( Scene ):
    def construct( self ):

        title = Text( 'Circular velocity and acceleration.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 5 )

        eq = [ AcolorsMathTex( concat( vec_r, ' = r ', hat_r ) ),
               AcolorsMathTex( concat( hat_r, ' = ', vec_e1, r'e^{i\theta}' ) ),
               AcolorsMathTex( concat( 'i = ', vec_e1, vec_e2 ) ) ]

        eq[0].shift( 1.5 * UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        i = 0
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.5 * LEFT, None )
        self.wait( 5 )
        i = 1
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN + 0.5 * LEFT, None )
        self.wait( 5 )


# vim: et sw=4 ts=4
