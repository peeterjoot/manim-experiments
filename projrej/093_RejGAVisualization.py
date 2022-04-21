from helper import *

waittime = 5

class RejGAVisualization( Scene ):
    def construct( self ):

        title = Tex( 'Rejection: $\mathbb{R}^3$ GA visualization.' )
        title.move_to( 3 * UP )
        title.set_color( BLUE )
        title.scale( 1.5 )
        self.add( title )

        o = [ -0.0, -1.5, 0 ]
        du = np.array( [ 3, 1, 0 ] )
        dv = np.array( [ 1, 3, 0 ] )
        ou = o + du
        ov = o + dv

        ucapdir = du/ np.linalg.norm( du )
        oucap = o + ucapdir
        proj = np.dot( dv, ucapdir ) * ucapdir
        oproj = o + proj

        rej = dv - proj
        rejdir = rej/ np.linalg.norm( rej )
        vrej = Arrow( start = oproj, end = ov, color = GREEN, buff = 0 )
        vrejl = AcolorsMathTex( concat( hatu, l.lr( l.wedge( hatu, vecv ) ) ) )
        #vrejl.set_color( GREEN )
        vrejl.next_to( vrej, 0.2 * RIGHT )

        orejcap = o + rejdir
        orej = o + rej

        au      = Arrow( start = o, end = ou, buff = 0, color = RED )
        aucap   = Arrow( start = o, end = oucap, buff = 0, color = GREEN )
        arejcap = Arrow( start = o, end = orejcap, buff = 0, color = GREEN )
        av      = Arrow( start = o, end = ov, buff = 0, color = YELLOW )
        arej    = Arrow( start = o, end = orej, buff = 0, color = GREEN )
        ul      = AcolorsMathTex( vecu )
        ucapl   = AcolorsMathTex( hatu )
        rejcapl = AcolorsMathTex( concat( hatu, 'i' ) )
        rejl    = AcolorsMathTex( concat( hatu, r' i ', l.norm( vecv ), r' \sin\theta' ) )

        #ul.set_color( RED )
        ul.next_to( au, RIGHT )
        ul.shift( 0.5 * LEFT )

        vl = AcolorsMathTex( vecv )
        #vl.set_color( YELLOW )
        vl.next_to( av, UP )
        vl.shift( 0.5 * DOWN )

        ucapl.set_color( PURPLE )
        ucapl.next_to( aucap, RIGHT )
        ucapl.shift( 0.5 * LEFT + 0.25 * DOWN )

        #rejcapl.set_color( GREEN )
        rejcapl.next_to( arejcap, RIGHT )
        rejcapl.shift( 1.25 * LEFT + 0.25 * UP )

        #rejl.set_color( GREEN )
        rejl.move_to( rejcapl )
        rejl.shift( 0.5 * LEFT + 2.0 * UP )

        ltheta = MathTex( r'\theta' )
        ltheta.move_to( o + 0.5 * (UP + RIGHT) )

        eq = [
              AcolorsMathTex( concat( l.wedge( hatu, vecv ), ' = ' ) ),
              AcolorsMathTex( l.frac( l.wedge( hatu, vecv ), l.norm( l.wedge( hatu, vecv ) ) ) ),
              AcolorsMathTex( l.norm( vecv ), r' \sin\theta' ),
              AcolorsMathTex( ' = i ', l.norm( vecv ), r' \sin\theta' ) ]

        eq[0].move_to( [ -3.0, -2.5, 0 ] )
        eq[1].next_to( eq[0], RIGHT )
        eq[2].next_to( eq[1], RIGHT )
        eq[3].next_to( eq[2], RIGHT )

        all = VGroup( au, ul, av, vl, vrej, vrejl, ltheta, *eq )

        self.add( all )
        self.play( Indicate( eq[1] ) )
        self.wait( waittime )
        self.play( Indicate( eq[2] ) )
        self.wait( waittime )

        ug = VGroup(aucap, ucapl)
        self.play( ReplacementTransform( VGroup(au, ul), ug ) )
        self.wait( waittime )
        self.add( VGroup( aucap.copy(), ucapl.copy() ) )
        self.play( ReplacementTransform( VGroup(aucap, ucapl, ltheta), VGroup(arejcap, rejcapl) ) )
        self.wait( waittime )
        self.play( ReplacementTransform( VGroup(arejcap, rejcapl), VGroup(arej, rejl) ) )
        self.wait( waittime )


# vim: et sw=4 ts=4
