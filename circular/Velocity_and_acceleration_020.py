from helper import *

class Velocity_and_acceleration_020( Scene ):
    def construct( self ):

        title = Text( 'Velocity and acceleration.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 5 )

        eq = [ AcolorsMathTex( concat( vec_v, " = ", r_prime, hat_r, ' + r ', rhat_prime ) ),
               AcolorsMathTex( concat(        " = ", r_prime, hat_r, r' + r \omega', hat_theta ) ) ]

        eq2 = [ AcolorsMathTex( concat( vec_a, " = ", prime( l.lr( r_prime, hat_r, ' + r ', rhat_prime ) ) ) ),
                AcolorsMathTex( concat(        " = ", dr_prime, hat_r, '+ 2', r_prime, rhat_prime, ' + r', dprime(hat_r) ) ),
                AcolorsMathTex( concat(        " = ", dr_prime, hat_r, '+ 2', r_prime, r'\omega', hat_theta, ' + r',
                    prime( l.lr( r'\omega', hat_theta ) ) ) ),
                AcolorsMathTex( concat(        " = ", dr_prime, hat_r, '+ 2', r_prime, r'\omega', hat_theta, r" + r \omega'", hat_theta,
                    r' + r \omega', that_prime ) ),
                AcolorsMathTex( concat(        " = ", dr_prime, hat_r, '+ 2', r_prime, r'\omega', hat_theta, r" + r \omega'", hat_theta,
                    r' - r \omega^2', hat_r ) ) ]

        eq[0].shift( 1.5 * UP + 4 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        i = 0
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN, None )
        self.wait( 5 )

        eq2[0].shift( 1.5 * UP + 0 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )
        i = 0
        write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN + 0.0 * LEFT, None )
        self.wait( 5 )
        i = 1
        write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN, None )
        self.wait( 5 )
        i = 2
        write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN, None )
        self.wait( 5 )
        i = 3
        write_aligned( self, eq2[i], eq2[i+1], 0.75 * DOWN, None )
        self.wait( 5 )


# vim: et sw=4 ts=4
