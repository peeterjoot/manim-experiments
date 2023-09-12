from helper import *

class m050_summary( Scene ):
    def construct( self ):

        title = Text( r"Summary." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        eq = [ MathTex( r"\mathbf{\hat{r}} = -{1 \over {G m^2 M} } \mathbf{p} L - \mathbf{e}" ),
               MathTex( concat( r"r = -{1 \over {G m^2 M} }", l.gpgradezero( " (\mathbf{x} \cdot \mathbf{p} + \mathbf{x} \wedge \mathbf{p}) L " ), r" - r e \cos\theta" ) ) ]
        eq[0].shift( 1.50 * UP + 0.00 * RIGHT )
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
