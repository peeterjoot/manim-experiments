from helper import *

class mxx_test( Scene ):
    def construct( self ):

        title = Text( 'Radial unit derivative: niave approach.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ 
               #MathTex( concat(             " = ", l.frac( hat_r, "r" ), "(", hat_r, prime(vec_r), " - r' )" ) )
               MathTex( r" = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \mathbf{r}' - r' )" )
             ]
        eq[0].shift( UP )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
