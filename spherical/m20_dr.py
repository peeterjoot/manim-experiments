from helper import *

class m20_dr( Scene ):
    def construct( self ):

        title = Text( 'Radial unit vector' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( r'\hat{\mathbf{r}} \propto', l.frac( r'\partial \mathbf{x}', r'\partial r') ) ) ]
        eq[0].shift( 1 * UP + 0.00 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        eq2 = [ MathTex( concat( l.frac( r'\partial \mathbf{x}', r'\partial r'), ' = ', vec_e3, r'e^{j\theta}' ) ) ]
        eq2[0].move_to( eq[0] ).shift( 1.50 * DOWN )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )

        eq3 = [ MathTex( concat( r'\hat{\mathbf{r}} =', vec_e3, r'e^{j\theta}' ) ) ]
        eq3[0].move_to( eq2[0] ).shift( 1.50 * DOWN )
        self.play( Write( eq3[0] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
