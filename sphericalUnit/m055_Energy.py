from helper import *

class m055_Energy( Scene ):
    def construct( self ):

        title = Text( 'Kinetic energy.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( r"\mathbf{v} = r' \hat{\mathbf{r}} + \hat{\mathbf{r}} ( \hat{\mathbf{r}} \wedge \mathbf{v} )" ),
               MathTex( r"{ m \over 2 } \mathbf{v}^2 = { m \over 2 } (r'){}^2 + { m \over 2 } (\hat{\mathbf{r}} ( \hat{\mathbf{r}} \wedge \mathbf{v} )){}^2" ),
               MathTex(                            r"= { m \over 2 } (r'){}^2 + { 1 \over {2mr^2} } (\hat{\mathbf{r}} ( \mathbf{r} \wedge (m\mathbf{v}) )){}^2" ),
               MathTex( r"\mathrm{Let}\, L = \mathbf{r} \wedge (m\mathbf{v}) = \mathbf{r} \wedge \mathbf{p}" ) ]

        eq[0].shift( 2 * UP + 3 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )
        for i in range(3):
            sh = 1.20 * DOWN + 0.0 * RIGHT
            if i == 1:
                sh += 1.22 * RIGHT + 0.0 * DOWN
            if i == 2:
                sh += 1.1  * LEFT + 0.0 * DOWN
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        eq2 = [ MathTex( r"\mathbf{v} = r' \hat{\mathbf{r}} + \hat{\mathbf{r}} ( \hat{\mathbf{r}} \wedge \mathbf{v} ), \quad L = \mathbf{r} \wedge \mathbf{p}" ),
                MathTex( r"{ m \over 2 } \mathbf{v}^2 = { m \over 2 } (r'){}^2 + { 1 \over {2 m r^2} } \hat{\mathbf{r}} L \hat{\mathbf{r}} L" ),
                MathTex( r"                           = { m \over 2 } (r'){}^2 - { 1 \over {2 m r^2} } \hat{\mathbf{r}} L^2 \hat{\mathbf{r}}" ),
                MathTex( r"                           = { m \over 2 } (r'){}^2 - { 1 \over {2 m r^2} } L^2 \hat{\mathbf{r}}{}^2" ),
                MathTex( r"                           = { m \over 2 } (r'){}^2 - { 1 \over {2 m r^2} } L^2" ) ]
        eq2[0].move_to( eq[0] ).shift( 2.0 * RIGHT )
        self.play( ReplacementTransform( VGroup(*eq), eq2[0] ) )
        self.wait( 5 )
        for i in range(4):
            sh = 1.20 * DOWN + 0.0 * RIGHT
            if i == 1:
                sh += 1.20 * RIGHT + 0.0 * DOWN
            write_aligned( self, eq2[i], eq2[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
