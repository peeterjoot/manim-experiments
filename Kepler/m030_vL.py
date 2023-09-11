from helper import *

class m030_vL( Scene ):
    def construct( self ):

        title = MathTex( r"\mbox{What is this}\, \mathbf{v} L\, \mbox{multivector?}" )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        eq = [ MathTex( r"\mathbf{\hat{r}} = -{1 \over {G m M} } \mathbf{v} L - \mathbf{e}" ) ]
        self.play( Write( eq[0] ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
