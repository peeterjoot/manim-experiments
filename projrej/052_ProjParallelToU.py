from helper import *

class ProjParallelToU( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        projr      = l.mult( invu, lr_udotv )
        rejr       = l.mult( invu, lr_uwedgev )

        labels = DrawVectorsAndProjRej( self, 0 )

        what_to_prove = Tex( r'PROOF: $\text{Proj}$ is parallel to $\mathbf{u}$.' )
        what_to_prove.move_to( 3 * UP )
        what_to_prove.set_color( BLUE )
        self.play( Write( what_to_prove ) )

        eq4 = [ MathTex( concat( l.Proj( vecu, vecv ), '=', lr_vdotu, invu ) ),
                MathTex( concat( '=', lr_vdotu, hatu, l.pow( l.norm( vecu ), n = -1 ) ) ),
                MathTex( concat( '=', l.lr( l.dot( vecv, hatu ) ), hatu ) ) ]
        eq4[0].move_to( eq, DOWN )
        eq4[0].shift( 0 * DOWN )
        eq4[0].set_color_by_tex_to_color_map( acolors )
        self.play( Write( eq4[0] ) )
        self.wait( 2 )

        for i in range(2):
            write_aligned( self, eq4[i], eq4[i+1], 1.25 * DOWN, acolors )
            self.wait( 2 )


# vim: et sw=4 ts=4
