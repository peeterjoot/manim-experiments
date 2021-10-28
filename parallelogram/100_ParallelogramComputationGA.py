from helper import *
from helper2 import *

class ParallelogramComputationGA( Scene ):
    def construct( self ):
        DrawVectorsAndProjRej( self, 1 )

        vdotusq    = l.lrsq( vdotu )
        rej        = l.mult( lr_vwedgeu, invu )
        rrej       = l.mult( invu, lr_uwedgev )
        ar_a = [ t_area, '=', t_base, r' \times ', t_height ]
        ar_0 = [ l.sq( t_area ), '=', l.sq( t_base ), r' \times ', l.sq( t_height ) ]
        eq_a = MathTex( *ar_a )
        eq_a.set_color_by_tex_to_color_map( acolors )
        eq_a.shift( 2.0 * UP + 2.0 * RIGHT )

        eq_0 = MathTex( *ar_0 )
        eq_0.set_color_by_tex_to_color_map( acolors )
        eq_0.shift( 2.05 * UP + 2.0 * RIGHT )

        self.play( Write( eq_a ) )
        self.wait( )
        self.play( TransformMatchingTex( eq_a, eq_0 ) )
        self.wait( )

        eq_1 = MathTex( '=', uu, l.lrsq( rej, big = 1 ) )
        write_aligned( self, eq_0, eq_1, 1.0 * DOWN, acolors )
        self.wait( )

        eq_2 = MathTex( '=', uu, rej, rrej )
        tx_aligned( self, eq_1, eq_2, 0 * UP, acolors )
        self.wait( )

        eq_3 = MathTex( '=', rej, uu, rrej )
        tx_aligned( self, eq_2, eq_3, 0 * UP, acolors )
        self.wait( )


        eq_4 = MathTex( '=', l.neg( l.lrsq( vwedgeu ) ) )
        tx_aligned( self, eq_3, eq_4, 0.1 * UP, acolors )
        self.wait( )


        eq_5 = MathTex( l.lrsq( vwedgeu ), '=', l.dot( lr_vwedgeu, lr_vwedgeu ) )
        eq_5.set_color_by_tex_to_color_map( acolors )
        eq_5.move_to( eq_a, LEFT )
        eq_5.shift( 3 * DOWN + 0.8 * LEFT )
        self.play( Write( eq_5 ) )
        self.wait( )

        eq_6 = MathTex( '=', l.dot( vecv, l.lr( l.dot( vecu, lr_vwedgeu ) ) ) )
        write_aligned( self, eq_5, eq_6, 0.75 * DOWN, acolors )
        self.wait( )

        eq_7 = MathTex( '=', l.dot( vecv, l.lr( l.sub( l.mult( lr_udotv, vecu ), l.mult( uu, vecv ) ) ) ) )
        tx_aligned( self, eq_6, eq_7, 0 * DOWN, acolors )
        self.wait( )

        eq_8 = MathTex( '=', l.sub( vdotusq, l.mult( uu, vv ) ) )
        tx_aligned( self, eq_7, eq_8, 0 * DOWN, acolors )
        self.wait( )

        self.play( FadeOut( VGroup( eq_5, eq_8 ) ) )
        self.wait( )

        eq_9 = MathTex( '=', l.sub( l.mult( uu, vv ), vdotusq ) )
        write_aligned( self, eq_4, eq_9, 0.75 * DOWN, acolors )
        self.wait( )



# vim: et sw=4 ts=4
