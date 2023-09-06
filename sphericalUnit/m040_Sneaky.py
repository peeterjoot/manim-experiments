from helper import *

class m040_Sneaky( Scene ):
    def construct( self ):

        title = Text( 'Radial unit derivative: sneaky approach.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        # TODO
        eq = [ MathTex( concat( rhat_prime, " = ", l.frac( 'd', 'dt' ), '(', vec_r, '/r)' ) ) ]
        #       MathTex(                    r" = { \mathbf{r}' \over r } - { \mathbf{r} \over r^2 }" ),
        #       MathTex( concat(             " = ", l.frac('1', 'r'), "(", prime(vec_r), " - r'", hat_r, " )" ) ),
        #       MathTex( r" = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \mathbf{r}' - r' )" ) ]
        eq[0].shift( 2 * UP + 0 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
