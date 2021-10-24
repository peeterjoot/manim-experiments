from helper import *

class ProjRej2( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        proj2      = l.mult( l.lr( l.dot( vecv, hatu ) ), hatu )
        rej2       = l.mult( l.lr( l.wedge( vecv, hatu ) ), hatu )
        projr      = l.mult( invu, lr_udotv )
        rejr       = l.mult( invu, lr_uwedgev )

        eq = MathTex( l.Proj( vecu, vecv ), ' &\equiv ', proj, l.newline,
                      l.Rej( vecu, vecv ),  ' &\equiv ', rej, l.newline )
        eqreversed = MathTex( concat( '&=', projr, l.newline ),
                              concat( '&=', rejr, l.newline ) )
        equnit = MathTex( concat( '&=', proj2, l.newline ),
                          concat( '&=', rej2, l.newline ) )
        eq[2].set_color( BLUE )
        eq[6].set_color( BLUE )

        for i in range(0, 3):
            self.play( Write( eq[i] ) )
        self.wait(3)
        # +7s

        for i in range(4, 8):
            self.play( Write( eq[i] ) )
        self.wait(2)
        # +7s

        self.wait(5)
        eqreversed.shift( 2.5 * RIGHT )
        eqreversed.set_color( TEAL )
        self.play( eq.animate.shift( 1.3 * LEFT ) )
        for i in range(2):
            self.play( Write( eqreversed[i] ) )
        self.wait( 5 )

        howorig = MathTex( concat( vecv, ' = ', vecv, vecu, invu ) )
        howorig.set_color( BLUE )
        howorig.move_to( 2 * UP + 0.2 * LEFT )

        howreversed = MathTex( concat( vecv, ' = ', invu, vecu, vecv ) )
        howreversed.set_color( TEAL )
        howreversed.move_to( 2 * UP + 2.8 * RIGHT )
        self.wait( 1 )

        self.play( AnimationGroup( FadeIn( howreversed ), FadeIn( howorig ) ) )
        self.wait( 1 )
        self.play( AnimationGroup( FadeOut( howreversed ), FadeOut( howorig ) ) )
        self.wait( 2 )

        self.wait( 14 )
        equnit[0].shift( 2.5 * RIGHT + 0.2 * UP )
        equnit[1].shift( 2.5 * RIGHT + 0.25 * DOWN )
        equnit.set_color( RED )
        self.play( ReplacementTransform( eqreversed, equnit ) )
        self.wait( 8 )



# vim: et sw=4 ts=4
