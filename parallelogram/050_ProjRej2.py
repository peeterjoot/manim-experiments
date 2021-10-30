from helper import *

class ProjRej2( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        proj2      = l.mult( l.lr( l.dot( vecv, hatu ) ), hatu )
        rej2       = l.mult( l.lr( l.wedge( vecv, hatu ) ), hatu )
        projr      = l.mult( invu, lr_udotv )
        rejr       = l.mult( invu, lr_uwedgev )

        eqa = MathTex( l.Proj( vecu, vecv ), ' \equiv ', proj )
        eqa.set_color_by_tex_to_color_map( acolors )
        eqa.shift( 2 * LEFT )
        self.play( Write( eqa ) )

        eqb = MathTex( l.Rej( vecu, vecv ),  ' \equiv ', rej )
        write_aligned( self, eqa, eqb, 1.25 * DOWN, acolors, 'Proj' )
        self.wait(3)
        # +7s
        self.wait(2)
        # +7s

        eqreversed1 = MathTex( concat( '=', projr ) )
        eqreversed2 = MathTex( concat( '=', rejr ) )

        self.wait(5)
        eqreversed1.next_to( eqa, RIGHT );
        eqreversed1.set_color_by_tex_to_color_map( acolors )
        eqreversed2.next_to( eqb, RIGHT );
        eqreversed2.set_color_by_tex_to_color_map( acolors )

        self.play( AnimationGroup( Write( eqreversed1 ), Write( eqreversed2 ) ) )
        self.wait( 5 )

        howorig = MathTex( concat( vecv, ' = ', vecv, vecu, invu ) )
        howorig.set_color_by_tex_to_color_map( acolors )
        howorig.move_to( 2 * UP + 0.2 * LEFT )

        howreversed = MathTex( concat( vecv, ' = ', invu, vecu, vecv ) )
        howreversed.set_color_by_tex_to_color_map( acolors )
        howreversed.move_to( 2 * UP + 2.8 * RIGHT )

        self.play( AnimationGroup( FadeIn( howreversed ), FadeIn( howorig ) ) )
        self.wait( 1 )
        self.play( AnimationGroup( FadeOut( howreversed ), FadeOut( howorig ) ) )
        self.wait( 1 )


        equnit1 = MathTex( concat( '=', proj2 ) )
        equnit2 = MathTex( concat( '=', rej2 ) )
        self.wait( 14 )
        equnit1.next_to( eqreversed1, RIGHT )
        equnit2.next_to( eqreversed2, RIGHT )
        equnit1.set_color_by_tex_to_color_map( acolors )
        equnit2.set_color_by_tex_to_color_map( acolors )
        self.play( AnimationGroup( Write( equnit1 ), Write( equnit2 ) ) )
        #self.play( ReplacementTransform( eqreversed, equnit ) )
        self.wait( 8 )



# vim: et sw=4 ts=4
