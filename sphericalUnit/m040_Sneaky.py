from helper import *

class m040_Sneaky( Scene ):
    def construct( self ):

        title = Text( 'Radial unit derivative: sneaky approach.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        eq = [ MathTex( r"\mathbf{x}' = \hat{\mathbf{r}} \hat{\mathbf{r}} \mathbf{x}'" ),
               MathTex(             r"= \hat{\mathbf{r}} ( \hat{\mathbf{r}} \cdot \mathbf{x}' + \hat{\mathbf{r}} \wedge \mathbf{x}' )" ),
               MathTex(             r"= \hat{\mathbf{r}} ( r' + \hat{\mathbf{r}} \wedge \mathbf{x}' )" ),
               MathTex(             r"= r' \hat{\mathbf{r}} + \hat{\mathbf{r}}( \hat{\mathbf{r}} \wedge \mathbf{x}')" ),
               MathTex( r"\mathrm{But:}\quad \mathbf{x}' = r' \hat{\mathbf{r}} + r \hat{\mathbf{r}}'" ) ]
        eq[0].shift( 2 * UP + 1 * LEFT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        for i in range(4):
            sh = 1.00 * DOWN + 0.0 * RIGHT
            if i == 0:
                sh += 0.52 * RIGHT + 0.0 * DOWN
            if i == 3:
                sh += 0.50 * LEFT + 0.0 * DOWN
            write_aligned( self, eq[i], eq[i+1], sh, None )
            self.wait( 5 )

        eq2 = MathTex( r"\hat{\mathbf{r}}' = { \hat{\mathbf{r}} \over r } ( \hat{\mathbf{r}} \wedge \mathbf{x}' )" )
        #eq2.shift( 1.0 * LEFT )
        self.play( ReplacementTransform( VGroup(*eq), eq2 ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
