from helper import *

class m030_Simple( Scene ):
    def construct( self ):

        title = Text( 'Radial unit derivative: naive approach.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( concat( rhat_prime,r" = { d \over dt } { \mathbf{x} \over r }" ) ),
               MathTex(                    r" = { \mathbf{x}' \over r } - { {r' \mathbf{x}} \over r^2 }" ),
               MathTex( concat(             " = ", l.frac('1', 'r'), "(", prime(vec_x), " - r'", hat_r, " )" ) ),
               MathTex( r" = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \mathbf{x}' - r' )" ) ]

        eq2 = [ MathTex( r" = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \mathbf{x}' - \hat{\mathbf{r}} \cdot \mathbf{x}' )" ),
                MathTex( r" = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \wedge \mathbf{x}' )" ) ]
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

        eq3 = MathTex( r"\hat{\mathbf{r}}' = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \wedge \mathbf{x}' )" ) 
        self.play( ReplacementTransform( VGroup(*eq, *eq2), eq3 ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
