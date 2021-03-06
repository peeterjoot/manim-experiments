from helper import *

class ProjRej2( Scene ):
    def construct( self ):
        proj       = l.mult( lr_vdotu, invu )
        rej        = l.mult( lr_vwedgeu, invu )
        projr      = l.mult( invu, lr_udotv )
        rejr       = l.mult( invu, lr_uwedgev )

        labels = DrawVectorsAndProjRej( self, 0 )

        claim = Text( "Claim: " )
        claim.move_to( 3 * UP )
        claim.set_color( BLUE )
        #These components of v are the projection and rejection."
        self.play( Write( claim ) )

        #howorig = MathTex( concat( vecv, ' = ', vecv, vecu, invu ) )
        #howorig.set_color_by_tex_to_color_map( acolors )
        #howorig.move_to( 2 * UP + 1.0 * LEFT )

        #howreversed = MathTex( concat( vecv, ' = ', invu, vecu, vecv ) )
        #howreversed.set_color_by_tex_to_color_map( acolors )
        #howreversed.move_to( 2 * UP + 1.8 * RIGHT )


        eqa = AcolorsMathTex( l.Proj( vecu, vecv ), ' \equiv ', proj )
        eqa.shift( 0 * LEFT + 1 * UP )
        #self.play( AnimationGroup( FadeIn( howorig ), Write( eqa ) ) )
        self.play( Write( eqa ) )

        eqb = AcolorsMathTex( l.Rej( vecu, vecv ),  ' \equiv ', rej )
        write_aligned( self, eqa, eqb, 1.25 * DOWN, None, 'Proj' )
        self.wait(10)

        eqreversed1 = AcolorsMathTex( concat( '=', projr ) )
        eqreversed2 = AcolorsMathTex( concat( '=', rejr ) )

        eqreversed1.next_to( eqa, RIGHT );
        eqreversed2.next_to( eqb, RIGHT );

        #self.play( AnimationGroup( FadeIn( howreversed ), Write( eqreversed1 ), Write( eqreversed2 ) ) )
        self.play( Write( eqreversed1 ), Write( eqreversed2 ) )
        self.wait( 20 )

        blist = BulletedList( r'Must show that $\text{Proj}$ is parallel to $\mathbf{u}$,',
                              r'that $\text{Rej}$ is perpendicular to $\mathbf{u}$,',
                              r'and that $\text{Rej}$ is a vector.',
                              height = 1.5 )
        blist.next_to( eqa, DOWN )
        blist.shift( 1.5 * DOWN )
        blist.set_color( BLUE )
        for item in blist:
            self.play( Write( item ) )
            self.wait( 12 )

        self.wait( 10 )



        #self.play( AnimationGroup( FadeOut( howreversed ), FadeOut( howorig ) ) )
        #self.wait( )

        #proj2      = l.mult( l.lr( l.dot( vecv, hatu ) ), hatu )
        #rej2       = l.mult( l.lr( l.wedge( vecv, hatu ) ), hatu )
        #rej2r      = l.mult( hatu, l.lr( l.wedge( hatu, vecv ) ) )
        #equnit1 = AcolorsMathTex( concat( '=', proj2 ) )
        #equnit2 = AcolorsMathTex( concat( '=', rej2 ) )
        #equnit2r = AcolorsMathTex( concat( '=', rej2r ) )
        #self.wait( 14 )
        #equnit1.next_to( eqreversed1, RIGHT )
        #equnit2.next_to( eqreversed2, RIGHT )
        #equnit2r.next_to( eqreversed2, RIGHT )
        #self.play( AnimationGroup( Write( equnit1 ), Write( equnit2 ) ) )
        #self.wait( 1 )
        #self.play( TransformMatchingTex( equnit2, equnit2r ) )
        #self.wait( 7 )
        #self.play( ReplacementTransform( eqreversed, equnit ) )



# vim: et sw=4 ts=4
