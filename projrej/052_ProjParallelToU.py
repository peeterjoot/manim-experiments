from helper import *

class ProjParallelToU( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        projr      = l.mult( invu, lr_udotv )
        rejr       = l.mult( invu, lr_uwedgev )

        labels = DrawVectorsAndProjRej( self, 0 )

        title = Tex( r'$\text{Proj}$ parallel to $\mathbf{u}$.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        title.scale( 1.5 )
        self.add( title )

        eq4 = [ AcolorsMathTex( concat( l.Proj( vecu, vecv ), '=', lr_vdotu, invu ) ),
                AcolorsMathTex( concat( '=', lr_vdotu, hatu, l.pow( l.norm( vecu ), n = -1 ) ) ),
                AcolorsMathTex( concat( '=', l.lr( l.dot( vecv, hatu ) ), hatu ) ) ]
        eq4[0].move_to( title, DOWN )
        eq4[0].shift( 2 * DOWN )
        #eq4[0].set_color_by_tex_to_color_map( acolors )
        self.play( Write( eq4[0] ) )
        self.wait( 2 )

        for i in range(2):
            eq4[i+1].shift( 2 * RIGHT )
            write_aligned( self, eq4[i], eq4[i+1], 1.25 * DOWN, None )
            self.wait( 2 )


# vim: et sw=4 ts=4
