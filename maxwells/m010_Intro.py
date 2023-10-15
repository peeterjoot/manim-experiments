from helper import *

class m010_Intro( Scene ):
    def construct( self ):

        title = Text( "Maxwell's equation in geometric algebra." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 5 )

        fadeall( self )

# vim: et sw=4 ts=4
