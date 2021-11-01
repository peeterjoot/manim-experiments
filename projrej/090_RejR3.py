from helper import *

class RejR3( Scene ):
    def construct( self ):

        title = Tex( 'Rejection: $\mathbb{R}^3$ form.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        title.scale( 1.5 )
        self.add( title )

        eq = [ AcolorsMathTex( concat( l.Rej( vecu, vecv ), '=', l.lr( l.wedge( vecv, hatu ) ), hatu ) ),
               AcolorsMathTex( concat( '=', l.gpgradeone( l.lr( l.wedge( vecv, hatu ) ), hatu ) ) ),
               AcolorsMathTex( concat( '=', l.gpgradeone( 'I', l.lr( l.cross( vecv, hatu ) ), hatu ) ) ),
               AcolorsMathTex( concat( '=', l.gpgradeone( 'I',
                                                          l.lr( l.dot( l.lr( l.cross( vecv, hatu ) ), hatu ) ), '+',
                                                          l.lr( l.wedge( l.lr( l.cross( vecv, hatu ) ), hatu ) ) ) ) ),
               AcolorsMathTex( concat( '=', 'I',          l.lr( l.wedge( l.lr( l.cross( vecv, hatu ) ), hatu ) ) ) ),
               AcolorsMathTex( concat( '=', 'I^2',        l.cross( l.lr( l.cross( vecv, hatu ) ), hatu ) ) ),
               AcolorsMathTex( concat( '= -', l.cross( l.lr( l.cross( vecv, hatu ) ), hatu ) ) ),
               AcolorsMathTex( concat( '= ', l.cross( hatu, l.lr( l.cross( vecv, hatu ) ) ) ) ) ]

        self.play( Write( eq[0] ) )
        i = 0
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN, None )

        for i in range(1,7):
            tx_matching( self, eq[i], eq[i+1], 0.00 * DOWN, None )
            self.wait( 2 )

# vim: et sw=4 ts=4
