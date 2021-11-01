from helper import *

class ProjRej( Scene ):
    def construct( self ):

        labels = DrawVectorsAndProjRej( self, 0 )

        title = Text( 'The trick: multiply by one.' )
        #.scale(0.75)
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        self.add( title )

        projr       = l.mult( invu, lr_udotv )
        rejr        = l.mult( invu, lr_uwedgev )
        eq2 = AcolorsMathTex( concat( vecv, r' &= 1 \times ', vecv, l.newline ),
                              concat( r' &= ', l.lr( invu, vecu, big = 1 ), vecv, l.newline ),
                              concat( r' &= ', invu, l.lr( vecu, vecv ), l.newline ),
                              concat( r' &= ', invu, l.lr( l.add( udotv, uwedgev ) ), l.newline ),
                              concat( r' &= ', l.add( projr, rejr ), l.newline ) )
        #eq2.set_color_by_tex_to_color_map( acolors )
        eq2.shift( 2 * RIGHT + 0.5 * DOWN )
        for item in eq2:
           self.play( Write( item ) )
           self.wait( 7 )
        self.wait( 1 )
        self.play( FadeOut( eq2 ) )


        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        eq = AcolorsMathTex( concat( vecv, r' &= ', vecv, r'\times 1', l.newline ),
                             concat( r' &= ', vecv, l.lr( vecu, invu, big = 1 ), l.newline ),
                             concat( r' &= ', l.lr( vecv, vecu ), invu, l.newline ),
                             concat( r' &= ', l.lr( l.add( vdotu, vwedgeu ) ), invu, l.newline ),
                             concat( r' &= ', l.add( proj, rej ), l.newline ) )
        #eq.set_color_by_tex_to_color_map( acolors )

        eq.shift( 2 * RIGHT + 0.5 * DOWN )
        for item in eq:
           self.play( Write( item ) )
           self.wait( 1 )
        self.wait( 1 )





# vim: et sw=4 ts=4
