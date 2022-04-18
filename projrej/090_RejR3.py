from helper import *

def explain(self, e):
    move = ( -4.0, -2, 0 )
    if e:
        g = VGroup( MathTex( e ) )
        g.move_to( move )
        g.set_color( RED )
        for t in g:
            self.play( FadeIn( t ) )
        self.wait( 1 )
        for t in g:
            self.play( FadeOut( t ) )
    else:
        self.wait( 1 )

class RejR3( Scene ):
    def construct( self ):

        title = Tex( 'Rejection: $\mathbb{R}^3$ form.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        title.scale( 1.5 )
        self.add( title )
        veca = l.vec( 'a' )
        vecb = l.vec( 'b' )

        eq = [ AcolorsMathTex( concat( l.Rej( vecu, vecv ), '=', hatu, l.lr( l.wedge( hatu, vecv ) ) ) ),               # 0
               AcolorsMathTex( concat( '=', l.gpgradeone( hatu, l.lr( l.wedge( hatu, vecv ) ) ) ) ),                    # 1
               AcolorsMathTex( concat( '=', l.gpgradeone( hatu, 'I', l.lr( l.cross( hatu, vecv ) ) ) ) ),               # 2
               AcolorsMathTex( concat( '=', l.gpgradeone( 'I', hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ),               # 2b
               AcolorsMathTex( concat( '=', l.gpgradeone( 'I',                                                          # <3>
                                                          l.lr( l.dot( hatu, l.lr( l.cross( hatu, vecv ) ) ) ), '+',    #
                                                          l.lr( l.wedge( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ) ) ), # </3>
               AcolorsMathTex( concat( '=', 'I',          l.lr( l.wedge( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ) ),   # 4
               AcolorsMathTex( concat( '=', 'I^2',        l.cross( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ),           # 5
               AcolorsMathTex( concat( '= -', l.cross( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ),                       # 6
               AcolorsMathTex( concat( '= ', l.cross( hatu, l.lr( l.cross( vecv, hatu ) ) ) ) ) ]                       # 7

        explainations = [ '',
                          concat( veca, '= ', l.gpgradeone( veca ) ),                                  # 1
                          concat( l.wedge( veca, vecb ), '= I', l.lr( l.cross( veca, vecb ) ) ),       # 2
                          concat( veca, 'I = I', veca ),                                               # 2b
                          concat( veca, 'B = ', l.dot( veca, 'B' ), '+', l.wedge( veca, 'B' ) ),       # 3
                          '',                                                                          # 4
                          concat( l.wedge( veca, vecb), '= I', l.lr( l.cross( veca, vecb ) ) ),        # 5
                          'I^2 = -1',                                                                  # 6
                          concat( l.cross( veca, vecb), '= -', l.lr( l.cross( vecb, veca ) ) ),        # 7
                          '' ]

        self.play( Write( eq[0] ) )
        self.wait( 2 )
        explain( self, explainations[1] )
        i = 0
        write_aligned( self, eq[i], eq[i+1], 0.75 * DOWN, None )

        for i in range(1,8):
            explain( self, explainations[i+1] )
            tx_matching( self, eq[i], eq[i+1], 0.00 * DOWN, None )
            self.wait( 1 )

# vim: et sw=4 ts=4
