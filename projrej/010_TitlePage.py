from helper import *

class TitlePage( Scene ):
    def construct( self ):
        t = Text( "Geometric algebra: projection and rejection." )
        t.shift( 3 * DOWN )
        self.add( t )

        labels = DrawVectorsAndProjRej( self, 0, origin = [ 5, -3, 0 ] )
        self.wait( 5 )


# vim: et sw=4 ts=4
