from helper import *

class m010_Intro( Scene ):
    def construct( self ):

        title = Text( "Wedge product, Cramer's rule, and least squares GA solution." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 20 )

        fadeall( self )

# vim: et sw=4 ts=4
