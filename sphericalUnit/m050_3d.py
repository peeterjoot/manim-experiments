from helper import *

class m050_3d( Scene ):
    def construct( self ):

        title = Text( 'Radial unit derivative: triple vector cross product.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( r"\hat{\mathbf{r}}' = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \wedge \mathbf{x}' )" ),
               MathTex( concat(           r"= {1 \over r}", l.gpgradeone( r" \hat{\mathbf{r}} ( \hat{\mathbf{r}} \wedge \mathbf{x}' )" ) ) ),
               MathTex( concat(           r"= {1 \over r}", l.gpgradeone( r" \hat{\mathbf{r}} I ( \hat{\mathbf{r}} \times \mathbf{x}' )" ) ) ),
               MathTex( concat(           r"= {1 \over r}", l.gpgradeone( r" I^2 \hat{\mathbf{r}} \times ( \hat{\mathbf{r}} \times \mathbf{x}' )" ) ) ),
               MathTex( concat(           r"= {1 \over r}", r"( \hat{\mathbf{r}} \times \mathbf{x}' ) \times \hat{\mathbf{r}} " ) ) ]
        eq[0].shift( 2 * UP + 1 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )
        for i in range(4):
            sh = 1.20 * DOWN + 0.0 * RIGHT
            if i == 0:
                sh += 0.55 * RIGHT + 0.0 * DOWN
            #if i == 3:
            #    sh += 0.50 * LEFT + 0.0 * DOWN
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
