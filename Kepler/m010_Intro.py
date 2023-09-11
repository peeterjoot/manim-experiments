from helper import *

class m010_Intro( Scene ):
    def construct( self ):

        title = Text( 'Elliptical orbital motion from gravitational law.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 10 )

        eq = MathTex( r"\mathbf{F} = - { {G m M} \over r^2 } \mathbf{\hat{r}}" )
        eq.shift( 0.50 * DOWN + 3 * RIGHT )
        self.play( Write( eq ) )
        self.wait( 10 )

        fadeall( self )

# vim: et sw=4 ts=4
