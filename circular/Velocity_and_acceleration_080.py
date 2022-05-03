from helper import *

class Velocity_and_acceleration_080( Scene ):
    def construct( self ):

        title = Text( 'Velocity and acceleration.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
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

        eq3 = AcolorsMathTex( concat(        " = ", l.lr( dr_prime, r" - r \omega^2" ), hat_r, '+', l.lr( r"2 r' \omega + r \omega'"), hat_theta ) )
        eq3.move_to( eq2[i+1] )
        self.play( TransformMatchingTex( eq2[i+1], eq3 ) )
        self.wait( 5 )

        eq4 = AcolorsMathTex( concat(        " = ", l.lr( dr_prime, r" - r \omega^2" ), hat_r, '+', l.frac('1', 'r'), prime( l.lr( r'r^2 \omega' ) ), hat_theta ) )
        eq4.move_to( eq3 )
        eq4.shift( 0.3 * DOWN + 0.38 * LEFT )
        self.play( TransformMatchingTex( eq3, eq4 ) )
        self.wait( 5 )

        eq5 = AcolorsMathTex( concat( vec_v, " = ", r_prime, hat_r, r' + r \omega', hat_theta, r',\quad',
            vec_a,
            " = ", l.lr( dr_prime, r" - r \omega^2" ), hat_r, '+', l.frac('1', 'r'), prime( l.lr( r'r^2 \omega' ) ), hat_theta ) )

        all = VGroup( *eq, eq2[0], eq2[1], eq2[2], eq2[3], eq4 )
        self.play( TransformMatchingTex( all, eq5 ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
