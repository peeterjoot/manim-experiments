from helper import *

class m010_Intro( Scene ):
    def construct( self ):

        title = Text( 'Radial representations.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = MathTex( concat( vec_x, " = r ", hat_r ) )
        eq.shift( UP )
        self.play( Write( eq ) )
        self.wait( 5 )

        eq2 = MathTex( concat( vec_x, " = r' ", hat_r, " + r ", rhat_prime ) )
        eq2.move_to( eq ).shift( DOWN * 1.5 )
        self.play( Write( eq2 ) )
        self.wait( 5 )

        eq3 = MathTex( concat( rhat_prime, " = ?") )
        eq3.move_to( eq2 ).shift( DOWN * 1.5 )
        self.play( Write( eq3 ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
