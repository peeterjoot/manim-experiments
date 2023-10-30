from mycolors import *

class m010_Intro( Scene ):
    def construct( self ):

        title = Text( "Foo." )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.play( FadeIn( title ) )
        self.wait( 1 )

        fadeall( self )

# vim: et sw=4 ts=4
