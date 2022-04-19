from helper import *

def explain(self, e):
    move = ( -4.0, -3, 0 )
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

        o = [ -5.0, 0, 0 ]
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
        vrejl = MathTex( concat( hatu, l.lr( l.wedge( hatu, vecv ) ) ) )
        vrejl.set_color( GREEN )
        vrejl.next_to( vrej, 0.2 * RIGHT )

        orejcap = o + rejdir
        orej = o + rej

        au      = Arrow( start = o, end = ou, buff = 0, color = RED )
        aucap   = Arrow( start = o, end = oucap, buff = 0, color = GREEN )
        arejcap = Arrow( start = o, end = orejcap, buff = 0, color = GREEN )
        av      = Arrow( start = o, end = ov, buff = 0, color = YELLOW )
        arej    = Arrow( start = o, end = orej, buff = 0, color = GREEN )
        ul      = MathTex( vecu )
        ucapl   = MathTex( hatu )
        rejcapl = MathTex( concat( hatu, 'i' ) )
        rejl    = MathTex( concat( hatu, r' i \sin\theta' ) )

        ul.set_color( RED )
        ul.next_to( au, RIGHT )
        ul.shift( 0.5 * LEFT )

        vl = MathTex( vecv )
        vl.set_color( YELLOW )
        vl.next_to( av, UP )
        vl.shift( 0.5 * DOWN )

        ucapl.set_color( GREEN )
        ucapl.next_to( aucap, RIGHT )
        ucapl.shift( 0.5 * LEFT + 0.25 * DOWN )

        rejcapl.set_color( GREEN )
        rejcapl.next_to( arejcap, RIGHT )
        rejcapl.shift( 1.25 * LEFT + 0.25 * UP )

        rejl.set_color( GREEN )
        rejl.move_to( rejcapl )
        rejl.shift( 0.0 * LEFT + 2.0 * UP )

        ltheta = MathTex( r'\theta' )
        ltheta.move_to( o + 0.5 * (UP + RIGHT) )

        all = VGroup( au, ul, av, vl, vrej, vrejl, ltheta )

        self.add( all )


        veca = l.vec( 'a' )
        vecb = l.vec( 'b' )
        eq1 = [ AcolorsMathTex( concat( l.Rej( vecu, vecv ), '=', hatu, l.lr( l.wedge( hatu, vecv ) ) ) ),               # 0
               AcolorsMathTex( concat( '=', l.gpgradeone( hatu, l.lr( l.wedge( hatu, vecv ) ) ) ) ),                    # 1
               AcolorsMathTex( concat( '=', l.gpgradeone( hatu, 'I', l.lr( l.cross( hatu, vecv ) ) ) ) ),               # 2
               AcolorsMathTex( concat( '=', l.gpgradeone( 'I', hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ),               # 3
               AcolorsMathTex( concat( '=', l.gpgradeone( 'I',
                                                          l.lr( l.dot( hatu, l.lr( l.cross( hatu, vecv ) ) ) ), '+ I^2',
                                                          l.lr( l.cross( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ) ) )  # 4
               ]

        eq3 = [
               AcolorsMathTex( '=' ),
               AcolorsMathTex( l.gpgradeone( 'I', l.dot( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ),
               AcolorsMathTex( '+' ),
               AcolorsMathTex( l.gpgradeone( 'I^2', l.lr( l.cross( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ) )
               ]

        eq2 = [
               AcolorsMathTex( concat( '=', 'I^2',        l.cross( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ),           # 6
               AcolorsMathTex( concat( '= -', l.cross( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ),                       # 7
               AcolorsMathTex( concat( '= ', l.cross( hatu, l.lr( l.cross( vecv, hatu ) ) ) ) ) ]                       # 8

        explainations1 = [ '',
                           concat( veca, '= ', l.gpgradeone( veca ) ),                                   # 1
                           concat( l.wedge( veca, vecb ), '= I', l.lr( l.cross( veca, vecb ) ) ),        # 2
                           concat( veca, 'I = I', veca ),                                                # 3
                           concat( veca, vecb, ' = ', l.dot( veca, vecb ), '+', 'I', l.lr( l.cross( veca, vecb ) ) ), # 4
                           '' ]                                                                          # 5

        explainations2 = [ '',                                                                           # 6
                           'I^2 = -1',                                                                   # 7
                           concat( l.cross( veca, vecb), '= -', l.lr( l.cross( vecb, veca ) ) ),         # 8
                           '' ]


        eq1[0].shift( DOWN + LEFT )
        eq2[0].shift( DOWN + LEFT )
        eq3[0].shift( DOWN + LEFT )
        self.play( Write( eq1[0] ) )
        self.wait( 2 )
        explain( self, explainations1[1] )
        i = 0
        write_aligned( self, eq1[i], eq1[i+1], 0.75 * DOWN, None )
        last = eq1[i+1]

        for i in range(1,4):
            explain( self, explainations1[i+1] )
            tx_matching( self, last, eq1[i+1], 0.00 * DOWN, None )
            self.wait( 3 )
            last = eq1[i+1]

        eq3[0].move_to( last )
        eq3[1].next_to( eq3[0], RIGHT )
        eq3[2].next_to( eq3[1], RIGHT )
        eq3[3].next_to( eq3[2], RIGHT )
        g = VGroup(*eq3)
        tx_matching( self, last, g, 0.00 * DOWN, None )
        self.wait(1)
        self.play( Indicate( eq3[1] ) )
        self.wait(1)
        self.play( Indicate( eq3[3] ) )
        self.wait(1)
        remainder = AcolorsMathTex( concat( '=', l.gpgradeone( 'I^2', l.lr( l.cross( hatu, l.lr( l.cross( hatu, vecv ) ) ) ) ) ) )
        remainder.next_to( last )
        remainder.shift( 8 * LEFT )
        self.play( ReplacementTransform( g, remainder ) )
        last = remainder

        for i in range(3):
            explain( self, explainations2[i] )
            tx_matching( self, last, eq2[i], 0.00 * DOWN, None )
            self.wait( 1 )
            last = eq2[i]

        self.play( ReplacementTransform( VGroup(au, ul), VGroup(aucap, ucapl) ) )
        self.wait( 1 )
        self.play( ReplacementTransform( VGroup(aucap, ucapl, ltheta), VGroup(arejcap, rejcapl) ) )
        self.wait( 1 )
        self.play( ReplacementTransform( VGroup(arejcap, rejcapl), VGroup(arej, rejl) ) )
        self.wait( 1 )


# vim: et sw=4 ts=4
