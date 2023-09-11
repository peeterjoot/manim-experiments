from helper import *

class m060_Summary( Scene ):
    def construct( self ):

        title = Text( 'Summary.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( r"\mathbf{x} = r \hat{\mathbf{r}}, \quad \mathbf{x}' = r' \hat{\mathbf{r}} + r \hat{\mathbf{r}}'" ),
               MathTex( "\hat{\mathbf{r}}' = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \wedge \mathbf{x}' )" ),
               MathTex(                  r"= { 1 \over r } \mathrm{Rej}_{\hat{\mathbf{r}}} \mathbf{x}'" ),
               MathTex(                  r"= {1 \over r} ( \hat{\mathbf{r}} \times \mathbf{x}' ) \times \hat{\mathbf{r}}" ),
               MathTex( r"{ m \over 2 } \mathbf{v}^2 = { 1 \over {2m} } (m r'){}^2 - { 1 \over {2 m r^2} } L^2, \quad L = \mathbf{r} \wedge \mathbf{p}" ) ]

        eq[0].shift( 2 * UP + 1 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )
        for i in range(4):
            sh = 1.20 * DOWN + 0.0 * RIGHT
            if i == 0:
                sh += 0.00 * RIGHT + 0.0 * DOWN
            if i == 1:
                sh += 0.55 * RIGHT + 0.0 * DOWN
            if i == 3:
                sh += 1.20 * LEFT + 0.0 * DOWN
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
