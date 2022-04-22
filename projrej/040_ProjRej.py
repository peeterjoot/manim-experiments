from helper import *

class ProjRej( Scene ):
    def construct( self ):

        labels = DrawVectorsAndProjRej( self, 0 )

        title = Text( 'The trick: multiply by one.' )
        #.scale(0.75)
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )
        self.wait( 7 )

        projr       = l.mult( invu, lr_udotv )
        rejr        = l.mult( invu, lr_uwedgev )
        eq2 = [ AcolorsMathTex( concat( vecv, r' = 1 \times ', vecv, l.newline ) ),
                AcolorsMathTex( concat( ' = ', l.lr( invu, vecu, big = 1 ), vecv, l.newline ) ),
                AcolorsMathTex( concat( ' = ', invu, l.lr( vecu, vecv ), l.newline ) ),
                AcolorsMathTex( concat( ' = ', invu, l.lr( l.add( udotv, uwedgev ) ), l.newline ) ),
                AcolorsMathTex( concat( ' = ', l.add( projr, rejr ), l.newline ) ) ]
        delays = [ 8, 5, 7, 4, 4 ]

        eq2[0].shift( 0 * RIGHT + 2.0 * UP )
        i = 0
        self.play( Write( eq2[i]) )
        self.wait( delays[i] )
        for i in range(4):
           write_aligned( self, eq2[i], eq2[i+1], 1.15 * DOWN, None )
           self.wait( delays[i+1] )

        self.wait( 4 )
        self.play( FadeOut( *eq2 ) )
        self.wait( 4 )


        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        eq = [ AcolorsMathTex( concat( vecv, ' = ', vecv, r'\times 1', l.newline ) ),
               AcolorsMathTex( concat( ' = ', vecv, l.lr( vecu, invu, big = 1 ), l.newline ) ),
               AcolorsMathTex( concat( ' = ', l.lr( vecv, vecu ), invu, l.newline ) ),
               AcolorsMathTex( concat( ' = ', l.lr( l.add( vdotu, vwedgeu ) ), invu, l.newline ) ),
               AcolorsMathTex( concat( ' = ', l.add( proj, rej ), l.newline ) ) ]

        i = 0
        eq[0].move_to( eq2[0] )
        i = 0
        self.play( Write( eq[i]) )
        self.wait( delays[i] )
        for i in range(4):
           write_aligned( self, eq[i], eq[i+1], 1.15 * DOWN, None )
           self.wait( delays[i+1] )

        self.wait( 8 )

# vim: et sw=4 ts=4
