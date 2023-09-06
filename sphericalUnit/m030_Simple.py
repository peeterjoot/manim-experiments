from helper import *

class m030_Simple( Scene ):
    def construct( self ):

        title = Text( 'Radial unit derivative: niave approach.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( rhat_prime, " = ", l.frac( 'd', 'dt' ), '(', vec_r, '/r)' ) ),
               #MathTex( concat(             " = ", prime(vec_r), "/r  - r'", vec_r, "/r^2" ) ),
               MathTex(                    r" = { \mathbf{r}' \over r } - { \mathbf{r} \over r^2 }" ),
               MathTex( concat(             " = ", l.frac('1', 'r'), "(", prime(vec_r), " - r'", hat_r, " )" ) ),
               MathTex( r" = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \mathbf{r}' - r' )" ) ]

        eq2 = [ MathTex( r" = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \mathbf{r}' - \hat{\mathbf{r}} \cdot \mathbf{r}' )" ),
                MathTex( r" = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \wedge \mathbf{r}' )" ) ]
        eq[0].shift( 2 * UP + 3 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(3):
            sh = 1.25 * DOWN + 0.0 * RIGHT
            if i == 0:
                sh += 0.27 * RIGHT + 0.0 * DOWN
            #if i == 2:
            #    sh += 0.50 * DOWN
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        eq2[0].move_to( eq[0] ).shift( 5 * RIGHT )
        self.play( Write( eq2[0] ) )
        self.wait( 5 )

        for i in range(1):
            sh = 1.20 * DOWN + 0.0 * RIGHT
            #if i == 0:
            #    sh += 0.25 * RIGHT
            #if i == 2:
            #    sh += 0.50 * DOWN
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 5 )

        eq3 = MathTex( r"\hat{\mathbf{r}}' = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \wedge \mathbf{r}' )" ) 
        self.play( ReplacementTransform( VGroup(*eq, *eq2), eq3 ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
