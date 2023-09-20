from helper import *

class m050_summary( Scene ):
    def construct( self ):

        title = Text( r"Summary." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 2 )

        fadeall( self )

# vim: et sw=4 ts=4
