from helper import *

waittime = 5

class RejCross( Scene ):
    def construct( self ):

        title = Tex( 'Rejection: $\mathbb{R}^3$ cross product form.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        title.scale( 1.5 )
        self.add( title )

        vrejl = AcolorsMathTex( concat( 
            l.cross( hatu, l.lr( l.cross( vecv, hatu ) ) ), ' = ', 
            l.cross( hatu, 
                l.frac( l.cross( vecv, hatu ), l.norm( l.cross( vecv, hatu ) )
            ) ), r'\sin\theta' ) )

        self.add( all )
        self.wait( waittime )

# vim: et sw=4 ts=4
