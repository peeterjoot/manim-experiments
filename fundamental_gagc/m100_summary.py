from mycolors import *

class m100_summary( Scene ):
    def construct( self ):

        title = Text( "Summary." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 0.25 )

        fadeall( self )

# vim: et sw=4 ts=4
